from django.test import TestCase
from django.urls import reverse

from .models import Product, Box, Order, OrderItem
from .services import recommend_box


class BoxRecommendationTest(TestCase):

    def setUp(self):

        # Create Products
        self.tshirt = Product.objects.create(
            name="T-Shirt",
            length=20,
            width=15,
            height=5,
            weight=0.3
        )

        self.shoes = Product.objects.create(
            name="Shoes",
            length=30,
            width=20,
            height=12,
            weight=1.0
        )

        # Create Boxes
        self.small_box = Box.objects.create(
            name="Small Box",
            length=30,
            width=25,
            height=15,
            max_weight=2,
            cost=20
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            length=40,
            width=30,
            height=20,
            max_weight=5,
            cost=30
        )

        self.large_box = Box.objects.create(
            name="Large Box",
            length=60,
            width=40,
            height=30,
            max_weight=10,
            cost=50
        )

        # Create Order
        self.order = Order.objects.create()

    def test_cheapest_suitable_box(self):

        OrderItem.objects.create(
            order=self.order,
            product=self.tshirt,
            quantity=1
        )

        result = recommend_box(self.order)

        self.assertEqual(result.name, "Small Box")

    def test_weight_exceeds_capacity(self):

        heavy_product = Product.objects.create(
            name="Heavy Product",
            length=10,
            width=10,
            height=10,
            weight=15
        )

        OrderItem.objects.create(
            order=self.order,
            product=heavy_product,
            quantity=1
        )

        result = recommend_box(self.order)

        self.assertIsNone(result)

    def test_dimensions_exceed_all_boxes(self):

        big_product = Product.objects.create(
            name="Big Product",
            length=100,
            width=100,
            height=100,
            weight=1
        )

        OrderItem.objects.create(
            order=self.order,
            product=big_product,
            quantity=1
        )

        result = recommend_box(self.order)

        self.assertIsNone(result)

    def test_product_rotation(self):

        rotated_product = Product.objects.create(
            name="Rotated Product",
            length=25,
            width=15,
            height=30,
            weight=1
        )

        OrderItem.objects.create(
            order=self.order,
            product=rotated_product,
            quantity=1
        )

        result = recommend_box(self.order)

        self.assertEqual(result.name, "Small Box")

    def test_multiple_quantities_weight(self):

        OrderItem.objects.create(
            order=self.order,
            product=self.tshirt,
            quantity=3
        )

        result = recommend_box(self.order)

        self.assertEqual(result.name, "Small Box")

    def test_invalid_order_api(self):

        response = self.client.get(
            reverse("recommend_box", args=[999])
        )

        self.assertEqual(response.status_code, 404)

    
    def test_combined_volume_exceeds_small_box(self):

        # Create an order with two shoes
        OrderItem.objects.create(
            order=self.order,
            product=self.shoes,
            quantity=2
        )

        result = recommend_box(self.order)

        # Small box volume is insufficient.
        # Medium box should be recommended.
        self.assertEqual(result.name, "Medium Box")

    def test_empty_order_returns_none(self):

        result = recommend_box(self.order)

        self.assertIsNone(result)


    def test_api_success_response(self):

        OrderItem.objects.create(
            order=self.order,
            product=self.tshirt,
            quantity=1
        )

        response = self.client.get(
            reverse("recommend_box", args=[self.order.id])
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["order_id"], self.order.id)
        self.assertEqual(data["recommended_box"]["name"], "Small Box")
        self.assertEqual(data["recommended_box"]["cost"], "20.00")

    def test_api_empty_order_response(self):

        response = self.client.get(
            reverse("recommend_box", args=[self.order.id])
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertIsNone(data["recommended_box"])
        self.assertEqual(data["message"], "No suitable box found")



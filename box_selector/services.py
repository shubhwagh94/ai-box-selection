
from .models import Box


def recommend_box(order):

    # Get all order items with product details
    items = list(order.items.select_related("product"))

    # Return None if order is empty
    if not items:
        return None

    # Calculate total weight and volume
    total_weight = sum(
        item.product.weight * item.quantity
        for item in items
    )

    total_volume = sum(
        item.product.length
        * item.product.width
        * item.product.height
        * item.quantity
        for item in items
    )

    suitable_boxes = []

    for box in Box.objects.all():

        # Check maximum weight
        if total_weight > box.max_weight:
            continue

        # Check whether each product fits individually
        box_dimensions = sorted([
            box.length,
            box.width,
            box.height
        ])

        all_products_fit = True

        for item in items:
            product = item.product

            product_dimensions = sorted([
                product.length,
                product.width,
                product.height
            ])

            if not all(
                p <= b
                for p, b in zip(product_dimensions, box_dimensions)
            ):
                all_products_fit = False
                break

        if not all_products_fit:
            continue

        # Check combined product volume
        box_volume = box.length * box.width * box.height

        if total_volume > box_volume:
            continue

        suitable_boxes.append(box)

    # Select the cheapest suitable box
    if suitable_boxes:
        return min(suitable_boxes, key=lambda box: box.cost)

    return None

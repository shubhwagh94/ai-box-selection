from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Order
from .services import recommend_box


def recommend_box_api(request, order_id):

    if request.method != "GET":
        return JsonResponse(
            {"error": "Only GET method is allowed"},
            status=405
        )

    order = get_object_or_404(Order, id=order_id)

    recommended_box = recommend_box(order)

    total_weight = sum(
        item.product.weight * item.quantity
        for item in order.items.all()
    )

    if recommended_box is None:
        return JsonResponse({
            "order_id": order.id,
            "total_weight": total_weight,
            "recommended_box": None,
            "message": "No suitable box found"
        })

    return JsonResponse({
        "order_id": order.id,
        "total_weight": total_weight,
        "recommended_box": {
            "name": recommended_box.name,
            "cost": str(recommended_box.cost),
            "dimensions": {
                "length": recommended_box.length,
                "width": recommended_box.width,
                "height": recommended_box.height
            }
        },
        "message": "Suitable box found successfully"
    })

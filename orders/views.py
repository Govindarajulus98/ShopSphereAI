from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order


@login_required
def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = sum(item.total_price() for item in cart_items)

    return render(request, "orders/checkout.html", {
        "cart_items": cart_items,
        "total": total
    })


@login_required
def place_order(request):

    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect("cart")

    for item in cart_items:

        Order.objects.create(
            user=request.user,
            product=item.product,
            quantity=item.quantity,
            total_price=item.total_price(),
            status="Pending"
        )

    # Empty Cart
    cart_items.delete()

    return redirect("my_orders")


@login_required
def my_orders(request):

    orders = Order.objects.filter(user=request.user)

    return render(request, "orders/my_orders.html", {
        "orders": orders
    })
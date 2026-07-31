from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart
from products.models import Product


@login_required
def add_to_cart(request, id):
    product = Product.objects.get(id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.total_price()

    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total": total
    })
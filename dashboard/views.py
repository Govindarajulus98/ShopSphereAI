from django.shortcuts import render
from django.contrib.auth.models import User
from products.models import Product, Category
from orders.models import Order
from cart.models import Cart
from wishlist.models import Wishlist


def dashboard_home(request):

    context = {
        "users": User.objects.count(),
        "products": Product.objects.count(),
        "categories": Category.objects.count(),
        "orders": Order.objects.count(),
        "cart": Cart.objects.count(),
        "wishlist": Wishlist.objects.count(),
    }

    return render(request, "dashboard/dashboard.html", context)
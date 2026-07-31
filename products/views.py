from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Product
from reviews.models import Review


def product_list(request):
    query = request.GET.get("q")

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query)
        )
    else:
        products = Product.objects.all()

    return render(request, "products/product_list.html", {
        "products": products
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    reviews = Review.objects.filter(product=product)

    return render(request, "products/product_detail.html", {
        "product": product,
        "reviews": reviews,
    })
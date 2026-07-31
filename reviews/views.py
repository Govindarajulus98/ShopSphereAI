from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from products.models import Product


@login_required
def add_review(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":

        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Review.objects.create(
            user=request.user,
            product=product,
            rating=rating,
            comment=comment
        )

        return redirect("product_detail", id=id)
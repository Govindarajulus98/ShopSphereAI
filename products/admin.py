from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "brand",
        "price",
        "stock",
        "created_at",
    )

    list_filter = ("category", "brand")
    search_fields = ("name", "brand")
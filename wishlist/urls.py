from django.urls import path
from . import views

urlpatterns = [
    path("", views.wishlist_view, name="wishlist"),
    path("add/<int:id>/", views.add_to_wishlist, name="add_to_wishlist"),
]
from django.urls import path
from . import views


urlpatterns = [
    path('cart', views.cart_detail, name='cart'),
    path("cart_add/<book_id>", views.cart_add, name='cart_add'),
    path("cart_remove/<book_id>", views.cart_remove, name='cart_remove'),
]

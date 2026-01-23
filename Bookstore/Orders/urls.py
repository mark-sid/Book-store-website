from django.urls import path
from . import views

urlpatterns = [
    path('order_create', views.OrderCreateView.as_view(), name='order_create')
]

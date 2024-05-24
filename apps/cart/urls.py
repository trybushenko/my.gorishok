from django.urls import path

from .views import (cart_view, checkout_view, add_to_cart, remove_from_cart)

app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/', add_to_cart, name='add_to_cart'),
    path('remove/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout_view, name='checkout'),
]
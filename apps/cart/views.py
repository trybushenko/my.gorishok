import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from .models import ShoppingSession, CartItem

# Create your views here.

def cart_view(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('login')
    
    shopping_session, created = ShoppingSession.objects.get_or_create(user=user)
    cart_items = CartItem.objects.filter(session=shopping_session)

    context = {
        'cart_items' : cart_items,
        'cart' : shopping_session
    }

    return render(request, 'cart/cart.html', context)

@login_required
def checkout_view(request):
    user = request.user
    try:
        shopping_session = ShoppingSession.objects.get(user=user)
        cart_items = CartItem.objects.filter(session=shopping_session)
    except ShoppingSession.DoesNotExist:
        shopping_session = None
        cart_items = None

    if request.method == 'POST':
        return redirect('cart:checkout_process')
    
    context = {
        'cart_items' : cart_items,
        'cart' : shopping_session
    }

    return render(request, 'cart/checkout.html', context)
    
@require_POST
def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    # product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        user = request.user
    else:
        user = get_user_model().objects.get(email=request.session.get('guest_email'))

    shopping_session, created = ShoppingSession.objects.get_or_create(user=user)

    cart_item, created = CartItem.objects.get_or_create(session=shopping_session, product_id=product_id)
    cart_item.quantity += int(quantity)
    cart_item.save()

    return JsonResponse({'status' : 'success', 'message' : 'Product had been added to cart'})

@require_POST
def remove_from_cart(request):
    data = json.loads(request.body)
    product_id = data.get('product_id')

    if request.user.is_authenticated:
        user = request.user
    else:
        user = get_user_model().objects.get(email=request.session.get('guest_email'))

    shopping_session = get_object_or_404(ShoppingSession, user=user)

    cart_item = get_object_or_404(CartItem, session=shopping_session, product_id=product_id)
    cart_item.delete()

    return JsonResponse({'status': 'success', 'message': 'Product has been removed from cart'})
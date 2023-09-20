from django.shortcuts import render, redirect
from .models import Product, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce_app/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            user=request.user
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('cart')


def cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        cart_items = []

    return render(request, 'ecommerce_app/cart.html', {'cart_items': cart_items})
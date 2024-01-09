from django.shortcuts import render, get_object_or_404
from .cart import Cart
from website.models import Product
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    cart_quantity = cart.get_quantities()
    return render(request, 'cart_summary.html',{'cart_products':cart_products,'cart_quantity':cart_quantity})
def cart_add(request):
    cart = Cart(request)
    # test for Post
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product,id = product_id)
        cart.add(product=product, quantity=product_qty)
        #get cart quatity
        cart_quatity = cart.__len__()
        response = JsonResponse({
            'qty':cart_quatity
        })
        return response
        
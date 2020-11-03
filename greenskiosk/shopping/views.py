from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, request
from django.core.exceptions import ObjectDoesNotExist
from catalogue.models import Product
from .models import Cart
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm
from django.urls import reverse

# Create your views here.

@require_POST
def cart_add(request, product_id):
    try:
        cart_id = request.session['cart_id']
        cart=Cart.objects.get(id=cart_id)
    except KeyError:
        cart = Cart.objects.create(status="new")
        request.session['cart_id'] = cart.id
        
    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        return render(request, 'detail.html', {"error": "cart does not exist"})

    cart.products.add(product)
    products = cart.products.all()

    if request.user.is_authenticated and not cart.owner:
        cart.owner = request.user
        cart.save()

    return render(request, "detail.html", {"products": products})
    

    
def cart_remove(request, product_id):
    try:
        cart_id = request.session['cart_id']
    except KeyError:
        return render(request, "detail.html", {"error": "Cart  not found"})

    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        return render(request, "detail.html", {"error": "Product  not found"})

    cart = Cart.objects.get(id=cart_id)
    cart.products.remove(product)
    products = cart.products.all()
    
    return render(request, "detail.html", {"products": products})
      

def cart_detail(request):
    """ 
         Try block checks if there already is a session,the except block checks for an empty cart
         ,if it there's none it queries the cart by id and looks for the contents in the cart 
         else returns the template that renders the view. 
     """
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {'cart': cart}
    else:
        context = {'empty': True}
        template = 'shopping/detail.html'
    return render(request, template, context)
    

def update_cart(request, slug):
    """ 
    Looks for an already existing session,if it's there it grabs that id and uses that cart, 
    if nor available creates a new instance of the cart and queries the cart
    using the_id which is assigned the value of cart_id

    """
    request.session.set_expiry(200000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)

#Querries the products,add the respective product,calculates the total and removes a product from cart too

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    if not product in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)
    new_total = 0.00
    for item in cart.products.all():
        new_total += float(item.price)

    request.session['cart_item_total']=cart.products.count()    
    cart_total = new_total
    cart.save()

    return HttpResponseRedirect(reverse(cart))
    


    
    # for item in cart:
    #     item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    # return render(request, 'detail.html', {'cart': cart})
     

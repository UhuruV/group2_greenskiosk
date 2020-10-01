from django.shortcuts import render
from catalogue.models import Product


# Create your views here.

def upload_cart(request,product_id):
    products=Product.objects.filter(id=product_id)

    return render(request,'cart.html',{'products':products})

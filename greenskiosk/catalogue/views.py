from django.shortcuts import render,redirect
from .models import Product
from django.http import request
from .forms import ProductForm



# Create your views here.

def products_list(request):
    products = Product.objects.all()
    return render(request,'products_list.html',{'products':products})


def product_description(request,product_id):
    product = Product.objects.filter(id=product_id)
    return render(request,'product_description.html',{'product':product})

def upload_product(request):
    # form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('products_list')
    else:
        form = ProductForm()
   
    return render(request, 'upload_product.html', {'form': form})





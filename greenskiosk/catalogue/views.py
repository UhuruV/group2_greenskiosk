from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from django.http import request
from .forms import ProductForm
from shopping.forms import CartAddProductForm



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

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form':cart_product_form
    }
    return render(request, 'catalogue/product/product_description.html', context)
    





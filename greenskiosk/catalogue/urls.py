from django.urls import path
from . import views
from .views import products_list,product_description
from .views import upload_product


urlpatterns = [
    path('products/', products_list, name='products_list'),
    path("products/upload/", upload_product, name="product-uploads"),
    path('description/', product_description, name='product_description'),
    path('products/<int:product_id>/',product_description, name="id"),

]

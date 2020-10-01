from django.urls import path
from .views import upload_cart

urlpatterns = [
    path('cart/<int:product_id>/',upload_cart,name='upload_cart')
]

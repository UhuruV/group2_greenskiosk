from django.urls import path
from . import views
from .views import upload_kiosk

urlpatterns = [
    path('kiosk/upload/', upload_kiosk, name='upload_kiosk'),
]
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':"form-control"}),
            'category':forms.TextInput(attrs={'class':"form-control"}),
            'description':forms.Textarea(attrs={'class':"form-control"}),
            'suplier_price':forms.TextInput(attrs={'class': "form-control"}),
            'selling_price':forms.TextInput(attrs={'class': "form-control"}),
            'suplier':forms.Select(attrs={'class': "form-control"}),
            'kiosk':forms.TextInput(attrs={'class': "form-control"}),
            'number_in_stock':forms.TextInput(attrs={'class': "form-control"}),
            'image':forms.FileInput(attrs={'class': "form-control"})
        }

        
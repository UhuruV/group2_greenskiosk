from django.shortcuts import render,redirect
from .forms import KioskForm
from django.http import request

# Create your views here.
def upload_kiosk(request):
    if request.method == "POST":
        form=KioskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("product-uploads")

    else:
        form=KioskForm()

    return render(request, 'upload_kiosk.html', {'form': form})

    
    
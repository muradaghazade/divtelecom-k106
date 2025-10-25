from django.shortcuts import render
from core.models import *

def home(request):
    slider = Slider.objects.all()
    product = Product.objects.all()
    context = {
        'slider': slider,
        'product': product,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about-us.html')

def product(request):
    return render(request, 'product.html')


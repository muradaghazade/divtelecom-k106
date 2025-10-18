from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def product(request):
    return render(request, 'product.html')
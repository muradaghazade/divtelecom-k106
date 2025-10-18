from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
]
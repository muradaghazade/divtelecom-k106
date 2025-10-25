from django.contrib import admin
from core.models import *

admin.site.register([
    Product,Slider,Brand,Category,Image,Favorite_product,Cart,Order,Comment,

])

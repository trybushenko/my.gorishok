from django.contrib import admin

from .models import (Category, Product, Country,Image, ImageAssociation)
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Country)
admin.site.register(Image)
admin.site.register(ImageAssociation)
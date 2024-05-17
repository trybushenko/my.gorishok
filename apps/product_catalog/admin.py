from django.contrib import admin

from .models import (Category, Product, Country,Image, ImageAssociation, Discount)
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Discount)
admin.site.register(Product)
admin.site.register(Country)
admin.site.register(Image)
admin.site.register(ImageAssociation)
admin.site.register(Category, CategoryAdmin)
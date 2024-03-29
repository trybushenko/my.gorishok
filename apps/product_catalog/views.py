import random

from typing import Any
from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.utils.translation import gettext_lazy as _

from .models import Product, Category

class CategoryView(ListView):
    model = Category
    template_view = 'product_catalog/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()
    

class ProductView(ListView):
    model = Product
    template_name = 'product_catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self) -> QuerySet[Any]:
        category_slug = self.kwargs.get('category')

        category = Category.objects.get(slug=category_slug)
        return Product.objects.filter(category_id=category.id).order_by('name')
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        related_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)
        related_products = random.sample(list(related_products), 4)
        context['related_products'] = related_products
        return context

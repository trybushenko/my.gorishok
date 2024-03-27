from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.utils.translation import gettext_lazy as _

from .models import Product, Category

# Create your views here.

class CategoryView(ListView):
    model = Category
    template_view = 'product_catalog/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        _(Category.name)
        return Category.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        translated_categories = [(category.id, _(category.name)) for category in context['categories']]
        context['translated_categories'] = translated_categories
        return context
    

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
    
def home(request):
    return HttpResponse('Hello world! This is home of the product catalog!')

def catalog(request):
    return HttpResponse('Hello fellows! This is catalog!')
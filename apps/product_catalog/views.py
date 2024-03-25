from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.urls import reverse
from django.views.generic import DetailView

from .models import Product

# Create your views here.

class ProductView(ListView):
    model = Product
    template_name = 'product_catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.order_by('name')
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_catalog/product_detail.html'
    context_object_name = 'product'
    
def home(request):
    return HttpResponse('Hello world! This is home of the product catalog!')

def catalog(request):
    return HttpResponse('Hello fellows! This is catalog!')
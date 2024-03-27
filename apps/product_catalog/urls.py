from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import views

app_name = 'product_catalog'

urlpatterns = [
    path('', views.CategoryView.as_view(), name='category_list'),
    path('<slug:category>', views.ProductView.as_view(), name='product_list'),
    path('<slug:category>/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]
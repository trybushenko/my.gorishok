from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import views

app_name = 'product_catalog'

urlpatterns = [
    path('', views.ProductView.as_view(), name='products_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path

from . import views

app_name = 'product_catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog')
]
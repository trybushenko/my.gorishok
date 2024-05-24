"""
URL configuration for my_gorishok project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    # home page that redirects to product catalog
    path('', RedirectView.as_view(url='product_catalog/', permanent=True), name='home'),
    # product catalog that shows category list
    path('product_catalog/', include(('apps.product_catalog.urls', 'product_catalog'), namespace='product_catalog')),
    # endpoint that is responsible for user management
    path('accounts/', include('allauth.urls')),
    path('user/', include(('apps.user_management.urls', 'user_management'), namespace='user_management')),
    path('cart/', include(('apps.cart.urls', 'cart'), namespace='cart')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

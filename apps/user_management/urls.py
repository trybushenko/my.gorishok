from django.urls import path

from .views import account_profile, continue_as_guest

app_name = 'user_management'

urlpatterns = [
    path('profile/', account_profile, name='account_profile'),
    path('continue_as_guest/', continue_as_guest, name='continue_as_guest'),
    # Add other URLs as needed
]
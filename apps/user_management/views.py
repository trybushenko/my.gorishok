from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.http import JsonResponse

from .utils import create_guest_user

# Create your views here.

def account_profile(request):
    return render(request, 'user_management/account_profile.html')

def continue_as_guest(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        guest_user = create_guest_user()
        guest_user.backend = 'allauth.account.auth_backends.AuthenticationBackend'

        login(request, guest_user)
        return JsonResponse({'redirect_url': '/cart/'})
    else:
        guest_user = create_guest_user()
        guest_user.backend = 'allauth.account.auth_backends.AuthenticationBackend'

        login(request, guest_user)
        return redirect('cart:cart')
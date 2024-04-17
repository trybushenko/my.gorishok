from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class AppUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password')

class AppUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password')
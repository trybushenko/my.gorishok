from django import forms as d_forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from allauth.account.forms import SignupForm

class AppUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password')

class AppUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password')

class CustomSignupForm(SignupForm):
    first_name = d_forms.CharField(max_length=30, required=True, label="First Name")
    last_name = d_forms.CharField(max_length=30, required=True, label="Last Name")

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    
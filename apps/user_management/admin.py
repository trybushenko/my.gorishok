from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AppUserChangeForm, AppUserCreationForm

User = get_user_model()

class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = User
    # Define which fields are displayed in the user change form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    # Define which fields are used in the user creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    # Define which fields are displayed in the user list
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_superuser')
    # Define which fields can be used to search for users in the admin interface
    search_fields = ('email', 'first_name', 'last_name')
    # Define how users are ordered in the admin interface
    ordering = ('email', )
    
    list_filter = ('is_active', 'is_superuser',)  # Update this line

# Register your models here.
admin.site.register(User, AppUserAdmin)
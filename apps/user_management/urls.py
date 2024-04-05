from django.urls import path
from .views import CreateUser, UpdateUser, DeleteUser, user_list

urlpatterns = [
    path('', CreateUser.as_view(), name='user_create'),
    path('<int:pk>/', UpdateUser.as_view(), name='user_update'),
    path('<int:pk>/delete', DeleteUser.as_view(), name='user_delete'),
    path('users/', user_list, name='user_list'),
    # Add other URLs as needed
]
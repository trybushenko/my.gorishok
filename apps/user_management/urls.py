from django.urls import path
from .views import CreateUser, UpdateUser, DeleteUser, user_list

urlpatterns = [
    path('create-user/', CreateUser.as_view(), name='create_user'),
    path('update-user/<int:pk>/', UpdateUser.as_view(), name='update_user'),
    path('delete-user/<int:pk>/', DeleteUser.as_view(), name='delete_user'),
    path('user-list/', user_list, name='user_list'),
    # Add other URLs as needed
]
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User

# Create your views here.
class CreateUser(LoginRequiredMixin, CreateView):
    model = User
    fields = ('email', 'first_name', 'last_name', 'password')
    template_name = 'create_user.html'
    success_url = reverse_lazy('user:user_list')

class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('email', 'first_name', 'last_name', 'password')
    template_name = 'update_user.html'
    success_url = reverse_lazy('user:user_list')

class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('user:user_list')


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users' : users})

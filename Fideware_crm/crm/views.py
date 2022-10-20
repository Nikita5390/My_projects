from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView,
)
from django.urls import reverse
from .forms import UserForm
from .models import User
from django.shortcuts import render
from datetime import datetime, timedelta
import requests
from .serializer import UserSerializer




class UserCreateView(CreateView):
    template_name: str = "crm/user_add.html"
    form_class: type = UserForm

    def get_success_url(self):
        return reverse('user-list')


class UserListView(ListView):
    template_name: str = "crm/user_list.html"
    model: type = User

    def get_queryset(self):
        status = self.request.GET.get("status")
        step = self.request.GET.get("step")
        next_contact = self.request.GET.get("next_contact")
        result = User.objects.all()
        pk = 0
        if status:
            result = User.objects.filter(status=status)
        if step:
            result = User.objects.filter(step=step)
        return result


class UserDetailView(DetailView):
    template_name: str = "crm/user_detail.html"
    model: type = User


class UserDeleteView(DeleteView):
    template_name: str = "crm/user_delete.html"
    model: type = User
    success_url: str = "#"

    def get_success_url(self):
        return reverse('user-list')


class UserUpdateView(UpdateView):
    # data = User.objects.all()
    # def post(self, request, *args, **kwargs):
    #     serializer = User.objects.all()
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    template_name: str = "crm/user_update.html"
    form_class: type = UserForm
    model = User

    def get_success_url(self):
        return reverse('user-list')


def users_date_filter(request, pk):
    users = User.objects.all()
    if pk == 1:
        now = datetime.now()
        users = User.objects.filter(next_contact=now.date())
    if pk == 2:
        now = datetime.now() + timedelta(days=1)
        users = User.objects.filter(next_contact=now.date())
    if pk == 3:
        now = datetime.now() - timedelta(days=1)
        users = User.objects.filter(next_contact__lte=now.date())
    if pk == 4:
        now = datetime.now()
        users = User.objects.filter(next_contact__lte=now.date())
    print(users)
    return render(request, "crm/user_list.html", {"object_list": users})

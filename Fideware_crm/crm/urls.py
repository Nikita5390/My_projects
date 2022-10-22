from django.urls import path
from .views import UserCreateView, UserListView, UserDetailView, UserDeleteView, \
    UserUpdateView, users_date_filter

urlpatterns = [
    path("add/", view=UserCreateView.as_view(), name="user-add"),
    path("list/", view=UserListView.as_view(), name="user-list"),
    path("<str:pk>/", view=UserDetailView.as_view(), name="user-detail"),
    path("<str:pk>/delete", view=UserDeleteView.as_view(), name="user-delete"),
    path("<str:pk>/update", view=UserUpdateView.as_view(), name="user-update"),
    path("filter/<int:pk>", view=users_date_filter, name="users_date_filter"),

]

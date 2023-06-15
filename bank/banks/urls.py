from django.contrib import admin
from django.urls import path
from banks import views

urlpatterns = [
    path('', views.index),
]

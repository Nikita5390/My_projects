from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrReadOnly
from .models import User, Transaction, Category
from .serializers import UserSerializer, TransactionSerializer, CategorySerializer
from .filters import TransactionFilter, CategoryFilter
from rest_framework.filters import OrderingFilter


class UserCreateListApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [TransactionFilter, OrderingFilter]
    filter_fields = ['count', 'date', 'organization']
    ordering_fields = ['count', 'date', 'organization']

    def get_permissions(self):
        if self.action == 'destroy' or self.action == 'create' or self.action == 'update':
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [CategoryFilter, OrderingFilter]
    filter_fields = ['title']
    ordering_fields = ['title']

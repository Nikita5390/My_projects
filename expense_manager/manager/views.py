from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import User, Transaction
from .serializers import UserSerializer, TransactionSerializer
from .filters import TransactionFilter


class UserCreateListApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = TransactionFilter

    ordering_fields = ['count', 'date']

    def get_queryset(self):
        count = self.request.query_params.get("count")
        queryset = self.queryset.all()
        if count:
            queryset = self.queryset.filter(count=count)
        return queryset

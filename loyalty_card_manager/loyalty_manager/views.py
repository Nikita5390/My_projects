from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Card, Order, Product
from .serializers import CardSerializer, OrderSerializer, ProductSerializer
import random
import string
from rest_framework.response import Response


def card_generator():
    card_series = list(string.ascii_uppercase)
    card_number = list(range(1, 100))
    random_series = random.choice(card_series)
    random_number = random.choice(card_number)
    random_card = [random_series, random_number]
    return random_card


class CardViewSet(viewsets.ModelViewSet):
    search_fields = ["series_card", "number_card", "release_date", "last_use_date", "status"]
    filter_backends = (filters.SearchFilter,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request, *args, **kwargs):
        card = card_generator()
        series_card = card[0]
        number_card = card[1]
        new_card = Card.objects.create(
            series_card=series_card,
            number_card=number_card
        )
        return Response(status=200)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

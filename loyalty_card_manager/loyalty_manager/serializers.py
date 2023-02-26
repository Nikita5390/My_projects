from rest_framework import serializers
from .models import *


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("series_card", "number_card", "release_date", "last_use_date", "status", "total_order", "total_price")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("order_id", "total_price", "date", "discount", "discount_calc")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("product_order", "name", "price", "price_discount")

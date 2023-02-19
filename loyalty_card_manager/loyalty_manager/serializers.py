from rest_framework import serializers
from .models import *


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("series_card", "number_card", "release_date", "last_use_date", "status", "total_order", "total_price")


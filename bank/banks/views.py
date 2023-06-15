from django.shortcuts import render
from .models import *


def index(request):
    manufacturers = Manufacturer.objects.all().select_related('product')
    for manufacturer in manufacturers:
        print(manufacturer.product.credit_request.contract.id)

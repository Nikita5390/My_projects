from django.contrib import admin
from .models import Manufacturer, Contract, CreditRequest, Product


admin.site.register(Manufacturer)
admin.site.register(Contract)
admin.site.register(CreditRequest)
admin.site.register(Product)
# Register your models here.

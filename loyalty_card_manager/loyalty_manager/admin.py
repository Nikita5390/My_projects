from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DiscountGuide)
admin.site.register(Card)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductInOrder)
admin.site.register(OrderInCard)
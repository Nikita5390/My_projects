from django.db import models
from enum import Enum
from django.db.models.signals import post_save


class StatusCard(Enum):
    active = "Активирована"
    no_active = "Не активирована"
    overdue = "Просрочена"

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class DiscountGuide(models.Model):
    class Meta:
        db_table = "discount_guides"

    discount_name = models.CharField(max_length=100)
    discount_percent = models.FloatField()

    def __str__(self):
        return self.discount_name


class Card(models.Model):
    class Meta:
        db_table = "cards"

    card_id = models.AutoField(primary_key=True)
    total_order = models.IntegerField(default=0)
    series_card = models.CharField(max_length=50, unique=True)
    number_card = models.IntegerField(unique=True)

    release_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    expiration_date = models.DateTimeField()
    last_use_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    total_price = models.FloatField(null=True, default=0)
    status = models.CharField(max_length=50, choices=StatusCard.choices(), default=StatusCard.no_active)

    def __str__(self):
        return f"series: {self.series_card}, number: {self.number_card}, " \
               f"release: {self.release_date}, exp: {self.expiration_date}," \
               f" status: {self.status}, orders: {self.total_order}, total: {self.total_price}$"


class Product(models.Model):
    class Meta:
        db_table = "products"

    product_order = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    price_discount = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        db_table = "orders"

    order_id = models.AutoField(primary_key=True)
    total_price = models.FloatField(default=0)  # total amount all products in order
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    discount = models.FloatField(null=True, default=0)
    discount_calc = models.FloatField(null=True, default=0)

    def __str__(self):
        return f"Заказ № {self.order_id}"

    def save(self, *args, **kwargs):
        pass
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    class Meta:
        db_table = "products_in_order"

    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    price_per_item = models.FloatField(default=0)
    total_price = models.FloatField(default=0)  # price * number
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Товар: {self.product.name} {self.number} шт, № заказа {self.order.order_id}. Итого: {self.total_price}$"

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.number * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class OrderInCard(models.Model):
    class Meta:
        db_table = "orders_in_card"

    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, blank=True, null=True, default=None, on_delete=models.CASCADE)
    total_order = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Заказ: {self.order.order_id}"


def order_in_card_post_save(sender, instance, created, **kwargs):
    card = instance.card
    all_order_in_card = OrderInCard.objects.filter(card=card)
    card_total_order = len(all_order_in_card)
    order = instance.order
    all_price_in_card = OrderInCard.objects.filter(order=order)
    card_total_price = card.total_price
    for item in all_price_in_card:
        card_total_price += item.order.total_price

    instance.card.total_order = card_total_order
    instance.card.save(force_update=True)


post_save.connect(order_in_card_post_save, sender=OrderInCard)

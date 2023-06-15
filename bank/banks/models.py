from django.db import models


class Contract(models.Model):
    class Meta:
        db_table = "contracts"

    number_contract = models.CharField(max_length=50, null=False)
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number_contract


class CreditRequest(models.Model):
    class Meta:
        db_table = "credit_requests"

    name = models.CharField(max_length=50, null=False)
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='credit_request')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        db_table = "products"

    product_name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    credit_request = models.ForeignKey(CreditRequest, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name


class Manufacturer(models.Model):
    class Meta:
        db_table = "manufacturer"

    manufacturer_name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='manufacturer')

    def __str__(self):
        return self.manufacturer_name

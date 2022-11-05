from django.db import models


class User(models.Model):
    class Meta:
        db_table = "users"

    name = models.CharField(max_length=50, null=False)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    class Meta:
        db_table = "transactions"

    id = models.AutoField(primary_key=True)
    count = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    organization = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=150)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.organization


class Category(models.Model):
    class Meta:
        db_table = "categories"

    title = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products_images')
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        db_table = 'product'


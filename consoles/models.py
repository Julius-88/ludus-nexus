from django.db import models
from django.conf import settings


class Console(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.username

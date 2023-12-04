import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from consoles.models import Product


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    newsletter_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, null=True, blank=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=500)
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def _generate_order_number(self):
        """ Generate a random, unique order number using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """Update grand total each time a line item is added"""
        self.total_price = self.orderdetails_aggregate(
            Sum('orderdetail_total'))['orderdetail_total_sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """Override the original save method to set the order number if it has
         not been set already"""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='orderdetails')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    orderdetail_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """Calculate orderdetail_total before saving"""
        self.orderdetail_total = self.product.price * self.quantity
        super(OrderDetail, self).save(*args, **kwargs)

    def __str__(self):
        return self.order.order_number

from django.db import models
from products.enums import InstallmentOption, ShippingType

class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    default_price = models.DecimalField(max_digits=10, decimal_places=2)  # product price without discount
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=None)
    installment_option = models.CharField(max_length=4, choices=InstallmentOption.choices, blank=True, null=True, default=None)
    shipping_type = models.CharField(max_length=6, choices=ShippingType.choices)
    free_shipping = models.BooleanField(default=False)
    link = models.URLField()

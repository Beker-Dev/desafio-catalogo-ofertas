from django.db import models


class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    default_price = models.DecimalField(max_digits=10, decimal_places=2)  # product price without discount
    link = models.URLField()
    
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)
    # installment_option = 
    shipping_type = models.enums.Choices(
        ('full', 'Full'),
        ('normal', 'Normal')
    )
    free_shipping = models.BooleanField(default=False)
    
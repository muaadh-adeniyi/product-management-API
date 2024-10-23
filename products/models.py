from django.db import models
import uuid

class Product(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('NGN', 'Nigerian Naira'),  # Add more currencies as needed
    ]

    id = models.UUIDField( primary_key=True , default= uuid.uuid4 ,editable=False )
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='NGN')

    def __str__(self):
        return self.name


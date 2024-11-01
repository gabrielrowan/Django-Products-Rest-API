from django.db import models
from datetime import date

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    sale_applied = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sale_expiry_date = models.DateField(blank=True, null=True, default=date.today)
    
    def __str__(self):
        return self.name

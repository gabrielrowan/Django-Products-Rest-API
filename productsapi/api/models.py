from django.db import models
from datetime import date

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    # Auto_now_add automatically sets the datetime field value to now when first created
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    sale_applied = models.BooleanField(default=False)
    # blank = True allows field to be left blank when object is created
    # null = True means empty values will be stored as null in the db
    sale_price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    sale_expiry_date = models.DateField(blank=True, null=True, default=date.today)
    
    # Defines the string representation of an instance of a model
    # In this instance, the string representation is set to the name field of the model
    def __str__(self):
        return self.name

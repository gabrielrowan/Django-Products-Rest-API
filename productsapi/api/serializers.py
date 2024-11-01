from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "created_date", "price", "sale_applied", "sale_price", "sale_expiry_date"]
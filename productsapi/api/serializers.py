from rest_framework import serializers
from .models import Product

# Serializers are able to transform data, such as model instances, to JSON so that it can be rendered on the frontend
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "created_date", "price", "sale_applied", "sale_price", "sale_expiry_date"]
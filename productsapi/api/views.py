from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Using the rest framework means having access to pre=build views for commonly used patterns

# ListCreateAPIView provides get and post method handlers 
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Custom method to delete all product objects
    def delete(self, request, *args, **kwargs):
          Product.objects.all().delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

# Provides get, put and delete method handlers
class ProductPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        # 'pk' stands for 'primary key'
        lookup_field = "pk"


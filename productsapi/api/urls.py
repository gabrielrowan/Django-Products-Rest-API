from django.urls import path
from . import views 

urlpatterns = [
    path("products/", views.ProductListCreate.as_view(), name="product-view-create"),
    path("products/<int:pk>/", views.ProductPostRetrieveUpdateDestroyView.as_view(), name="update")
]
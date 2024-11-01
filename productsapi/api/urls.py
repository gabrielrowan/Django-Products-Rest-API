from django.urls import path
from . import views 

# Contains a mapping between URL patterns and Python callback functions in the form of views

urlpatterns = [
    ''' 
    Url for:
        - Viewing all products
        - Creating a product 
        - Deleting all products
    '''
    path("products/", views.ProductListCreate.as_view(), name="viewall-create-deleteall"),
    
    ''' 
    Url for:
        - Fetting data for a given product based on the primary key
        - Updating a product 
        - Deleting a product
    '''
    path("products/<int:pk>/", views.ProductPostRetrieveUpdateDestroyView.as_view(), name="get-update-delete")
]
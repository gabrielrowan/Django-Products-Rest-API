# Products API 

### Made With 

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Overview

This is an API made using Django and the REST framework. 

It implements the CRUD operations (Create, Read, Update, Delete) to allow you to do the following: 

- Create a product
- Update a product
- List all products
- View an individual product
- Delete a product
- Delete all products

### Products

Each product has the following characteristics: 
- Name
- Description (optional)
- Price
- Sale Applied (whether there is a discout that currently applies to that item)
- Sale Price (optional)
- Sale Price Expiry Date (optional)

### Urls
This project has 2 URL patterns:

1) `/Products/` - Here you can view all products, delete all products or add a new product
2) `/Products/id` - Here you can view, update or delete an individual product


### Future additions  :rocket:

- In the future, I would like to add an enum field for `PriceType` to the `Product` model, so that you can specify whether the price type is `Per Item` or `Per Weight`.
- For example, there are some products where you pay per item (ie. washing up liquid) and some products where you pay per weight (ie. potatoes) :potato:
   


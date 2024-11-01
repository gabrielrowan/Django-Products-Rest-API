# Products API 

### Made With 

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Overview

This is an API made using Django and the REST framework. It is also my first Django project :smiley:

It implements the CRUD operations (Create, Read, Update, Delete) to allow you to do the following: 

- Create a product
- Update a product
- List all products
- View an individual product
- Delete a product
- Delete all products

### Demo

https://github.com/user-attachments/assets/db7e134d-7a00-4e94-ba2a-f66d3c9cb365

0.00 - Overview of the code
1.54 - Demo of listing and creating products
3.53 - Deleting and editing a product 

### Products

Each product has the following characteristics: 
- Name
- Description
- Price
- Sale Applied (whether there is a discout that currently applies to that item)
- Sale Price (optional)
- Sale Price Expiry Date (optional)

### Urls
This project has 2 URL patterns:

1) `/Products/` - Here you can view all products, delete all products or add a new product
2) `/Products/id` - Here you can view, update or delete an individual product

### Training Wheels :bike:

As this is my first Django project, I have included comments in the code that have helped me to become more familiar with the different aspects of the framework

### Learning Points :ledger:

No project is build without making mistakes and learning from them. Here are some mistakes which I learnt from: 
- Adding a new field to the model without also adding this item to the list of fields in the `ProductSerializer` class
- Getting the following error after renaming a field: `It is impossible to add a non-nullable field to feature without specifying a default.`
The solution was to follow the steps in the command line to specify a temporary value for the field I had renamed, so that it could be used for pre-existing model objects

### Future additions  :rocket:

- In the future, I would like to add an enum field for `PriceType` to the `Product` model, so that you can specify whether the price type is `Per Item` or `Per Weight`.
- For example, there are some products where you pay per item (ie. washing up liquid) and some products where you pay per weight (ie. potatoes).
   


 1st question:  
 The "product" and "product_category" entities appear to have a one-to-many relationship based on the information provided.

The "category in" attribute in the "product inventory" entity indicates the product category each product (identified by its unique ID) falls within. This suggests that a product or group of products may include more than one item.
As a result, the relationship fits the following description:

Every product is a member of a single product category.
There can be more than one product in a given product category.
Foreign key constraints are commonly used in database schemas to describe this relationship. A foreign key column referencing the primary key of the "product_category" table is likely to be present in the "product" table.

2nd question:
We can use a foreign key constraint to make sure that every product in the "Product" database has a valid category allocated to it.
The table is named "Product".
The primary key field in the "Product_Category" database is referenced by the foreign key column "category_id" in the "Product" table.
The table that has the categories in it is called "Product_Category".
Within the "Product_Category" table, the primary key column is "id".
You can make sure that every product in the "Product" database has a proper category allocated to it—specified by the "category_id" column—by adding this foreign key constraint.

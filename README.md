# Petco chain store management system

**COMS4111 Project 1 Part 3**

![screenshot](static/photo/product_photos/logo.png)

This part of project is contributed by:
+ Mengjie Zhang (mz2840) mz2840@columbia.edu
+ Chang Lu (cl4150) cl4150@columbia.edu

**Project summary**:

We are proposing an entity-relationship model for the Petco chain store management system. 
Petco chain store is an industry-leading health and wellness company focused on improving the lives of pets. 
Petco operates more than 20 Petco stores in New York City which offer a wide range of pets’ products.
This ER-model contains basically the whole procedure of how the Petco stores run. 
We take entities such as customer, payment, insurance, pet, product, employee, manager, shop, and supplier.

+ The PostgreSQL account is: mz2840
+ The URL of the web application is: (http://35.229.113.142:8111/)

**Implementation of the proposal**: 

Customer is able to:
+ View insurance and product information
+ View shop information

Employee is able to:
+ Query insurance and product information
+ Query shift information
+ Query shop directory
+ Record payment information

Manager is able to:
+ View employee information
+ View payment information
+ Query shop directory
+ View supplier list

Supplier is able to:
+ View shop product list

As for the Admin part mentioned in Part 1 proposal, we moved the Record payment information to Employee, the Query shop directory to Employee and Manager, the Query supply list to Manager.
We did not implement On-Board/De-Board Employees and On-Board/De-Board Managers function, because that requires to change the SQL schema (add ON DELETION option).

**Description of two web pages**
+ Type in shop address to search for the shop information as well as the product it serves. This requires the join of three tables(prodect, product_sold, shop).
+ Insert the information in three tables: customer, payment, customer_buy in database by a single page. Because the same customer will go to the store many times to buy different products, which will lead to the same customer information, but different products or payment information they purchased. Therefore, it is necessary to first determine whether the customer's information has been recorded before, if so, skip recording customer information directly, and record payment and customer_buy information. In this case, employees can efficiently process customer and payment information.

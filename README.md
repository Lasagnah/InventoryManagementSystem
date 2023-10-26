# Inventory Management System
## Introduction
In this project, I will be designing an Inventory Management System for a retail store. It will be done using the commandline, and will be able to model a store's transactions and generate reports as well. 
## Implemented Functionalities
### Found in IMS.py
This is where most, if not all of the Inventory Management actually goes down. We have 3 classes (Product, Inventory, Transaction), each building off of each other. 
* Product class, which represents each individual item. Has a unique ID associated, as well as a Name, Price, Category, and Count (in stock) as fields.
    * Has an update method, to update the fields of the given item. 
    * Has methods to get the price and count of an item.
* Inventory class, which represents a set of all of the products in a store. 
    * Has methods to get the price, name, category, count, and ID of a given item, as well as a method to find an item given its name. 
    * Has methods to add and remove items from the inventory.
    * Has a method to help with the selling of an item.
    * Has a method to update an item, which calls the update method in the Product class.
* Transaction Class, which represents a list of all of the transactions.
    * Has methods to generate reports, based off of amount of items sold, total revenue for each item, and the total stock of each item.
    * Has a method to sell an item and add to the transaction list.
### Found in main.py
This is where the commandline interface implementation is found. 
It mainly consists of a While loop, which takes input, and then determines what to do based off of the input given. 
## Test cases
### Found in testcases.py

## Discussion

## Conclusion

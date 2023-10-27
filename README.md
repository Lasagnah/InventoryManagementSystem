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
Test Cases were ommitted for get methods, as well as the command line interface integration.
* Test Case 1: Creates an inventory, adds an item to the inventory, then checks to see if the item created is the same as the item in the inventory.
* Test Case 2: Tests updating a product's information, asserts that the product's information is the new information.
* Test Case 3: First tests the sell method, asserts that the amount of product changed, then prints out all of the different product reports.
## Discussion
As for the complexity of this system, its on the pretty low side. I essentially used a database-type design, where I first created a piece of data, being the Product class, which then we created our database class, the Inventory class. The Inventory class will contain all of our Products, so it has to be able to work with it together. The Transaction class is sort of an offshoot of the inventory class, but it is being used in a way that it doesn't really need to be initialized, so it keeps a track of all transactions. 
## Conclusion
This implementation is pretty simple and doesn't really need all that much effort to use this in an actual store situation. The only things that would need to be changed are the reports formatting for readability/accessibility, as well as potentially multiple lists of transactions (one for each register and a master list), and potentially a GUI/more robust main.py file for accessibility and ease of use.  
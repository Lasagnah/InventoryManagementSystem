from IMS import *
import re
i = Inventory()
while True:
    s = input("Type 'A' to add item, 'S' to sell an item, 'R' to generate reports, or 'Exit' to exit")
    if s == "Exit" or None:
        # Exit condition
        break
    elif s == "A":
        # Add item code
        s = input("Input the item's name, amount, price, and category (in that order, each followed by a comma)")
        #Regex manipulation to get name, amount, price, and category
        
    elif s == "S":
        # Sell item code
        s = input("What is the item you are trying to sell?")
        item = i.getProd(s)
        s = input("How many would you like to sell?")
        
        Transaction.sellItem(item, s)

    elif s == "R":
        # gen report code
        s = input("What kind of report would you like to generate? 'S' for sales, 'R' for revenue, or 'T' for Stock")
        if s =="S":
            #Stock report
            print(Transaction.getStockReport(i))
        if s == "R":
            #Revenue report
            print(Transaction.getRevReport())
        if s == "T":
            print(Transaction.getStockReport())
    else:
        print("Sorry the code you input was incorrect, try again")
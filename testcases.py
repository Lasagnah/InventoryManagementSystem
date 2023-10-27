from IMS import * 

def test1():
    #This will test creating an inventory and adding an item
    #This will also test the get product method
    i = Inventory()
    p = Product("prod1", 3, 2.50, "oranges")
    i.addItem(p)
    assert i.getProd("prod1") == p
    return True

def test2():
    #This will test the update method and the get product method
    i = Inventory()
    p = Product("prod1", 3, 2.50, "oranges")
    i.addItem(p)
    i.updateProduct(p, "prod 1", 4, 5.0, "Apples")
    assert i.getProd("prod 1") == Product("prod 1", 4, 5.0, "Apples")
    
def test3():
    #This will test selling items and generating reports for selling items
    i = Inventory()
    p = Product("prod1", 3, 2.50, "oranges")
    i.addItem(p)
    assert p.getCount == 1 
    #Print out the reports
    Transaction.getSalesReport()
    Transaction.getRevReport()
    Transaction.getStockReport(i)



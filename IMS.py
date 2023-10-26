class Product:
    numOfProducts = 0
    def __init__(self, name = "unspecified", inStock = 0, price = 0.0, category = "unspecified"):
        self.name = name
        self.inStock = inStock
        self.price = price
        self.category = category
        self.productID = Product.numOfProducts
        Product.numOfProducts += 1

    def update(self, name, inStock, price, category):
        if name is not None:
            self.name = name
        if inStock is not None:
            self.inStock = inStock
        if price is not None:
            self.price = price
        if category is not None:
            self.category = category

    def sellItem(self, product, amt):
        if amt > self.inStock:
            return "error, not enough product"
        self.inStock -= amt 
        return

    def getPrice(self):
        return self.price
    
    def getCount(self):
        return self.inStock

class Inventory:
    def __init__(self):
        self.inventory = {}
    
    def addItem(self, product):
        self.inventory.add(product)

    def removeItem(self, product):
        self.inventory.remove(product)

    def sellItem(self, product, amt):
        if amt > self.getProdCount(self,product):
            return "error, not enough product"
        self.inventory(product).inStock -= amt 
        return

    def updateStock(self, product, num):
        self.inventory(product).inStock = num

    def getProdPrice(self, product):
        return self.inventory(product).price
    
    def getProdName(self, product):
        return self.inventory(product).name
    
    def getProdID(self, product):
        return self.inventory(product).productID
    
    def getProdCount(self, product):
        return self.inventory(product).inStock
    
    def getCategory(self, product):
        return self.inventory(product).category

    def getProd(self, name):
        for p in self.inventory:
            if p.name == name:
                return p
        return "error, no product with given name found."
    
    def updateProduct(self, product, name, inStock, price, category):
        self.inventory(product).update(name, inStock, price, category)
    
class Transaction:
    transactions = []

    def sellItem(self, item, amt):
        #This function will check to see if we have enough items to sell
        #Then will add the transaction to the transaction list
        if amt > item.getCount():
            return False
        else:
            Transaction.transactions.append((item, amt))
            item.sellItem(amt)
            return True

    def getSalesReport(self):
        #This function will return a dictionary of all of the items sold and the amount sold
        #Returns a dictionary with the format {item:amount sold}
        t_arr = []
        i_arr = []
        for t in Transaction.transactions:
            #loop through all transactions
            if t[0] in i_arr:
            #If we already encountered the item sold, add the amount sold to a running tally
                t_arr[i_arr.index(t[0])]+=t[1]
            else:
            #Else, add it to a list of encountered items, add the amount to a running tally
                i_arr.append(t[0])
                t_arr.append(t[1])
        d = dict(zip(i_arr, t_arr))
        return d 

    def getStockReport(self, inventory):
        #This function will return a dictionary of all of the items and the amount in stock
        #Returns a dictionary with the format {item:amount in stock}
        t_arr = []
        i_arr = []
        for item in inventory.inventory:
            i_arr.append(item)
            t_arr.append(inventory.getProdCount(item))
        d = dict(zip(i_arr, t_arr))
        return d 
    
    def getRevReport(self):
        #This function will return a dictionary of all of the items sold and the profit/revenue
        #Returns a dictionary with the format {item:revenue}
        t_arr = []
        i_arr = []
        for t in Transaction.transactions:
            #loop through all transactions
            if t[0] in i_arr:
            #If we already encountered the item sold, add the revenue to a running tally
                t_arr[i_arr.index(t[0])]+=t[1] * t[0].getPrice()
            else:
            #Else, add it to a list of encountered items, add the revenue to a running tally
                i_arr.append(t[0])
                t_arr.append(t[1] * t[0].getPrice())
        d = dict(zip(i_arr, t_arr))
        return d 
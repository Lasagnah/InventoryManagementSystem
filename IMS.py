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
    def __init__(self, items):
        Transaction.transactions.add(items)


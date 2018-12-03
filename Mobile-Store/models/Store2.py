import sqlite3
from models.Item import Item 


conn = sqlite3.connect('inventory.db')
c = conn.cursor()

class StoreTwo:
    def __init__(self):
        self.storeItems = []
        self.itemPrices = []
        c.execute('SELECT name, price FROM Inventory') 
        self.storeItems = c.fetchall()
        for name, price in self.storeItems:
            self.itemPrices.append(Item(name,price))
    
    def getItemPrices(self):
        return self.itemPrices


    
    

            


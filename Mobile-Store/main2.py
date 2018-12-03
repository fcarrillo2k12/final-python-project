import tkinter as tk
from tkinter.font import Font
from tkinter import *  
from tkinter import messagebox
from models.Store2 import StoreTwo
from  models.ShoppingCart import ShoppingCart

def viewStore():
    global storeWindow 
    storeLabelFrame = LabelFrame(storeWindow, text="Store Items")
    storeLabelFrame.pack(fill="both", expand="yes", padx="20", pady="10")

    storeItemsFrame = Frame(storeLabelFrame)
    storeItemsFrame.pack(padx="10", pady="5")
    storeTwo = StoreTwo()
    itemPrices = storeTwo.getItemPrices()
    for item in itemPrices:
        counter = 0
        itemFrame = Frame(storeItemsFrame,  pady="5")
        itemFrame.pack(fill="both", expand="yes")

        nameLabel = Label(itemFrame, text=item.name,font=("Times New Roman",15),fg="blue")
        priceLabel = Label(itemFrame, text="$ %s"%item.price , font=("Times New Roman",13),fg="red")  
        addToCartBtn = Button(itemFrame, text="Add To Cart",cursor="hand2", command=lambda i=item: addItemToCart(i) ) 
        btnImage=PhotoImage(file="icons/shopp.png")       
        addToCartBtn.image= btnImage
        addToCartBtn.config(image=btnImage,width="51",height="51")

        nameLabel.pack(side="left")
        priceLabel.pack(side="left",fill="both", expand="yes" )
        addToCartBtn.pack(side="right" )
        counter+1

    btnGoCart = Button(storeWindow, text="Your Cart", font=("Times New Roman",15,"bold"),fg="green",bg="white",cursor="hand2", command=viewCart )
    btnGoCart.pack(pady="6")

def viewCart():   
    cartWindow = Toplevel()
    cartWindow.title("Your Cart")
    cartWindow.grab_set()
    global cart
    cartItems = cart.getCartItems()

    cartItemsLabelFrame = LabelFrame(cartWindow,text="Items in Cart")
    cartItemsLabelFrame.pack(fill="both", expand="yes", padx="20", pady="10")

    cartItemsFrame = Frame(cartItemsLabelFrame, padx=3, pady=3)
    cartItemsFrame.pack()
    index = 0
    for item in cartItems:
        itemFrame = Frame(cartItemsFrame,  pady="5")
        itemFrame.pack(fill="both", expand="yes")

        nameLabel = Label(itemFrame, text=item.name,font=("Times New Roman",15),fg="blue")
        priceLabel = Label(itemFrame, text="$ %s"%item.price,font=("Times New Roman",13),fg="red")  
        addToCartBtn = Button(itemFrame, text="Remove From Cart", font=("Times New Roman",11,"bold"),fg="green",bg="white",cursor="hand2", command=lambda i=index: removeFromCart(i,cartWindow) )

        nameLabel.pack(side="left")
        priceLabel.pack(side="left")
        addToCartBtn.pack(side="right" )
        index += 1

    checkOutFrame = Frame(cartWindow, pady="10")
    totalPriceLabel = Label(checkOutFrame, text="Total Price : $ %s" % cart.getTotalPrice(), font=("Times New Roman",14,"bold"),fg="indigo")
    totalPriceLabel.pack(side="left")
    buyBtn = Button(checkOutFrame, text="Buy Now", font=("Times New Roman",15,"bold"),fg="indigo",bg="white",cursor="hand2", command=lambda : buyCommand(cartWindow))
    buyBtn.pack(side="left",padx="10")
    checkOutFrame.pack()

    backToStoreBtn = Button(cartWindow, text="Back To Store", font=("TImes New Roman",15,"bold"),fg="green",bg="white",cursor="hand2",command=cartWindow.destroy)
    backToStoreBtn.pack(pady="6")

    cartWindow.mainloop()

def addItemToCart(item=None):
    global cart
    cart.addToCart(item)
    messagebox.showinfo(title="Action Successful" , message="%s Has Been Added To The Cart"%item.name )

def removeFromCart(itemIndex=None,cartWindow=None):
    global cart
    cart.removeFromCart(itemIndex)
    messagebox.showinfo(title="Action Successful",message="Item Has Been Removed From The Cart")
    cartWindow.destroy()
    viewCart()
def buyCommand(cartWindow):
    global cart
    cart.emptyCart()
    cartWindow.destroy()    
    messagebox.showinfo(title="Action Successful",message="Purchase Completed Successfully")

storeWindow = tk.Tk()
storeWindow.title("Mobile Accessories Store")
viewStore()

cart = ShoppingCart() 

storeWindow.mainloop()
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime

conn = sqlite3.connect("D:\Final project\Database\stock.db")
c = conn.cursor()


#date
date = datetime.datetime.now().date()
class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        #frames
        self.left = Frame(master, width=400, height=600, bg= 'white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=600, height=600, bg='lightgreen')
        self.right.pack(side=RIGHT)

        #components
        self.heading = Label(self.left, text='Cashier', font=('arial 18 bold'), bg='green', fg='white')
        self.heading.place(x=10,y=0)

        self.date_1 = Label(self.right, text="Today's Date: " + str(date), font=('arial 18 bold'),bg='lightgreen', fg='white')
        self.date_1.place(x=0,y=0)

        #table invoice
        self.tproduct = Label(self.right, text='Products', font=('arial 18 bold'), bg='lightgreen', fg='white')
        self.tproduct.place(x=0,y=40)

        self.tproduct = Label(self.right, text='Quantity', font=('arial 18 bold'), bg='lightgreen', fg='white')
        self.tproduct.place(x=225,y=40)

        self.tproduct = Label(self.right, text='Total Price', font=('arial 18 bold'), bg='lightgreen', fg='white')
        self.tproduct.place(x=450,y=40)

        #entry label
        self.itemlabel = Label(self.left, text='Enter product ID', font=('arial 18 bold'), bg='white')
        self.itemlabel.place(x=10,y=40)

        self.item_e = Entry(self.left, width=10,font=('arial 24 bold'),bg='grey')
        self.item_e.place(x=10,y=80)

        #button
        self.item_b = Button(self.left, text='Search', width=10, height=2, bg='green', command=self.search)
        self.item_b.place(x=150,y=80)

        

        #Label that will be inserted by def search
        self.product_name = Label(self.left, font=('arial 18 bold'), bg='white')
        self.product_name.place(x=10, y=140)

        self.product_price = Label(self.left, font=('arial 18 bold'), bg='white')
        self.product_price.place(x=10, y=180)




    def search(self, *args, **kwargs):
        self.get_id = self.item_e.get()
        query = "SELECT name, price FROM clothe WHERE id=?"
        result = c.execute(query, (self.get_id, ))
        for self.r in result:
            self.get_name = self.r[0]
            self.get_price = self.r[1]
        self.product_name.configure(text="Product's Name: " + str(self.get_name))
        self.product_price.configure(text='Price: ' + str(self.get_price))

        #quantity / discount
        self.quantity1 = Label(self.left, text='Enter Quantity: ', font=('arial 18 bold'), bg='white')
        self.quantity1.place(x=10, y=240)

        self.quantity_e = Entry(self.left,font=('arial 18 bold') ,width=10,bg='grey')
        self.quantity_e.place(x=200,y=240)

        self.discount1 = Label(self.left,text='Enter Discount: ', font=('arial 18 bold'),bg='white')
        self.discount1.place(x=10, y=280)

        self.discount_e = Entry(self.left,font=('arial 18 bold') ,width=10,bg='grey')
        self.discount_e.place(x=200,y=280)

        #add to cart button
        self.cart_b = Button(self.left, text='Add to cart', width=10, height=2, bg='green')
        self.cart_b.place(x=200,y=320)

        #generate bill
        self.bill_name= Label(self.left, text='Given Amount', font=('arial 18 bold'), bg='white')
        self.bill_name.place(x=10, y=400)

        self.bill_name_e = Entry(self.left,font=('arial 18 bold') ,width=10,bg='grey')
        self.bill_name_e.place(x=200, y=400)

        #change button
        self.change_btn = Button(self.left, text='Calculate change', width=16, height=2, bg='green')
        self.change_btn.place(x=200,y=440)

        #generate bill
        self.bill_btn = Button(self.left, text='Generate Bills', width=50, height=2, bg='green')
        self.bill_btn.place(x=10,y=500)


root = Tk()
b = Application(root)

root.geometry('1000x600')
root.title("Cashier")
root.mainloop()
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime

conn = sqlite3.connect("D:\Final project\Database\stock.db")
c = conn.cursor()


#date
date = datetime.datetime.now().date()

#temp list
product_list = []
product_prices = []
product_quantities = []
product_id = []
list_of_label =[]

class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        #frames
        self.left = Frame(master, width=400, height=600, bg= 'white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=600, height=600, bg='SpringGreen3')
        self.right.pack(side=RIGHT)

        #components
        self.heading = Label(self.left, text='Cashier', font=('arial 18 bold underline'), bg='SpringGreen3', fg='white')
        self.heading.place(x=10,y=0)

        self.date_1 = Label(self.right, text="Today's Date: " + str(date), font=('arial 18 bold underline'),bg='SpringGreen3', fg='white')
        self.date_1.place(x=0,y=0)

        #table invoice
        self.tproduct = Label(self.right, text='Products', font=('arial 18 bold underline'), bg='SpringGreen3', fg='white')
        self.tproduct.place(x=0,y=40)

        self.tproduct = Label(self.right, text='Quantity', font=('arial 18 bold underline'), bg='SpringGreen3', fg='white')
        self.tproduct.place(x=225,y=40)

        self.tproduct = Label(self.right, text='Total Price', font=('arial 18 bold underline'), bg='SpringGreen3', fg='white')
        self.tproduct.place(x=450,y=40)

        #entry label
        self.itemlabel = Label(self.left, text='Enter product ID', font=('arial 18 bold'), bg='white')
        self.itemlabel.place(x=10,y=40)

        self.item_e = Entry(self.left, width=10,font=('arial 24 bold'),bg='grey')
        self.item_e.place(x=10,y=80)

        #button
        self.item_b = Button(self.left, text='Search', width=10, height=2, bg='SpringGreen3', command=self.search)
        self.item_b.place(x=150,y=80)

    def search(self, *args, **kwargs):
        self.get_id = self.item_e.get()
        query = "SELECT * FROM clothe WHERE id=?"
        result = c.execute(query, (self.get_id, ))
        for self.r in result:
            self.get_name = self.r[1]
            self.get_stock = self.r[2]
            self.get_originalPrice = self.r[3]
            self.get_price = self.r[4]
            self.get_totalCost = self.r[5]
            self.get_totalEarning = self.r[6]
            self.get_assumedProfit = self.r[7]

        self.product_name = Label(self.left,text="Product's Name: " + str(self.get_name), font=('arial 18 bold'), bg='white')
        self.product_name.place(x=10, y=140)

        self.product_price = Label(self.left,text='Price: ' + str(self.get_price), font=('arial 18 bold'), bg='white')
        self.product_price.place(x=10, y=180)

        #quantity / discount
        self.quantity1 = Label(self.left, text='Enter Quantity: ', font=('arial 18 bold'), bg='white')
        self.quantity1.place(x=10, y=240)

        self.quantity_e = Entry(self.left,font=('arial 18 bold') ,width=10,bg='grey')
        self.quantity_e.place(x=200,y=240)
        self.quantity_e.focus()

        self.discount1 = Label(self.left,text='Enter Discount: ', font=('arial 18 bold'),bg='white')
        self.discount1.place(x=10, y=280)

        self.discount_e = Entry(self.left,font=('arial 18 bold') ,width=10,bg='grey')
        self.discount_e.place(x=200,y=280)
        self.discount_e.insert(END, 0)

        #add to cart button
        self.cart_b = Button(self.left, text='Add to cart', width=10, height=2, bg='SpringGreen3', command=self.add_to_cart)
        self.cart_b.place(x=200,y=320)

        self.tot_b = Button(self.left, text='Total', width=10, height=2, bg='SpringGreen3', command=self.total)
        self.tot_b.place(x=300,y=320)


    def add_to_cart (self, *args, **kwargs):
        self.u1 = self.quantity_e.get()
        self.u2 = self.discount_e.get()
        self.total_price = int(self.get_price) * int(self.u1)
        if int(self.u1) > int(self.get_stock):
            tkinter.messagebox.showinfo('Error', 'quantity exceed item stocks')
        else:
            if self.u2 == 0:
                product_prices.append(self.total_price)
            else:
                self.total_price -= int(self.total_price) * int(self.u2) / 100
                product_prices.append(self.total_price)

            product_list.append(self.get_name)
            product_quantities.append(self.u1)
            product_id.append(self.get_id)
            x_loop=0
            y_loop=80
            counter = 0

            for self.p in product_list:
                self.temp_name = Label(self.right, text=str(product_list[counter]), font=('arial 20 bold'), bg='SpringGreen3', fg='white')
                self.temp_name.place(x=x_loop, y=y_loop)
                list_of_label.append(self.temp_name)

                x_loop += 225

                self.temp_price = Label(self.right, text=int(product_quantities[counter]), font=('arial 20 bold'), bg='SpringGreen3', fg='white')
                self.temp_price.place(x=x_loop, y=y_loop)
                list_of_label.append(self.temp_price)

                x_loop += 225

                self.temp_quantities = Label(self.right, text=float(product_prices[counter]), font=('arial 20 bold'), bg='SpringGreen3', fg='white')
                self.temp_quantities.place(x=x_loop, y=y_loop)
                list_of_label.append(self.temp_quantities)
                x_loop = 0
                y_loop += 40
                counter += 1
        self.item_e.delete(0, END)
        self.quantity_e.delete(0, END)
        self.product_name.destroy()
        self.product_price.destroy()


            
    def total(self, *args, **kwargs):
        total_price_bill = sum(product_prices)
        self.total_label = Label(self.left, text=('total: ' + str(total_price_bill)), font=("arial 20 bold"), bg="white")
        self.total_label.place(x=10, y=360) 

        #generate bill
        self.bill_name= Label(self.left, text='Given Amount', font=('arial 18 bold'), bg='white')
        self.bill_name.place(x=10, y=400)

        self.bill_name_e = Entry(self.left,font=('arial 18 bold') ,width=10,bg='grey')
        self.bill_name_e.place(x=200, y=400)

        #change button
        self.change_btn = Button(self.left, text='Calculate change', width=16, height=2, bg='SpringGreen3',command=self.cash_change)
        self.change_btn.place(x=200,y=440)


    def cash_change(self, *args, **kwargs):
        #generate bill
        self.bill_btn = Button(self.left, text='Update the Database', width=50, height=2, bg='SpringGreen3', command=self.reduce_stock)
        self.bill_btn.place(x=10,y=540)


        total_price_bill = sum(product_prices)
        self.total_customer_money = self.bill_name_e.get()
        if float(self.total_customer_money) < total_price_bill:
            tkinter.messagebox.showinfo('Error', 'need more money')
        else:
            labelll_change = float(self.total_customer_money) - total_price_bill
            self.label_change = Label(self.left, text=('change: ' + str(labelll_change)), font=('arial 20 bold'), bg='white')
            self.label_change.place(x=10, y=500)


    def reduce_stock (self, *args, **kwargs):
        # decrease the stock
        self.x = 0

       
        for i in product_list:
            initial = "SELECT * FROM clothe WHERE id=?"
            result = c.execute(initial, (product_id[self.x], ))

            for r in result:
                self.old_stock = r[2]
                self.og_price = r[3]
                self.price = r[4]
            self.new_stock = int(self.old_stock) - int(product_quantities[self.x])
            self.total_cost = float(self.og_price) * float(self.new_stock)
            self.total_earn = float(self.price) * float(self.new_stock)
            self.assumed_profit = float(self.total_earn) - float(self.total_cost)
            # updating the stock
            sql = "UPDATE clothe SET stock=?, totalCost=?, totalEarning=?, assumedProfit=? WHERE id=?"
            c.execute(sql, (self.new_stock,self.total_cost, self.total_earn, self.assumed_profit, product_id[self.x]))
            conn.commit()

        tkinter.messagebox.showinfo('Success','Database stock has been decreased')

        for lbl in list_of_label:
            lbl.destroy()
            
        self.product_name.destroy()
        self.product_price.destroy()
        self.quantity1.destroy()
        self.quantity_e.destroy()
        self.discount1.destroy()
        self.discount_e.destroy()
        self.cart_b.destroy()
        self.tot_b.destroy()
        self.change_btn.destroy()
        self.bill_btn.destroy()
        self.bill_name.destroy()
        self.bill_name_e.destroy()
        self.label_change.destroy()
        self.total_label.destroy()
        self.item_e.delete(0, END)

        product_list.clear()
        product_prices.clear()
        product_quantities.clear()
        product_id.clear()
        list_of_label.clear()


root = Tk()
b = Application(root)

root.geometry('1000x600')
root.title("Cashier")
root.mainloop()
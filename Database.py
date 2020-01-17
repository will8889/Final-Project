from tkinter import *
import sqlite3
import tkinter.messagebox


conn = sqlite3.connect("D:\Final project\Database\stock.db")
c = conn.cursor()

class Database:
        def __init__(self, master, *args, **kwargs):

                self.master = master
                self.heading = Label(master, text="Store your item", font=('arial 40 bold'), fg='green')
                self.heading.place(x=300, y=0)

#==================================================== Labels ========================================
                
                self.id1 = Label(master, text="Enter ID", font=('arial 20 bold'))
                self.id1.place(x=10, y=70)

                self.name1 = Label(master, text="Enter Name", font=('arial 20 bold'))
                self.name1.place(x=10, y=120)

                self.stock1 = Label(master, text="Enter Stock", font=('arial 20 bold'))
                self.stock1.place(x=10, y=170)

                self.originalPrice1 = Label(master, text="Enter Original Price", font=('arial 20 bold'))
                self.originalPrice1.place(x=10, y=220)

                self.price1 = Label(master, text="Enter Price", font=('arial 20 bold'))
                self.price1.place(x=10, y=270)


#==================================================== ENTRY =====================================
                
                self.id_e = Entry(master, width=25,font=('arial 20 bold'))
                self.id_e.place(x=320,y=70)

                self.name_e = Entry(master, width=25,font=('arial 20 bold'))
                self.name_e.place(x=320,y=120)

                self.stock_e = Entry(master, width=25,font=('arial 20 bold'))
                self.stock_e.place(x=320,y=170)

                self.originalPrice_e = Entry(master, width=25,font=('arial 20 bold'))
                self.originalPrice_e.place(x=320,y=220)

                self.price_e = Entry(master, width=25,font=('arial 20 bold'))
                self.price_e.place(x=320,y=270)


#============================================== BUTTON ========================================
                
                self.btn_store = Button(master, text="Store",font=('arial 20 bold'), width=20, height=2, bg='green', fg='white', command=self.store_items)
                self.btn_store.place(x=300,y=370)
                self.btn_clear = Button(master, text="Clear", font=('arial 16 bold'), width=10, height=2, bg='green', fg='white', command=self.delete_entry)
                self.btn_clear.place(x=10,y=370)

#=========================================== ENTRY LOG =================================
                
                self.log = Text(master, width=32,height=25)
                self.log.place(x=720, y=70)
#====================================FUNCTION===============================
        def delete_entry(self, *args, **kwargs):
                self.id_e.delete(0, END)
                self.name_e.delete(0, END)
                self.stock_e.delete(0, END)
                self.originalPrice_e.delete(0, END)
                self.price_e.delete(0, END)

        def store_items(self, *args, **kwargs):
                self.id = self.id_e.get()
                self.name = self.name_e.get()
                self.stock = self.stock_e.get()
                self.originalPrice = self.originalPrice_e.get()
                self.price = self.price_e.get()
                if self.id == '' or self.name == '' or self.stock == '' or self.originalPrice == '' or self.price == '':
                        tkinter.messagebox.showinfo('Error', 'Please fill all the entries')
                else:
                        test = 'SELECT id FROM clothe'
                        test2 = c.execute(test)
                        counter = 0
                        for r in test2:
                                self.ids = list(r)
                                if int(self.id) in self.ids:
                                        counter += 1
                        if counter != 0:
                                MsgBox = tkinter.messagebox.askquestion ('Error','There is existing id in database, do you want to rewrite it?',icon = 'warning')
                                if MsgBox == 'yes':
                                        self.totalCost = float(self.originalPrice) * float(self.stock)
                                        self.totalEarning = float(self.price) * float(self.stock)
                                        self.assumedProfit = float(self.totalEarning - self.totalCost)
                                        updet = "UPDATE clothe SET name=?, stock=?, originalPrice=?, price=?, totalCost=?, totalEarning=?, assumedProfit=? WHERE id=?"
                                        c.execute(updet, (self.name,self.stock, self.originalPrice, self.price,self.totalCost, self.totalEarning, self.assumedProfit, self.id))
                                        conn.commit()
                                        tkinter.messagebox.showinfo("Success", "Your Database has been updated")
                                else:
                                        self.id_e.delete(0, END )
                        else:
                                self.totalCost = float(self.originalPrice) * float(self.stock)
                                self.totalEarning = float(self.price) * float(self.stock)
                                self.assumedProfit = float(self.totalEarning - self.totalCost)
                                sql = 'INSERT INTO clothe (id, name, stock, originalPrice, price, totalCost, totalEarning, assumedProfit) VALUES(?,?,?,?,?,?,?,?)'
                                c.execute(sql, (self.id, self.name, self.stock, self.originalPrice, self.price, self.totalCost, self.totalEarning, self.assumedProfit))
                                conn.commit()
                                self.log.insert(END, 'Added ' + str(self.name) + ' into your database\n')
                                tkinter.messagebox.showinfo("SUCCESS", 'Your item have been stored')


root = Tk()
b = Database(root)

root.geometry('1000x600')
root.title("Store your item")
root.mainloop()
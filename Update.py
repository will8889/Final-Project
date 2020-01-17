from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("D:\Final project\Database\stock.db")
c = conn.cursor()

class Update:
        def __init__(self, master, *args, **kwargs):

                self.master = master
                self.heading = Label(master, text="Update your item", font=('arial 40 bold'), fg='green')
                self.heading.place(x=300, y=0)

#=================================================== Label & Entry ================================
                self.id1 = Label(master, text="Enter ID", font=('arial 20 bold'))
                self.id1.place(x=10, y=70)

                self.id_entry = Entry(master, font=('arial 20 bold'), width=10)
                self.id_entry.place(x=320,y=70)

                self.id_btn = Button(master, text='Search', font=('arial 20 bold'),width=8, height=1, bg='green', fg='white', command=self.search)
                self.id_btn.place(x=520,y=60)
#==================================================== Labels ========================================


                self.name1 = Label(master, text="Enter Name", font=('arial 20 bold'))
                self.name1.place(x=10, y=120)

                self.stock1 = Label(master, text="Enter Stock", font=('arial 20 bold'))
                self.stock1.place(x=10, y=170)

                self.originalPrice1 = Label(master, text="Enter Original Price", font=('arial 20 bold'))
                self.originalPrice1.place(x=10, y=220)

                self.price1 = Label(master, text="Enter Price", font=('arial 20 bold'))
                self.price1.place(x=10, y=270)

                self.totalCost1 = Label(master, text="Total Cost Price", font=('arial 20 bold'))
                self.totalCost1.place(x=10, y=320)

                self.totalEarning1 = Label(master, text="Total Earning Price", font=('arial 20 bold'))
                self.totalEarning1.place(x=10, y=370)

#==================================================== ENTRY =====================================

                self.name_e = Entry(master, width=25,font=('arial 20 bold'))
                self.name_e.place(x=320,y=120)

                self.stock_e = Entry(master, width=25,font=('arial 20 bold'))
                self.stock_e.place(x=320,y=170)

                self.originalPrice_e = Entry(master, width=25,font=('arial 20 bold'))
                self.originalPrice_e.place(x=320,y=220)

                self.price_e = Entry(master, width=25,font=('arial 20 bold'))
                self.price_e.place(x=320,y=270)

                self.totalCost_e = Entry(master, width=25,font=('arial 20 bold'))
                self.totalCost_e.place(x=320,y=320)

                self.totalEarning_e = Entry(master, width=25,font=('arial 20 bold'))
                self.totalEarning_e.place(x=320,y=370)


#============================================== BUTTON ========================================
                self.btn_store = Button(master, text="Update",font=('arial 20 bold'), width=20, height=2, bg='green', fg='white', command=self.update)
                self.btn_store.place(x=300,y=470)
                self.btn_clear = Button(master, text="Clear", font=('arial 16 bold'), width=10, height=2, bg='green', fg='white', command=self.delete_entry)
                self.btn_clear.place(x=10,y=470)
#=========================================== ENTRY LOG =================================
                self.log = Text(master, width=30,height=25)
                self.log.place(x=720, y=70)
#=================================================FUNCTION===========================
        def delete_entry(self, *args, **kwargs):
                self.id_entry.delete(0, END)
                self.name_e.delete(0, END)
                self.stock_e.delete(0, END)
                self.originalPrice_e.delete(0, END)
                self.price_e.delete(0, END)
                self.totalCost_e.delete(0, END)
                self.totalEarning_e.delete(0, END)

        def search(self, *args, **kwargs):
                try:
                        sql = "SELECT * FROM clothe WHERE id=?"
                        result = c.execute(sql, (self.id_entry.get(), ))
                        for r in result:
                                self.n1 = r[1]
                                self.n2 = r[2]
                                self.n3 = r[3]
                                self.n4 = r[4]
                                self.n5 = r[5]
                                self.n6 = r[6]
                                self.n7 = r[7]
                        conn.commit()
                        #insert the entries to update
                        self.name_e.delete(0, END)
                        self.name_e.insert(0, str(self.n1))

                        self.stock_e.delete(0, END)
                        self.stock_e.insert(0, str(self.n2))
                        self.originalPrice_e.delete(0, END)
                        self.originalPrice_e.insert(0, str(self.n3))

                        self.price_e.delete(0, END)
                        self.price_e.insert(0, str(self.n4))

                        self.price_e.delete(0, END)
                        self.price_e.insert(0, str(self.n4))

                        self.price_e.delete(0, END)
                        self.price_e.insert(0, str(self.n4))

                        self.totalCost_e.delete(0, END)
                        self.totalCost_e.insert(0, str(self.n5))

                        self.totalEarning_e.delete(0, END)
                        self.totalEarning_e.insert(0, str(self.n6))
                except:
                        tkinter.messagebox.showinfo('Error', 'Please input correctly')

        def update(self, *args, **kwargs):
                try:
                        #get all the updated value
                        self.u_id = self.id_entry.get()
                        self.u1 = self.name_e.get()
                        self.u2 = self.stock_e.get()
                        self.u3 = self.originalPrice_e.get()
                        self.u4 = self.price_e.get()
                        self.u5 = float(self.u3) * float(self.u2)
                        self.u6 = float(self.u4) * float(self.u2)
                        self.u7 = float(self.u6) - float(self.u5)

                        query = "UPDATE clothe SET name=?, stock=?, originalPrice=?, price=?, totalCost=?, totalEarning=?, assumedProfit=? WHERE id=?"
                        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6,self.u7, self.u_id))
                        conn.commit()
                        self.log.insert(END, 'Your item have been updated\n')
                        tkinter.messagebox.showinfo("Success", "Your item have been updated")
                except:
                        tkinter.messagebox.showinfo('Error', 'Please input correctly')
               
                
root = Tk()
b = Update(root)

root.geometry('1000x600')
root.title("Update your item")
root.mainloop()
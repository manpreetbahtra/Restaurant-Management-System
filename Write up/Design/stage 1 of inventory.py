#############################################Inventory######################
from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox

class Inventory:

    def __init__(self,inventory):
        self.inventory = inventory
        self.inventory.title("Inventory")
        self.inventory.geometry("1350x800+0+0")
        self.inventory.configure(background='white')
        
#######################FRAMES########################

        Frame1 = Frame(self.inventory, bd=15, bg='white', width=1400, height=700, relief=RIDGE)###first frame- that opens main screen
        Frame1.grid()

        Frame2 = Frame(Frame1, bd=8, bg='white', width=800, height=500, padx=10, relief=RIDGE)###this frame resides in frame 1
        Frame2.pack(side=LEFT)

        Frame3 = Frame(Frame1, bd=8, bg='white', width=800, height=500, padx=10, relief=RIDGE)##this frame resides in frame 1
        Frame3.pack(side=RIGHT)

        #######################left and right frames ########################
        Frame4 = Frame(Frame2, bd=6, width=712, height=143, padx=6, bg='white', relief=RIDGE)
        Frame4.grid(row=0,column=0)

        Frame41 = Frame(Frame2, bd=6, width=712, height=160, padx=6, bg='white', relief=RIDGE)#resides in left frame
        Frame41.grid(row=1,column=0)

        Frame42 = Frame(Frame2, bd=6, width=712, height=160, padx=6, bg='white', relief=RIDGE)
        Frame42.grid(row=2,column=0)

##        Frame43 = Frame(Frame2, bd=6, width=712, height=80, padx=6, bg='white', relief=RIDGE)
##        Frame43.grid(row=3,column=0)

        Frame5 = Frame(Frame3, bd=6, width=500,  height=280, padx=6,bg='white', relief=RIDGE)
        Frame5.grid(row=0, column=0)

        Frame51 =Frame(Frame3, bd=6, width=500, height=280, padx=6,bg='white', relief=RIDGE)#resides in right frame
        Frame51.grid(row=1, column=0)

        Frame52 =Frame(Frame3, bd=6, width=500, height=280, padx=6,bg='white', relief=RIDGE)
        Frame52.grid(row=2, column=0)
        

##################################frame4##########################
        
        self.InventoryItems = ttk.Treeview(Frame4,height=15)

        self.InventoryItems['columns'] = ("productCode", 'itemName', 'quantity', 'reOrderLevel')

        self.InventoryItems.column("#0", width=0,  stretch=NO)
        self.InventoryItems.column("productCode",anchor=CENTER,width=90)
        self.InventoryItems.column("itemName",anchor=CENTER, width=150)
        self.InventoryItems.column("quantity",anchor=CENTER,width=90)
        self.InventoryItems.column("reOrderLevel",anchor=CENTER,width=90)

        self.InventoryItems.heading("#0",text="",anchor=CENTER) #phantom column
        self.InventoryItems.heading("productCode",text="Product Code", anchor=CENTER)
        self.InventoryItems.heading("itemName",text="Item Name",anchor=CENTER)
        self.InventoryItems.heading("quantity",text="Quantity",anchor=CENTER)
        self.InventoryItems.heading("reOrderLevel",text="Re-order Level",anchor=CENTER)

##        self.InventoryItems.insert(parent='',index='end',iid=0,text='',
##        values=(1,'Cookie Dough','100','20'))
##        self.InventoryItems.insert(parent='',index='end',iid=1,text='',
##        values=(2,'Fries','102','30'))
##        self.InventoryItems.insert(parent='',index='end',iid=2,text='',
##        values=(3,'Ben & Jerrys ice cream','97', '15'))
##        self.InventoryItems.insert(parent='',index='end',iid=3,text='',#iid need to be unique
##        values=(4,'Cinnamon Twists','87','25' ))
##        self.InventoryItems.insert(parent='',index='end',iid=4,text='',
##        values=(5,'Vegetables','57','40'))
##        self.InventoryItems.insert(parent='',index='end',iid=5,text='',
##        values=(6,'Fruits','90','40'))
##        self.InventoryItems.insert(parent='',index='end',iid=6,text='',
##        values=(7,'Bread','46','25'))
##        self.InventoryItems.insert(parent='',index='end',iid=7,text='',
##        values=(8,'Fish Fingers','99','40'))
##        self.InventoryItems.insert(parent='',index='end',iid=8,text='',
##        values=(9,'Pepsi','106','100'))
##        self.InventoryItems.insert(parent='',index='end',iid=9,text='',
##        values=(10,'Coke','200','150'))
        self.InventoryItems.grid()

        #######################labels, buttons, functions and entry boxes for frame 41########################
        productCodeLabel = Label(Frame41, text="Product Code")
        productCodeLabel.grid(row=0, column=0)

        itemNameLabel = Label(Frame41, text="Item Name")
        itemNameLabel.grid(row=0, column=1)

        quantityLabel = Label(Frame41, text="Quantity")
        quantityLabel.grid(row=0, column=2)

        reOrderLevelLabel = Label(Frame41, text="Re-order level")
        reOrderLevelLabel.grid(row=0, column=3)
        

        productCodeEntry = Entry(Frame41)
        productCodeEntry.grid(row=1, column=0)

        itemNameEntry = Entry(Frame41)
        itemNameEntry.grid(row=1, column=1)

        quantityEntry = Entry(Frame41)
        quantityEntry.grid(row=1, column=2)

        reOrderLevelEntry = Entry(Frame41)
        reOrderLevelEntry.grid(row=1, column=3)


        global inventoryProducts
        inventoryProducts = [
            [1,'Cookie Dough','100','20'],
            [2,'Fries','102','30'],
            [3,'Ben & Jerrys ice cream','97', '15'],
            [4,'Cinnamon Twists','87','25'],
            [5,'Vegetables','57','40'],
            [6,'Fruits','90','40'],
            [7,'Bread','46','25'],
            [8,'Fish Fingers','99','40'],
            [9,'Pepsi','106','100'],
            [10,'Coke','200','150'],
        ]


        global count
        count=0
        for record in inventoryProducts:
            self.InventoryItems.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]))
            count+=1

        
        #############################################Labels Frame5##################
        self.lblOpenAccount = Label(Frame5, font=('arial', 18, 'bold'), text="Account Opened:",padx=2, pady=2, bg='white')
        self.lblOpenAccount.grid(row=0,column=0, sticky=W)

        self.cboOpenAccount = ttk.Combobox(Frame5, textvariable=openAccount, state='readonly',
                                           font=('arial', 18, 'bold'), width=19) #cbo stands for combobox
        self.cboOpenAccount['value'] =("", "Select an option", "Yes", "No")
        self.cboOpenAccount.current(0)
        self.cboOpenAccount.grid(row=0,column=1,pady=2)
        

        self.lblDateOfApp = Label(Frame5, font=('arial', 18, 'bold'), text="Date of App:",padx=2, pady=2, bg='white')
        self.lblDateOfApp.grid(row=1,column=0, sticky=W)

        self.cboDateOfApp = ttk.Combobox(Frame5, textvariable=dateOfApp, state='readonly',
                                           font=('arial', 18, 'bold'), width=19) #cbo stands for combobox
        self.cboDateOfApp['value'] =("", "Select an option", "A", "B")
        self.cboDateOfApp.current(0)
        self.cboDateOfApp.grid(row=1,column=1, pady=2)

        

        self.lblNextCreditReview = Label(Frame5, font=('arial', 18, 'bold'), text="Next Credit Review:",padx=2, pady=2, bg='white')
        self.lblNextCreditReview.grid(row=2,column=0, sticky=W)

        self.cboNextCreditReview = ttk.Combobox(Frame5, textvariable=nextCreditReview, state='readonly',
                                           font=('arial', 18, 'bold'), width=19) #cbo stands for combobox
        self.cboNextCreditReview['value'] =("", "Select an option", "A", "B")
        self.cboNextCreditReview.current(0)
        self.cboNextCreditReview.grid(row=2,column=1, pady=2)


        self.lblLastCreditReview = Label(Frame5, font=('arial', 18, 'bold'), text="Last Credit Review:",padx=2, pady=2, bg='white')
        self.lblLastCreditReview.grid(row=3,column=0, sticky=W)

        self.cboLastCreditReview = ttk.Combobox(Frame5, textvariable=lastCreditReview, state='readonly',
                                           font=('arial', 18, 'bold'), width=19) #cbo stands for combobox
        self.cboLastCreditReview['value'] =("", "Select an option", "A", "B")
        self.cboLastCreditReview.current(0)
        self.cboLastCreditReview.grid(row=3,column=1, pady=2)


        self.lblDateOfReview = Label(Frame5, font=('arial', 18, 'bold'), text="Date Of Review:",padx=2, pady=2, bg='white')
        self.lblDateOfReview.grid(row=4,column=0, sticky=W)

        self.cboDateOfReview = ttk.Combobox(Frame5, textvariable=dateOfReview, state='readonly',
                                           font=('arial', 18, 'bold'), width=19) #cbo stands for combobox
        self.cboDateOfReview['value'] =("", "Select an option", "A", "B")
        self.cboDateOfReview.current(0)
        self.cboDateOfReview.grid(row=4,column=1,pady=2)
        
        #############################################Labels Frame5######

        self.txtInventoryReceipt= Text(Frame51, height=35, width=71, font=('arial', 9, 'bold'))
        self.txtInventoryReceipt.grid(row=0, column=0)#receipt for inventory which allows to type as it text

        receiptReference = StringVar()
        ############################functions in frame52#############

        def reset():
            checkFreezer.set(0)
            checkExpiryDates.set(0)
            checkDishes.set(0)
            checkHygiene.set(0)
##            tax.set("")
##            subtotal.set("")
##            total.set("")
            receiptReference.set("")
            self.txtInventoryReceipt.delete("1.0", END)
            return

        def exitInventory():
            answer= tkinter.messagebox.askyesno("Confirm Exit", "Are you sure to exit?")
            if answer == 1:
                inventory.destroy()
            else:
                return #do nothing

        ######Functions Frame52#######
        def total():
            x= random.randint(1000, 900000)
            randomReference= str(x)
            receiptReference.set("Inventory Receipt" + randomReference)

            self.txtInventoryReceipt.insert(END, "Receipt Reference:\t\t\t\t"+receiptReference.get())
            InventoryProducts = str(inventoryProducts)
            self.txtInventoryReceipt.insert(END, InventoryProducts)
            InventoryReceipt = str(self.txtInventoryReceipt)
            file = open("Inventory Receipt " +randomReference , "w") # w for write mode
            file.write(randomReference + "\n")# \n stands for new line
            file.write(InventoryProducts)
            file.write(InventoryReceipt)
            file.close()

        #####################################Buttons Frame52###################
        self.btnTotal = Button (Frame52, padx=18, pady=2, bd=4, fg='black', font=('arial', 9, 'bold'),
                                width=9, bg='white', text='Total', command=total).grid(row=0, column=0)
        self.btnReset = Button (Frame52, padx=18, pady=2, bd=4, fg='black', font=('arial', 9, 'bold'),
                                width=9, bg='white', text='Reset', command= reset).grid(row=0, column=1)
        self.btnExit = Button (Frame52, padx=18, pady=2, bd=4, fg='black', font=('arial', 9, 'bold'),
                                width=9, bg='white', text='Exit', command=exitInventory).grid(row=0, column=2)


if __name__== '__main__':
    inventory=Tk()
    application=Inventory(inventory)
    inventory.mainloop()

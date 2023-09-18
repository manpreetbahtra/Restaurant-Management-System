from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from tkinter import*  # * imports everything from tkinter
import os  # imports operating system
from tkinter import messagebox
import tempfile


class POS:

    def __init__(self,root):
        self.root = root
        self.root.title("Point of Sale")
        self.root.geometry("1400x800")
        self.root.configure(background='grey')
        self.inputValue = True

        global operator
        operator = ""
        changeInput = StringVar()
        taxInput = StringVar()
        subTotalInput = StringVar()
        totalInput = StringVar()
        item = StringVar()
        quantity = StringVar()
        amount = StringVar()
        choice = StringVar()
        cashInput = StringVar()
        


        self.chips = PhotoImage(file = "chips.gif")
        self.vegBurger = PhotoImage(file = "vegBurger.png")
        self.chickenBurger = PhotoImage(file = "chickenBurger.gif")
        self.sandwich = PhotoImage(file = "sandwich.gif")
        self.fishFingers = PhotoImage(file = "fishFingers.png")
        self.noodles = PhotoImage(file = "noodles.gif")

        self.coffee = PhotoImage(file = "coffee.png")
        self.coke = PhotoImage(file = "coke.png")
        self.orangeJuice = PhotoImage(file = "orangeJuice.png")
        self.sprite = PhotoImage(file = "sprite.png")
        self.lemonade = PhotoImage(file = "lemonade.png")
        self.pepsi = PhotoImage(file = "pepsi.png")
        self.fanta = PhotoImage(file = "fanta.png")

        self.cookies = PhotoImage(file = "cookies.gif")
        self.iceCream = PhotoImage(file = "iceCream.gif")
        self.applePie = PhotoImage(file = "applePie.gif")
        self.chocolateLavaCake = PhotoImage(file = "chocolateLavaCake.gif")
        self.cinnamonRolls = PhotoImage(file = "cinnamonRolls.png")

        self.cottagePie = PhotoImage(file = "cottagePie.png")
        self.beefStew = PhotoImage(file = "beefStew.png")
        self.cheeseDumplings = PhotoImage(file = "cheeseDumplings.png")
        self.lasagne = PhotoImage(file = "lasagne.png")
        self.riceWithVegetableCurry = PhotoImage(file = "riceWithVegetableCurry.png")

        #####################################Functions #################################################
        def deleteItem(): #remove unwanted items
            costOfItem = 0.0
            tax = 2.5
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values")[2])
                subTotalInput.set(str('£%.2f'%(costOfItem)))
                taxInput.set(str('£%.2f' %(((costOfItem * tax)/100))))
                totalInput.set(str('£%.2f' %((costOfItem) + ((costOfItem *tax)/100))))
                selectedItem = (self.POSRecords.selection()[0])
                self.POSRecords.delete(selectedItem)
            

        def exitPOS():
                answer= tkinter.messagebox.askyesno("Confirm Exit", "Are you sure to exit?")
                if answer == 1:
                    root.destroy()
                else:
                    return #do nothing

        def paymentMethod():
            if (choice.get() == "Cash"):
                self.txtCost.focus()
                cashInput.set("")
            elif (choice.get() == ""):
                cashInput.set("0")
                changeInput.set("")

        def reset():
            changeInput.set("")
            cashInput.set("")
            taxInput.set("")
            subTotalInput.set("")
            totalInput.set("")
            for x in self.POSRecords.get_children():
                self.POSRecords.delete(x)

        def printReceipt():
            a = self.txtReceipt.get("1.0", "end-1c")
            print (a)
            filename = tempfile.mktemp(".txt")
            open(filename, "w").write(a)
            os.startfile(filename, "print")

        def pay():
            pay= tkinter.messagebox.showinfo(title='Payment Successful!', message='Enjoy your meal')
		

        #####################################Frames #################################################

        mainFrame = Frame(self.root, bg='grey')
        mainFrame.grid(padx=8, pady=5)

        buttonFrame = Frame(mainFrame, bg='grey' , bd=5, width=1348, height =160, padx=4, pady=4, relief=RIDGE)
        buttonFrame.pack(side=BOTTOM)

        dataFrame = Frame(mainFrame, bg='grey' , bd=5, width=800, height =300, padx=4, pady=4, relief=RIDGE)
        dataFrame.pack(side=LEFT)

        dataFrameLEFTCOVER = LabelFrame(dataFrame, bg='grey' , bd=5, width=800, height =300, padx=4, pady=4,
                                        font=('arial', 12,'bold'),text="Point of Sale", relief=RIDGE)
        dataFrameLEFTCOVER.pack(side=LEFT)

        changeButtonFrame = Frame(dataFrameLEFTCOVER, bd=5, width=300, height =460, pady=4, relief=RIDGE)
        changeButtonFrame.pack(side=LEFT,padx=4)

        receiptFrame = Frame(dataFrameLEFTCOVER, bd=5, width=200, height =400, pady=5, relief=RIDGE)
        receiptFrame.pack(side=RIGHT,padx=4)

        foodItemFrame = LabelFrame(dataFrame, bd=5, width=450, height =300, padx=5, pady=2, bg='grey',
                                   font=('arial', 12,'bold'),text="Items", relief=RIDGE)
        foodItemFrame.pack(side=RIGHT)

        calculatorFrame = Frame(buttonFrame, bd=5, width=432, height=140, relief=RIDGE)
        calculatorFrame.grid(row = 0, column = 0, padx=5)

        changeFrame = Frame(buttonFrame, bd=5, width=500, height=140, pady =2, relief=RIDGE)
        changeFrame.grid(row = 0, column = 1, padx=5)

        removeFrame = Frame(buttonFrame, bd=5, width=400, height=140, pady =4, relief=RIDGE)
        removeFrame.grid(row = 0, column = 2, padx=5)

        ##############################################Entry and label widget #################################################
        self.lblSubTotal = Label(calculatorFrame, font=('arial', 14, 'bold'), text="Sub Total", bd=5)
        self.lblSubTotal.grid(row=0,column=0, sticky=W, padx=5)
        self.txtSubTotal = Entry(calculatorFrame, font=('arial', 14, 'bold'), textvariable=subTotalInput, bd=2, justify= LEFT, width =24)
        self.txtSubTotal.grid(row=0,column=1, sticky=W, padx=5)
        
        self.lblTax = Label(calculatorFrame, font=('arial', 14, 'bold'), text="Tax", bd=5)
        self.lblTax.grid(row=1,column=0, sticky=W, padx=5)
        self.txtTax = Entry(calculatorFrame, font=('arial', 14, 'bold'), textvariable=taxInput, bd=2, justify= LEFT, width =24)
        self.txtTax.grid(row=1,column=1, sticky=W, padx=5)

        self.lblTotal = Label(calculatorFrame, font=('arial', 14, 'bold'), text="Total", bd=5)
        self.lblTotal.grid(row=2,column=0, sticky=W, padx=5)
        self.txtTotal = Entry(calculatorFrame, font=('arial', 14, 'bold'), textvariable=totalInput, bd=2, justify= LEFT, width =24) # entry is for input fields. 
        self.txtTotal.grid(row=2,column=1, sticky=W, padx=5)

        self.lblPaymentMethod = Label(changeFrame, font=('arial', 14, 'bold'), text="Payment Method", bd=5)
        self.lblPaymentMethod.grid(row=0,column=0, sticky=W, padx=5)
        self.cboPaymentMethod = ttk.Combobox(changeFrame, font=('arial', 14, 'bold'), justify= RIGHT, width =24, state='readonly',
                                             textvariable=choice) # combobox is for dropdown menu
        self.cboPaymentMethod['value'] = ('', 'Cash', 'Visa Card', 'Master Card', 'Gift Card')
        self.cboPaymentMethod.current(0)
        self.cboPaymentMethod.grid(row=0,column=1)
        
        self.lblCost = Label(changeFrame, font=('arial', 14, 'bold'), text="Cash", bd=5)
        self.lblCost.grid(row=1,column=0, sticky=W, padx=5)
        self.txtCost = Entry(changeFrame, font=('arial', 14, 'bold'), textvariable=cashInput, bd=2, justify= LEFT, width =24,)
        self.txtCost.grid(row=1,column=1, sticky=W, padx=5)
        self.txtCost.insert(0, "0")

        self.lblChange = Label(changeFrame, font=('arial', 14, 'bold'), text="Change", bd=5)
        self.lblChange.grid(row=2,column=0, sticky=W, padx=5)
        self.txtChange = Entry(changeFrame, font=('arial', 14, 'bold'), textvariable=changeInput, bd=2, justify= LEFT, width =24)
        self.txtChange.grid(row=2,column=1, sticky=W, padx=5)

        self.btnPay= Button(removeFrame, padx=2, font=('arial', 15, 'bold'), text="Pay", width=10, height=1, bd=2,command=pay)
        self.btnPay.grid(row=1,column=0, pady=2, padx=7)

        self.btnPrintReceipt= Button(removeFrame, padx=2, font=('arial', 15, 'bold'), text="Print Receipt", width=10, height=1, bd=2, command=printReceipt)
        self.btnPrintReceipt.grid(row=1,column=2, pady=2, padx=7)
        
        self.btnExit = Button(removeFrame, padx=2, font=('arial', 15, 'bold'), text="Exit", width=10, height=1, bd=2, command=exitPOS)
        self.btnExit.grid(row=1,column=1, pady=2, padx=7)
        
        self.btnReset = Button(removeFrame, padx=2, font=('arial', 15, 'bold'), text="Reset", width=10, height=1, bd=2, command= reset)
        self.btnReset.grid(row=0,column=0, pady=2, padx=7)
        
        self.btnDeleteItem = Button(removeFrame, padx=2, font=('arial', 15, 'bold'), text="Delete Item", width=10, height=1, bd=2, command = deleteItem)
        self.btnDeleteItem.grid(row=0,column=1, pady=2, padx=7)
        
        self.btnPizza = Button(removeFrame, padx=2, font=('arial', 15, 'bold'), text="Pizza", width= 10, height=1, bd=2)
        self.btnPizza.grid(row=0, column=2, pady=2, padx=7)


        ############################################### Functions for menu items ################################################
        def cookies():
            costOfItem = 3.0
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Cookies", "1", "3.00"))
            self.txtReceipt.insert(END,("Cookies" +"\t\t\t" + "1"+"\t\t\t"+ "3.00"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 3)))# %.2f stands for 2 decimal places
                taxInput.set(str('£%.2f' % (((costOfItem - 3)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-3)+((costOfItem - 3) * tax) / 100)))

        def iceCream():
            costOfItem = 4.0
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Ice Cream", "1", "4.00"))
            self.txtReceipt.insert(END,("Ice Cream" +"\t\t\t" + "1"+"\t\t\t"+ "4.00"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 4)))
                taxInput.set(str('£%.2f' % (((costOfItem - 4)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-4)+((costOfItem - 4) * tax) / 100)))

        def chocolateLavaCake():
            costOfItem = 3.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Chocolate Lava Cake", "1", "3.99"))
            self.txtReceipt.insert(END,("Chocolate Lava Cake" +"\t\t\t" + "1"+"\t\t\t"+ "3.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 3.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 3.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-3.99)+((costOfItem - 3.99) * tax) / 100)))

        def cinnamonRolls():
            costOfItem = 3.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Cinnamon Rolls", "1", "3.99"))
            self.txtReceipt.insert(END,("Cinnamon Rolls" +"\t\t\t" + "1"+"\t\t\t"+ "3.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 3.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 3.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-3.99)+((costOfItem - 3.99) * tax) / 100)))

        def chips():
            costOfItem = 3.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Chips", "1", "3.99"))
            self.txtReceipt.insert(END,("Chips" +"\t\t\t" + "1"+"\t\t\t"+ "3.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 3.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 3.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-3.99)+((costOfItem - 3.99) * tax) / 100)))

        def vegBurger():
            costOfItem = 4.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Veg Burger", "1", "4.99"))
            self.txtReceipt.insert(END,("Veg Burger" +"\t\t\t" + "1"+"\t\t\t"+ "4.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 4.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 4.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-4.99)+((costOfItem - 4.99) * tax) / 100)))

        def chickenBurger():
            costOfItem = 3.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Chicken Burger", "1", "3.99"))
            self.txtReceipt.insert(END,("Chicken Burger" +"\t\t\t" + "1"+"\t\t\t"+ "3.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 3.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 3.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-3.99)+((costOfItem - 3.99) * tax) / 100)))

        def sandwich():
            costOfItem = 4.00
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Sandwich", "1", "4.00"))
            self.txtReceipt.insert(END,("Sandwich" +"\t\t\t" + "1"+"\t\t\t"+ "4.00"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 4.00)))
                taxInput.set(str('£%.2f' % (((costOfItem - 4.00)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-4.00)+((costOfItem - 4.00) * tax) / 100)))

        def fishFingers():
            costOfItem = 3.25
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Fish Fingers", "1", "3.25"))
            self.txtReceipt.insert(END,("Fish Fingers" +"\t\t\t" + "1"+"\t\t\t"+ "3.25"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 3.25)))
                taxInput.set(str('£%.2f' % (((costOfItem - 3.25)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-3.25)+((costOfItem - 3.25) * tax) / 100)))

        def noodles():
            costOfItem = 6.50
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Noodles", "1", "6.50"))
            self.txtReceipt.insert(END,("Noodles" +"\t\t\t" + "1"+"\t\t\t"+ "6.50"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 6.50)))
                taxInput.set(str('£%.2f' % (((costOfItem - 6.50)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-6.50)+((costOfItem - 6.50) * tax) / 100)))

        def cottagePie():
            costOfItem = 4.50
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Cottage Pie", "1", "4.50"))
            self.txtReceipt.insert(END,("Cottage Pie" +"\t\t\t" + "1"+"\t\t\t"+ "4.50"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 4.50)))
                taxInput.set(str('£%.2f' % (((costOfItem - 4.50)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-4.50)+((costOfItem - 4.50) * tax) / 100)))

        def beefStew():
            costOfItem = 5.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Beef Stew", "1", "5.99"))
            self.txtReceipt.insert(END,("Beef Stew" +"\t\t\t" + "1"+"\t\t\t"+ "5.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 5.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 5.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-5.99)+((costOfItem - 5.99) * tax) / 100)))

        def lasagne():
            costOfItem = 5.00
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Lasagne", "1", "5.00"))
            self.txtReceipt.insert(END,("Lasagne" +"\t\t\t" + "1"+"\t\t\t"+ "5.00"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 5.00)))
                taxInput.set(str('£%.2f' % (((costOfItem - 5.00)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-5.00)+((costOfItem - 5.00) * tax) / 100)))

        def cheeseDumplings():
            costOfItem = 7.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Cheese Dumplings", "1", "7.99"))
            self.txtReceipt.insert(END,("Cheese Dumplings" +"\t\t\t" + "1"+"\t\t\t"+ "7.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 7.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 7.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-7.99)+((costOfItem - 7.99) * tax) / 100)))

        def riceWithVegetableCurry():
            costOfItem = 4.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Rice With Vegetable Curry", "1", "4.99"))
            self.txtReceipt.insert(END,("Rice With Vegetable Curry" +"\t\t\t" + "1"+"\t\t\t"+ "4.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 4.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 4.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-4.99)+((costOfItem - 4.99) * tax) / 100)))

        def coffee():
            costOfItem = 4.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Coffee", "1", "4.99"))
            self.txtReceipt.insert(END,("Coffee" +"\t\t\t" + "1"+"\t\t\t"+ "4.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 4.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 4.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-4.99)+((costOfItem - 4.99) * tax) / 100)))

        def coke():
            costOfItem = 2.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Coke", "1", "2.99"))
            self.txtReceipt.insert(END,("Coke" +"\t\t\t" + "1"+"\t\t\t"+ "2.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 2.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 2.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-2.99)+((costOfItem - 2.99) * tax) / 100)))

        def orangeJuice():
            costOfItem = 3.00
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Orange Juice", "1", "3.00"))
            self.txtReceipt.insert(END,("Orange Juice" +"\t\t\t" + "1"+"\t\t\t"+ "3.00"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 3.00)))
                taxInput.set(str('£%.2f' % (((costOfItem - 3.00)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-3.00)+((costOfItem - 3.00) * tax) / 100)))

        def sprite():
            costOfItem = 3.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Sprite", "1", "3.99"))
            self.txtReceipt.insert(END,("Sprite" +"\t\t\t" + "1"+"\t\t\t"+ "3.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 3.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 3.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-3.99)+((costOfItem - 3.99) * tax) / 100)))

        def lemonade():
            costOfItem = 3.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Lemonade", "1", "3.99"))
            self.txtReceipt.insert(END,("Lemonade" +"\t\t\t" + "1"+"\t\t\t"+ "3.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 3.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 3.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-3.99)+((costOfItem - 3.99) * tax) / 100)))

        def pepsi():
            costOfItem = 2.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Pepsi", "1", "2.99"))
            self.txtReceipt.insert(END,("Pepsi" +"\t\t\t" + "1"+"\t\t\t"+ "2.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 2.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 2.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-2.99)+((costOfItem - 2.99) * tax) / 100)))

        def fanta():
            costOfItem = 2.99
            tax= (0.20 * costOfItem)
            self.POSRecords.insert("", tk.END, values = ("Fanta", "1", "2.99"))
            self.txtReceipt.insert(END,("Fanta" +"\t\t\t" + "1"+"\t\t\t"+ "2.99"+"\n"))
            for child in self.POSRecords.get_children():
                costOfItem += float(self.POSRecords.item(child, "values") [2])
                subTotalInput.set(str('£%.2f'%(costOfItem - 2.99)))
                taxInput.set(str('£%.2f' % (((costOfItem - 2.99)*tax)/100)))
                totalInput.set(str('£%.2f' % ((costOfItem-2.99)+((costOfItem - 2.99) * tax) / 100)))
                
    ########################################### Treeview widget for receipt #################################################
        scroll_x = Scrollbar(receiptFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(receiptFrame, orient=VERTICAL)

        self.POSRecords = ttk.Treeview(receiptFrame, height=20, columns=("Item", "Quantity", "Price"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,  fill=Y)

        self.POSRecords.heading("Item", text="Item")
        self.POSRecords.heading("Quantity", text="Quantity")
        self.POSRecords.heading("Price", text="Price")

        self.POSRecords['show']='headings'

        self.POSRecords.column("Item", width=150)
        self.POSRecords.column("Quantity", width=100)
        self.POSRecords.column("Price", width=100)

        self.POSRecords.pack(fill=BOTH, expand=1)
        self.POSRecords.bind("<ButtonRelease-1>")#event in use is called button release

        self.txtReceipt = Text(receiptFrame, width=80, height=1, font = ('arial', 5, 'bold'))
        self.txtReceipt.pack()

        self.txtReceipt.insert(END, "Item\t\t\t\t Quantity\t\t\t Price\t\n")


############################################### Menu Button widget #################################################
        self.btncookies = Button(foodItemFrame, padx=2, image=self.cookies, width=104, height=104, bd=2,command=cookies)
        self.btncookies.grid(row=0,column=0, pady=2, padx=4)

        self.btniceCream = Button(foodItemFrame, padx=2, image=self.iceCream, width=104, height=104, bd=2, command=iceCream)
        self.btniceCream.grid(row=0,column=1, pady=2, padx=4)

        self.btnchocolateLavaCake = Button(foodItemFrame, padx=2, image=self.chocolateLavaCake, width=104, height=104, bd=2, command=chocolateLavaCake)
        self.btnchocolateLavaCake.grid(row=1,column=0, pady=2, padx=4)

        self.btncinnamonRolls = Button(foodItemFrame, padx=2, image=self.cinnamonRolls, width=104, height=104, bd=2, command=cinnamonRolls)
        self.btncinnamonRolls.grid(row=1,column=1, pady=2, padx=4)

        self.btnchips = Button(foodItemFrame, padx=2, image=self.chips, width=104, height=104, bd=2, command=chips)
        self.btnchips.grid(row=2,column=0, pady=2, padx=4)

        self.btnvegBurger = Button(foodItemFrame, padx=2, image=self.vegBurger, width=104, height=104, bd=2,command= vegBurger)
        self.btnvegBurger.grid(row=2,column=1, pady=2, padx=4)

        self.btnchickenBurger = Button(foodItemFrame, padx=2, image=self.chickenBurger, width=104, height=104, bd=2, command=chickenBurger)
        self.btnchickenBurger.grid(row=2,column=2, pady=2, padx=4)

        self.btnsandwich = Button(foodItemFrame, padx=2, image=self.sandwich, width=104, height=104, bd=2, command=sandwich)
        self.btnsandwich.grid(row=0,column=2, pady=2, padx=4)

        self.btnfishFingers = Button(foodItemFrame, padx=2, image=self.fishFingers, width=104, height=104, bd=2,command=fishFingers)
        self.btnfishFingers.grid(row=1,column=2, pady=2, padx=4)

        self.btnnoodles = Button(foodItemFrame, padx=2, image=self.noodles, width=104, height=104, bd=2,command=noodles)
        self.btnnoodles.grid(row=3,column=0, pady=2, padx=4)

        self.btncottagePie = Button(foodItemFrame, padx=2, image=self.cottagePie, width=104, height=104, bd=2, command = cottagePie)
        self.btncottagePie.grid(row=3,column=1, pady=2, padx=4)

        self.btnbeefStew = Button(foodItemFrame, padx=2, image=self.beefStew, width=104, height=104, bd=2, command=beefStew)
        self.btnbeefStew.grid(row=3,column=2, pady=2, padx=4)

        self.btnlasagne = Button(foodItemFrame, padx=2, image=self.lasagne, width=104, height=104, bd=2,command=lasagne)
        self.btnlasagne.grid(row=3,column=3, pady=2, padx=4)

        self.btncheeseDumplings= Button(foodItemFrame, padx=2, image=self.cheeseDumplings, width=104, height=104, bd=2,command=cheeseDumplings)
        self.btncheeseDumplings.grid(row=0,column=3, pady=2, padx=4)

        self.btnriceWithVegetableCurry = Button(foodItemFrame, padx=2, image=self.riceWithVegetableCurry, width=104, height=104, bd=2, command=riceWithVegetableCurry)
        self.btnriceWithVegetableCurry.grid(row=2,column=3, pady=2, padx=4)

        self.btncoffee = Button(foodItemFrame, padx=2, image=self.coffee, width=104, height=104, bd=2,command=coffee)
        self.btncoffee.grid(row=2,column=4, pady=2, padx=4)

        self.btncoke = Button(foodItemFrame, padx=2, image=self.coke, width=104, height=104, bd=2,command=coke)
        self.btncoke.grid(row=0,column=4, pady=2, padx=4)

        self.btnorangeJuice = Button(foodItemFrame, padx=2, image=self.orangeJuice, width=104, height=104, bd=2, command=orangeJuice)
        self.btnorangeJuice.grid(row=1,column=4, pady=2, padx=4)

        self.btnsprite = Button(foodItemFrame, padx=2, image=self.sprite, width=104, height=104, bd=2,command=sprite)
        self.btnsprite.grid(row=2,column=4, pady=2, padx=4)

        self.btnlemonade = Button(foodItemFrame, padx=2, image=self.lemonade, width=104, height=104, bd=2,command=lemonade)
        self.btnlemonade.grid(row=3,column=4, pady=2, padx=4)

        self.btnpepsi= Button(foodItemFrame, padx=2, image=self.pepsi, width=104, height=104, bd=2,command=pepsi)
        self.btnpepsi.grid(row=1,column=3, pady=2, padx=4)

        self.btnfanta = Button(foodItemFrame, padx=2, image=self.fanta, width=104, height=104, bd=2,command=fanta)
        self.btnfanta.grid(row=2,column=3, padx=4)
    





if __name__=='__main__' :
    root = Tk()
    application = POS(root)
    root.mainloop()


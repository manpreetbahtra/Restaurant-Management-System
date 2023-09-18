from tkinter import*  # * imports everything from tkinter
import os  # imports operating system
from tkinter import messagebox
import tempfile
import csv
from collections import Counter 
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt


def loginSuccessful():
    session()


def delete2():
    screen3.destroy()


def session(): 
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Dashboard")
    screen3.geometry("400x400")
    Label(screen3, text = "Welcome to the Dashboard").pack()
    Button(screen3 , text = "Screen after the dashboard-Order" , command = order).pack() #Once the user is logged on inventory, staff, order and analytics tab will be displayed on the top of the screen which users will have various levels of access to.


def passwordNotRecognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Unsuccessful!")
    screen4.geometry("300x250")
    Label(screen4 , text = "Password not recognised").pack()
    Button(screen4 , text = "Ok" , command = delete3).pack()

    
def delete3():
    screen4.destroy()


def userNotFound():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Unsuccessful!")
    screen5.geometry("300x250")
    Label(screen5 , text = "User not Found").pack()
    Button(screen5 , text = "Ok" , command = delete4).pack()

def delete4():
    screen5.destroy()
    
def registerUser():
    global usernameInfo
    usernameInfo = username.get()
    passwordInfo = password.get()
    confirmPasswordInfo = confirmPassword.get()

    specialCharacters = ['!', '£', '%', '&', '*','#', '@'] #specified an array for special characters

    if usernameInfo == "":
        screen1.title("Warning!")
        Label(screen1, text = "All fields are required").pack()
    elif passwordInfo == "":
        screen1.title("Warning!")
        Label(screen1, text = "All fields are required").pack()
    elif confirmPasswordInfo == "":
        screen1.title("Warning!")
        Label(screen1, text = "All fields are required").pack()
    elif passwordInfo != confirmPasswordInfo :
        screen1.title("Warning!")
        Label(screen1, text = "Password and confirm password fields should match.").pack()
    elif len(usernameInfo) <= 4:
        screen1.title("Warning!")
        Label(screen1, text = "Username must be at least 5 characters long.").pack()
    elif len(passwordInfo) <= 7 or len(passwordInfo) >= 14 :
        screen1.title("Warning!")
        Label(screen1, text = "Password must be at least 8 characters long and must not exceed 13 characters.").pack()
    elif not any(chr.isdigit() for chr in passwordInfo): # chr stands for character
        screen1.title("Warning!")
        Label(screen1, text = "Password should contain at least one numeral").pack()
    elif not any(chr in specialCharacters for chr in passwordInfo): # if there is not 'any' then, it would only be true if ALL characters are numbers or special characters. 
        screen1.title("Warning!")
        Label(screen1, text = "Password should contain at least one special character !, £, %, &, *, #, @").pack()
    elif not any(chr.isupper() for chr in passwordInfo):
        screen1.title("Warning!")
        Label(screen1, text = "The password should have at least one uppercase letter").pack()
    elif not any(chr.islower() for chr in passwordInfo):
        screen1.title("Warning!")
        Label(screen1, text = "The password should have at least one lowercase letter").pack()
    else:
        file = open(usernameInfo , "w") # w for write mode
        file.write(usernameInfo + "\n") # \n stands for new line
        file.write(passwordInfo)
        file.close() # this file stores usernames and passwords in a text file.
        
        usernameEntry.delete(0 , END)
        passwordEntry.delete(0 , END) # this clears the fields once the user has registered successfully.
        confirmPasswordEntry.delete(0 , END)


        Label(screen1, text = "Registration Successful" , fg = "blue" , font = ("Calibri" , 11)).pack()#prompts the user that their registration has been successful. fg stands for foreground.


def register(): # specifies the register function
    global screen1
    screen1 = Toplevel(screen)# creates another screen
    screen1.title("Register")
    screen1.geometry("600x450")
    
    global username
    global password
    global confirmPassword
    global usernameInfo
    global passwordInfo
    global usernameEntry
    global passwordEntry
    global confirmPasswordEntry
    global passwordVerify
    
    username = StringVar()
    password = StringVar()
    confirmPassword = StringVar() # lowercase s wouldn't work.
    
    
    Label(screen1 , text = "Username ").pack() # used screen1 at the front to specify where the label and button goes otherwise it would appear on all screens.
    usernameEntry = Entry(screen1 , textvariable = username)
    usernameEntry.pack()
    Label(screen1 , text = "Password ").pack()
    passwordEntry = Entry(screen1 , textvariable = password, show = "*" )
    passwordEntry.pack()
    Label(screen1 , text = "Confirm Password").pack()
    confirmPasswordEntry = Entry(screen1 , textvariable = confirmPassword, show = "*" )
    confirmPasswordEntry.pack()
    Label(screen1 , text = "").pack() # leaves a line
    Button(screen1 , text = "Register" , width = 10 , height = 1 , command = registerUser).pack()

    
def login(): # specifies the login function
    global screen2 #another screen for logging in.
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x350")
    
    global usernameVerify
    global passwordVerify
    
    usernameVerify = StringVar()
    passwordVerify = StringVar()
    
    global usernameEntry1
    global passwordEntry1
    
    Label(screen2 , text = "Username ").pack()
    usernameEntry1 = Entry(screen2 , textvariable = usernameVerify)
    usernameEntry1.pack()
    Label(screen2 , text = "").pack()
    Label(screen2 , text = "Password ").pack()
    passwordEntry1 = Entry(screen2 , textvariable = passwordVerify , show = "*") # show = "*" because to show asterisk instead of the actual password.
    passwordEntry1.pack()
    Label(screen2 , text = "").pack()
    Button (screen2 , text = "Login" , width = 10 , height = 1 , command = loginVerify).pack()


def loginVerify():
    username1 = usernameVerify.get()
    password1 = passwordVerify.get()
    usernameEntry1.delete(0, END)
    passwordEntry1.delete(0, END)

    listOfFiles = os.listdir()
    if username1 in listOfFiles:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            loginSuccessful()  # 1st outcome- username and password correct
        else:
            passwordNotRecognised()  # 2nd outcome- username correct password incorrect
    else:
        userNotFound()# username not found.


def mainScreen():
    global screen # because we want to access it from another function. 
    screen = Tk()
    screen.title("Restaurant Management System")
    screen.geometry("900x750") # screen size
    Label(text = "Restaurant Management System" , bg = "grey" , width = "300", height = "2" , font = ("Calibri" , 14)).pack() #header label. bg stands for background..pack() organises widgets
    Label(text = "").pack() # leaves a line # Label and Button have to be capital otherwise not recognised
    Button (text = "Login" , height = "2" , width = "30" , command = login).pack()#Buttons for login and register
    Label(text = "").pack()
    Button (text = "Register" , height = "2" , width = "30", command = register).pack()
    
    screen.mainloop() #execution of python commands halts here.


def logout():
    global screen7
    screen7.destroy()

        ########################################################################## PURCHASING SYSTEM ##################################################################################################
                                                                        ################ MENU ##################
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

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
            

##        def giveChange(): # evaluation- this is not working properly. the error says could not convert string to float. However couldnt get pay button to function 
##            global cashInput
##            cashInput = StringVar()
##            costOfItem =0.0
##            tax = 2.5
##            cashInput = float(cashInput.get())
##            for child in self.POSRecords.get_children():
##                costOfItem += float(self.POSRecords.item(child, "values")[2])
##            changeInput.set(str('£%.2f' %(cashInput - ((costOfItem) + ((costOfItem * tax)/100)))))
##            if (cashInput.get() == "0"):
##                changeInput.set("")
##                paymentMethod()

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
		

        
        #######################################################################################
        
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
        
        ##############################################SEARCH AND AUTOFILL FUNCTION FOR MENU#############################################
        searchLabel = Label(root, text="Search for item", font = ("arial", 15)) #creating a label
        searchLabel.grid(pady=5)

        searchEntry = Entry(root, font=("arial",20))#creating an entry box 
        searchEntry.grid()

        searchList = Listbox(root, width=50) # create a listbox
        searchList.grid(pady=5)

        listOfItems = ["chips", "vegBurger", "cinnamonRolls", "pepsi", "coke", "beefStew", "Orange Juice", "Lemonade","Chocolate lava cake"] # list of items in menu

        def update(data):
            searchList.delete(0, END)

            for searchItem in data:
                searchList.insert(END, searchItem)

        def fillWithMenuItem(event): #update entry box with listbox clicked
            searchEntry.delete(0, END)
            searchEntry.insert(0, searchList.get(ACTIVE)) #add clicked list item to entry box

        def check(event):#create a function to check entry vs listbox 
            typed = searchEntry.get()# assign whatever typed to a variable then check to comapre variable with the listofItems
            if typed == "":
                data = listOfItems
            else:
                data = []
                for item in listOfItems :
                    if typed.lower() in item.lower(): #c would bring up both chips and cinnamon rolls in the listbox
                        data.append(item)
            update(data)

        searchList.bind("<<ListboxSelect>>", fillWithMenuItem)
        searchEntry.bind("<KeyRelease>", check )# check to see what we just typed in the search list

        # searching for one of the items displays all the items avaialble to be searched.

                ####################################################PIZZA########################################################
        def pizza():
            pizza=Tk()
            pizza.geometry("600x500")
            pizza.title("Order Pizza")

            pizzaToppings = ["Pizza Sauce", "BBQ Sauce", "Cheese", "Gluten Free Cheese", "Vegan Cheese", "Pepperoni", "Sausage", "Mushrooms"]
            pizzaList = Listbox(pizza, selectmode=MULTIPLE) #create pizza list
            pizzaList.grid(row=0, column=0)

            for topping in pizzaToppings:
                pizzaList.insert(0,topping)


            def addItems():
                result=""
                for item in pizzaList.curselection():
                    result=result + str(pizzaList.get(item)) + "\n"

                    self.lbl.config(text="Your Pizza selection" + "\n" + result)

            self.lbl= Label(pizza,text="")
            self.lbl.grid(row=5, column=1)

            addItem = Button(pizza, text="Add Items", command=addItems)
            addItem.grid(row=5, column=0)

            def checkout():
                self.POSRecords.insert("", tk.END, values = ("Pizza", "1", "7.99"))
                self.txtReceipt.insert(END,("Pizza" +"\t\t\t" + "1"+"\t\t\t"+ "7.99"+"\n"))
                file = open('itemsSold' , "a") # w for write mode
                file.write("Pizza" + '\n')
                file.close()
            
            checkout = Button(pizza, text="Checkout", command=checkout)
            checkout.grid(row=6,column=0)

            def deleteItem():
                temporary=[]
                deletingOperator=[]
                for i in pizzaList.curselection()[::-1]:
                    temporary.append(pizzaList.get(i))
                    pizzaList.delete(i)
                    deletingOperator.extend(temporary)
                #pizzaList.delete(0,7)
                

            delete = Button(pizza, text="Delete Item", command=deleteItem)
            delete.grid(row=7,column=0)

            def exitPizza():
                answer= messagebox.askyesno("Confirm Exit", "Are you sure to exit?")
                if answer == 1:
                    pizza.destroy()
                else:
                    return #do nothing

            exitPizza = Button(pizza, text="Exit",command=exitPizza)
            exitPizza.grid(row=8, column=0)


            pizza.mainloop()

                    
        ###############################################Entry and label widget #################################################
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

##        self.lblCash = Label(changeFrame, font=('arial', 14, 'bold'), text="Cash", bd=5)
##        self.lblCash.grid(row=1,column=0, sticky=W, padx=5)
##        self.txtCash = Entry(changeFrame, font=('arial', 14, 'bold'), textvariable=cashInput, bd=2, justify= LEFT, width =24)
##        self.txtCash.grid(row=1,column=1, sticky=W, padx=5)

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
        
        self.btnPizza = Button(removeFrame, padx=2, font=('arial', 15, 'bold'), text="Pizza", width= 10, height=1, bd=2, command=pizza)
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
            file = open('itemsSold.txt' , "a") # a for add mode # \n stands for new line
            file.write("Cookies;"+ "\n")
            file.close()

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
            file = open('itemsSold.txt' , "a") # a for add mode
            file.write("Ice Cream;")# \n stands for new line
            file.close()

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
            file = open('itemsSold.txt' , "a") 
            file.write("Chocolate Lava Cake;" + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") 
            file.write("Cinnamon Rolls" + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Chips' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Veg Burger' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Chicken Burger' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") 
            file.write('Sandwich' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write("Fish Fingers" + '\n')
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write("Noodles" + "\n")
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Cottage Pie' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Beef Stew' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Lasagne' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Cheese Dumplings' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Rice With Vegetable Curry' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Coffee' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Coke' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Orange Juice' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Sprite' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Lemonade' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Pepsi' + "\n")# \n stands for new line
            file.close()

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
            file = open('itemsSold' , "a") # a for add mode
            file.write('Fanta' + "\n")# \n stands for new line
            file.close()

########################################### Treeview widget for receipt #################################################
        scroll_x = Scrollbar(receiptFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(receiptFrame, orient=VERTICAL)

        self.POSRecords = ttk.Treeview(receiptFrame, height=20, columns=("Item", "Quantity", "Price"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

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

##fish = StringVar
##chicken = StringVar
##soup = StringVar
##salad = StringVar
##fries = StringVar
##prawns = StringVar
##
##cottagePie = StringVar
##beefStew = StringVar
##cheeseDumplings = StringVar
##lasagne = StringVar
##riceWithVegetableCurry = StringVar
##
##cookies = StringVar
##iceCream = StringVar
##applePie = StringVar
##chocolateLavaCake = StringVar
##cinnamonRolls = StringVar
    
##coke = StringVar
##drPepper = StringVar
##fanta = StringVar
##pepsi = StringVar
##sprite = StringVar
#Python Program to search string in text using Tkinter

def starters():
    global screen9
    screen9 = Toplevel(screen)
    screen9.title("Starters")
    screen9.geometry("400x400")
    Label(screen9 , text = "Starters available to order").pack()

##    global fish
##    global fishEntry
##    global fishInfo
##    global chicken
##    global chickenEntry
##    global chickenInfo
##    global soup
##    global soupEntry
##    global soupInfo
##    global salad
##    global saladEntry
##    global saladInfo
##    global fries
##    global friesEntry
##    global friesInfo
##    global prawns
##    global prawnsEntry
##    global prawnsInfo

##    Label(screen9 , text = "Fish       £5").pack() # used screen9 at the front to specify where the label and button goes otherwise it would appear on all screens.
##    fishEntry = Entry(screen9 , textvariable = fish)
##    fishEntry.pack()
##    Label(screen9, text="Chicken       £4.50").pack()  
##    chickenEntry = Entry(screen9, textvariable=chicken)
##    chickenEntry.pack()
##    Label(screen9, text="Soup       £4").pack()  
##    soupEntry = Entry(screen9, textvariable=soup) # entry creates a textbox
##    soupEntry.pack()
##    Label(screen9, text="Salad       £5").pack()  
##    saladEntry = Entry(screen9, textvariable=salad)
##    saladEntry.pack()
##    Label(screen9,text="Fries       £3.50").pack()
##    friesEntry = Entry(screen9, textvariable=fries)
##    friesEntry.pack()
##    Label(screen9,text="Prawns       £7").pack() 
##    prawnsEntry = Entry(screen9, textvariable=prawns)
##    prawnsEntry.pack()
##    Label(screen9, text="").pack()  # leaves a line
    
    
    starterItem= ["Fish", "Chicken", "Soup", "Salad", "Fries", "Prawns"]
    starterItemList = Listbox(screen9, selectmode = MULTIPLE) #create pizza list
    starterItemList.pack()
    for item in starterItem:
        starterItemList.insert(0,item)

    def addItems():
        result= ""
        for item in starterItemList.curselection():
            result = result + str(starterItemList.get(item)) + "\n"
            Label1= Label(screen9)
            Label1.configure(text="Your selection" + "\n" + result)
            Label1.pack()
            Label(screen9, text="Added Successfully!", fg="blue", font=("Calibri", 11)).pack()  # prompts the user that their order has been added to the basket. fg stands for foreground.
    Button(screen9, text="Add to order", width=10, height=1, command=addItems).pack()                

##    fishInfo = fish.get(item)
##    chickenInfo = chicken.get(item)
##    soupInfo = soup.get(item)
##    saladInfo = salad.get(item)
##    friesInfo = fries.get(item)
##    prawnsInfo = prawns.get(item)
##
##    listOfFiles = os.listdir()
##    if fishInfo > 0 or chickenInfo >= 0 or soupInfo >= 0:
##        file2 = open(fishinfo, "r")
##        verification = file2.read().splitlines()
##
##    file2 = open(fishInfo , "w") # w for write mode
##    file2.write(fishInfo + "\n") # \n stands for new line
##    file2.write(chickenInfo)
##    file2.write(soupInfo)
##    file2.write(saladInfo)
##    file2.write(friesInfo)
##    file2.write(prawnsInfo)
##    file2.close() # this file stores usernames and passwords in a text file.


##    fishEntry.delete(0, END)
##    chickenEntry.delete(0, END)  # this clears the fields once the user has added the items successfully.
##    soupEntry.delete(0, END)
##    saladEntry.delete(0, END)
##    friesEntry.delete(0, END)
##    prawnsEntry.delete(0, END)

def mainCourse():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Main Course")
    screen10.geometry("300x250")
    Label(screen10 , text = "Main Course available to order").pack()

    mainCourse = ["Beef Stew", "Cheese Dumplings ", "Cottage Pie", "Lasagne", "Rice with Vegetable Curry"]
    mainCourseList = Listbox(screen10, selectmode = MULTIPLE) #create main course list
    mainCourseList.pack()
    for item in mainCourse:
        mainCourseList.insert(0,item)

    def addMainCourse():
        result= ""
        for item in mainCourseList.curselection():
            result = result + str(mainCourseList.get(item)) + "\n"
            Label2= Label(screen10)
            Label2.configure(text="Your selection" + "\n" + result)
            Label2.pack()
            Label(screen10, text="Added Successfully!", fg="blue", font=("Calibri", 11)).pack()  # prompts the user that their order has been added to the basket. fg stands for foreground.
    Button(screen10, text="Add to order", width=10, height=1, command=addMainCourse).pack()

def desserts():
    global screen11
    screen11 = Toplevel(screen)
    screen11.title("Desserts")
    screen11.geometry("300x250")
    Label(screen11 , text = "Desserts available to order").pack()

    desserts = ["Apple Pie", "Chocolate Lava Cake ", "Cinnamon Rolls", "Cookies", "Ice Cream"]
    dessertsList = Listbox(screen11, selectmode = MULTIPLE) #create desserts list
    dessertsList.pack()
    for item in desserts:
        dessertsList.insert(0,item)

    def addDesserts():
        result= ""
        for item in dessertsList.curselection():
            result = result + str(dessertsList.get(item)) + "\n"
            Label3= Label(screen11)
            Label3.configure(text="Your selection" + "\n" + result)
            Label3.pack()
            Label(screen11, text="Added Successfully!", fg="blue", font=("Calibri", 11)).pack()  # prompts the user that their order has been added to the basket. fg stands for foreground.
    Button(screen11, text="Add to order", width=10, height=1, command=addDesserts).pack()
##    Button (screen11 , text = "Cookies").pack()
##    Button (screen11 , text = "Ice Cream").pack()
##    Button (screen11 , text = "Apple Pie ").pack()
##    Button (screen11 , text = "Chocolate Lava Cake").pack()
##    Button (screen11 , text = "Cinnamon Rolls").pack()

def drinks():
    global screen12
    screen12 = Toplevel(screen)
    screen12.title("Drinks")
    screen12.geometry("300x250")
    Label(screen12 , text = "Drinks available to order").pack()

    drink= ["Coke", "Dr Pepper", "Fanta", "Pepsi", "Sprite"]
    drinkList = Listbox(screen12, selectmode = MULTIPLE) #create drinks list
    drinkList.pack()
    for item in drink:
        drinkList.insert(0,item)

    def addDrink():
        result= ""
        for item in drinkList.curselection():
            result = result + str(drinkList.get(item)) + "\n"
            Label2= Label(screen12)
            Label2.configure(text="Your selection" + "\n" + result)
            Label2.pack()
            Label(screen12, text="Added Successfully!", fg="blue", font=("Calibri", 11)).pack()  # prompts the user that their order has been added to the basket. fg stands for foreground.
    Button(screen12, text="Add to order", width=10, height=1, command=addDrink).pack()


def order():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Menu")
    screen8.geometry("300x250")
    Label (screen8 , text = "Order").pack()
    


    Button (screen8 , text = "Starters", command = starters).pack()
    Button (screen8 , text = "Main Course", command = mainCourse).pack()
    Button (screen8 , text = "Desserts", command = desserts).pack()
    Button (screen8 , text = "Drinks", command = drinks).pack()

    

mainScreen() #calling the function

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

        Frame5 =Frame(Frame3, bd=6, width=500,  height=280, padx=6,bg='white', relief=RIDGE)
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
    

        def addRecord():
            global count
            self.InventoryItems.insert(parent='', index='end', iid=count, text="",
                                       values=(productCodeEntry.get(), itemNameEntry.get(), quantityEntry.get(), reOrderLevelEntry.get()))
            count+=1
            productCodeEntry.delete(0,END)
            itemNameEntry.delete(0,END)#clearing the entry widgets 
            quantityEntry.delete(0,END)
            reOrderLevelEntry.delete(0,END)


        addRecord = Button(Frame42, text="Add Record", command= addRecord)
        addRecord.pack(pady=5)



        def removeAllItemsInInventory():
            for record in self.InventoryItems.get_children(): ##referring to the treeview widget
                self.InventoryItems.delete(record)
                

        removeAllItemsInInventory = Button(Frame42, text= "Remove All Items In Inventory",
                                           command= removeAllItemsInInventory)
        removeAllItemsInInventory.pack(pady=5)
        

        def removeAnItemFromInventory():
            selection= self.InventoryItems.selection()[0]
            self.InventoryItems.delete(selection)



        removeAnItemFromInventory = Button(Frame42, text= "Remove an item from Inventory",
                                           command= removeAnItemFromInventory)
        removeAnItemFromInventory.pack(pady=5)


        def removeAllSelectedItems():
            selection = self.InventoryItems.selection()
            for item in selection:
                self.InventoryItems.delete(selection)


        removeSelectedItems = Button(Frame42, text="Remove selected items", command=removeAllSelectedItems)
        removeSelectedItems.pack(pady=5)



        def updateRecord():
            selection= self.InventoryItems.focus()
            self.InventoryItems.item(selection, text="", values= (productCodeEntry.get(),
                                                                          itemNameEntry.get(), quantityEntry.get(), reOrderLevelEntry.get()))
            productCodeEntry.delete(0,END)
            itemNameEntry.delete(0,END)#clearing the entry widgets 
            quantityEntry.delete(0,END)
            reOrderLevelEntry.delete(0,END)


        updateRecord = Button(Frame42, text="Update Records", command=updateRecord)
        updateRecord.pack(pady=5)




        def selectRecord():
            productCodeEntry.delete(0,END)
            itemNameEntry.delete(0,END)#clearing the entry widgets 
            quantityEntry.delete(0,END)
            reOrderLevelEntry.delete(0,END)
            selection= self.InventoryItems.focus()
            values = self.InventoryItems.item(selection, 'values')
##            temporary.config(text=values)
            productCodeEntry.insert(0, values[0])
            itemNameEntry.insert(0, values[1])
            quantityEntry.insert(0, values[2])
            reOrderLevelEntry.insert(0, values[3])


        selectRecord = Button(Frame42, text="Select Record", command=selectRecord)
        selectRecord.pack(pady=5)

        temporary= Label(Frame42, text="")
        temporary.pack(pady=5)




##        def alertInventory():
##            if quantity1.get() <= reOrderLevel1.get():
##                alert= tkinter.messagebox.showinfo(title='Alert!', message='Cookie dough is running low on stock!')
# tried to implement low stock alerts like in apicbase software however failed to do so as i could not get it to identify each items's quantity level. screenshot attached at 18)

##        ##########variables for frame43##############
##        tax = StringVar()
##        subtotal = StringVar()
##        total = StringVar()
##
##        #################frame43#############
##        self.lblTax = Label(Frame43, font=('arial', 18, 'bold'), text="Tax", padx=14, pady=4, bg='white')
##        self.lblTax.grid(row=0, column=0,sticky=W)
##        self.txtTax= Entry(Frame43, textvariable=tax, bd=2, width=14, font=('arial', 9, 'bold'), justify=LEFT)
##        self.txtTax.grid(row=1, column=0,padx=23, pady=5)
##
##        self.lblSubTotal = Label(Frame43, font=('arial', 18, 'bold'), text="SubTotal", padx=14, pady=4, bg='white')
##        self.lblSubTotal.grid(row=0, column=1,sticky=W)
##        self.txtSubTotal= Entry(Frame43, textvariable=subtotal, bd=2, width=14, font=('arial', 9, 'bold'), justify=LEFT)
##        self.txtSubTotal.grid(row=1, column=1,padx=23, pady=5)
##
##        self.lblTotal = Label(Frame43, font=('arial', 18, 'bold'), text="Total", padx=14, pady=4, bg='white')
##        self.lblTotal.grid(row=0, column=2,sticky=W)
##        self.txtTotal= Entry(Frame43, textvariable=tax, bd=2, width=14, font=('arial', 9, 'bold'), justify=LEFT)
##        self.txtTotal.grid(row=1, column=2,padx=23, pady=5)
        
        ####################variables for frame5###############
        checkFreezer=IntVar()
        checkExpiryDates = IntVar()
        checkDishes=IntVar()
        checkHygiene=IntVar()

        ####functions for frame5#########
        def checksFreezer():
            if checkFreezer.get() == 1:
                self.txtInventoryReceipt.insert(END, "Freezer is checked\n")
            elif checkFreezer.get() == 0:
                self.txtInventoryReceipt.delete("1.0", END)

        def checksExpiryDates():
            if checkExpiryDates.get() == 1:
                self.txtInventoryReceipt.insert(END, "None of the items have expired\n")
            elif (checkExpiryDates.get() == 0):
                self.txtInventoryReceipt.delete("1.0", END)

        def checksDishes():
            if checkDishes.get() ==1:
                self.txtInventoryReceipt.insert(END, "Equipment is maintained\n")
            elif (checkDishes.get() ==0):
                self.txtInventoryReceipt.delete("1.0", END)

        def checksHygiene():
            if checkHygiene.get() ==1:
                self.txtInventoryReceipt.insert(END, "Hygiene is maintained\n")
            elif (checkHygiene.get() ==0):
                self.txtInventoryReceipt.delete("1.0", END)

        
### frame5#########

        self.chkCheckFreezer = Checkbutton(Frame5, text= "Check Freezer", variable=checkFreezer, onvalue=1, offvalue=0,
                                           font=('arial',16,'bold'),bg='white', command= checksFreezer).grid(row=0, sticky=W)
        self.chkCheckExpiryDates = Checkbutton(Frame5, text= "Check Expiry Dates", variable=checkExpiryDates, onvalue=1, offvalue=0,
                                           font=('arial',16,'bold'),bg='white', command=checksExpiryDates).grid(row=1, sticky=W)
        self.chkCheckDishes =  Checkbutton(Frame5, text= "Check Dishes", variable=checkDishes, onvalue=1, offvalue=0,
                                           font=('arial',16,'bold'),bg='white', command=checksDishes).grid(row=2, sticky=W)
        self.chkCheckHygiene =  Checkbutton(Frame5, text= "Check Hygiene", variable=checkHygiene, onvalue=1, offvalue=0,
                                           font=('arial',16,'bold'),bg='white', command=checksHygiene).grid(row=3, sticky=W)
        


##        
##        #############################################Labels Frame5##################
##        self.lblOpenAccount = Label(Frame5, font=('arial', 18, 'bold'), text="Account Opened:",padx=2, pady=2, bg='white')
##        self.lblOpenAccount.grid(row=0,column=0, sticky=W)
##
##        self.cboOpenAccount = ttk.Combobox(Frame5, textvariable=openAccount, state='readonly',
##                                           font=('arial', 18, 'bold'), width=19) #cbo stands for combobox
##        self.cboOpenAccount['value'] =("", "Select an option", "Yes", "No")
##        self.cboOpenAccount.current(0)
##        self.cboOpenAccount.grid(row=0,column=1,pady=2)
##        
##
##        self.lblDateOfApp = Label(Frame5, font=('arial', 18, 'bold'), text="Date of App:",padx=2, pady=2, bg='white')
##        self.lblDateOfApp.grid(row=1,column=0, sticky=W)
##
##        self.cboDateOfApp = ttk.Combobox(Frame5, textvariable=dateOfApp, state='readonly',
##                                           font=('arial', 18, 'bold'), width=19) #cbo stands for combobox
##        self.cboDateOfApp['value'] =("", "Select an option", "A", "B")
##        self.cboDateOfApp.current(0)
##        self.cboDateOfApp.grid(row=1,column=1, pady=2)
##
##        
##
##        self.lblNextCreditReview = Label(Frame5, font=('arial', 18, 'bold'), text="Next Credit Review:",padx=2, pady=2, bg='white')
##        self.lblNextCreditReview.grid(row=2,column=0, sticky=W)
##
##        self.cboNextCreditReview = ttk.Combobox(Frame5, textvariable=nextCreditReview, state='readonly',
##                                           font=('arial', 18, 'bold'), width=19) #cbo stands for combobox
##        self.cboNextCreditReview['value'] =("", "Select an option", "A", "B")
##        self.cboNextCreditReview.current(0)
##        self.cboNextCreditReview.grid(row=2,column=1, pady=2)
##
##        
##
##        self.lblLastCreditReview = Label(Frame5, font=('arial', 18, 'bold'), text="Last Credit Review:",padx=2, pady=2, bg='white')
##        self.lblLastCreditReview.grid(row=3,column=0, sticky=W)

##        self.cboLastCreditReview = ttk.Combobox(Frame5, textvariable=lastCreditReview, state='readonly',
##                                           font=('arial', 18, 'bold'), width=19) #cbo stands for combobox
##        self.cboLastCreditReview['value'] =("", "Select an option", "A", "B")
##        self.cboLastCreditReview.current(0)
##        self.cboLastCreditReview.grid(row=3,column=1, pady=2)
##
##
##        self.lblDateOfReview = Label(Frame5, font=('arial', 18, 'bold'), text="Date Of Review:",padx=2, pady=2, bg='white')
##        self.lblDateOfReview.grid(row=4,column=0, sticky=W)
##
##        self.cboDateOfReview = ttk.Combobox(Frame5, textvariable=dateOfReview, state='readonly',
##                                           font=('arial', 18, 'bold'), width=19) #cbo stands for combobox
##        self.cboDateOfReview['value'] =("", "Select an option", "A", "B")
##        self.cboDateOfReview.current(0)
##        self.cboDateOfReview.grid(row=4,column=1,pady=2)
        
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


#################################Staff module############################
from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
import os
import datetime
from PIL import ImageTk, Image
from tkcalendar import*

class Staff:

    def __init__(self,staff):
        self.staff = staff
        self.staff.title("Staff")
        self.staff.geometry("1350x800+0+0")
        self.staff.configure(background='white')
###############################Frames############################

        Frame1 = Frame(self.staff, bd=15, bg='white', width=675, height=700, relief = RIDGE)
        Frame1.pack(side=LEFT) ##for staff info label 

        Frame2 = Frame(self.staff, bd=15, bg='white', width=675, height=700, relief = RIDGE)
        Frame2.pack(side=RIGHT) ##for staff payroll


        employeeInformation = Label(Frame1, font=('arial', 40, 'bold'), text="Employee Information ", relief=GROOVE, bd=10, bg="Dark Gray", fg="Black")
        employeeInformation.grid(row=0,column=0)

        employeePayroll = Label(Frame2, font=('arial', 40, 'bold'), text="Employee Payroll ", relief=GROOVE, bd=10, bg="Dark Gray", fg="Black")
        employeePayroll.grid(row=0,column=0)

        ################STAFF PAYROLL Frame2##########

        ###########Labels###
        fullName = Label(Frame2, text="Full Name", font=('arial', 16, 'bold'), bd=5, fg='black',
                          bg='white', justify=LEFT)
        fullName.grid(row=1, column=0)

        address = Label(Frame2, text="Address", font=('arial', 16, 'bold'), bd=5, fg='black',
                          bg='white')
        address.grid(row=2, column=0)

        phoneNumberLabel = Label(Frame2, text="Phone Number", font=('arial', 16, 'bold'), bd=5, fg='black',
                          bg='white')
        phoneNumberLabel.grid(row=3, column=0)

        hoursWorked = Label(Frame2, text="Hours Worked", font=('arial', 16, 'bold'), bd=5, fg='black',
                          bg='white')
        hoursWorked.grid(row=4, column=0)

        ratePerHour = Label(Frame2, text="Rate Per Hour", font=('arial', 16, 'bold'), bd=5, fg='black',
                          bg='white')
        ratePerHour.grid(row=5, column=0)

        tax = Label(Frame2, text="Tax", font=('arial', 16, 'bold'), bd=5, fg='black',
                          bg='white')
        tax.grid(row=6, column=0)

        overTime= Label(Frame2, text="Over time", font=('arial', 16, 'bold'), bd=5, fg='black',
                          bg='white')
        overTime.grid(row=7, column=0)

        grossPay= Label(Frame2, text="Gross Pay", font=('arial', 16, 'bold'), bd=5, fg='black',
                          bg='white')
        grossPay.grid(row=8, column=0)

        netPay= Label(Frame2, text="Net Pay", font=('arial', 16, 'bold'), bd=5, fg='black',
                          bg='white')
        netPay.grid(row=9, column=0)

        ##################variables for staff payroll#####
        fullName = StringVar()
        address = StringVar()
        phonenumber= StringVar()
        hoursWorked= StringVar()
        ratePerHour = StringVar()
        tax = StringVar()
        overTime = StringVar()
        grossPayment = StringVar()
        netPay = StringVar()
        payslip =StringVar()
        

        ###################Entry################
        fullNameEntry = Entry(Frame2, font=('arial', 16, 'bold'), textvariable= fullName, bd=2, justify=RIGHT,
                         width=24)
        fullNameEntry.grid(row=1, column=1)

        addressEntry = Entry(Frame2, font=('arial', 16, 'bold'), textvariable= address, bd=2, justify=RIGHT,
                         width=24)
        addressEntry.grid(row=2, column=1)

        phonenumberEntry = Entry(Frame2, font=('arial', 16, 'bold'), textvariable= phonenumber, bd=2, justify=RIGHT,
                         width=24)
        phonenumberEntry.grid(row=3, column=1)

        hoursWorkedEntry = Entry(Frame2, font=('arial', 16, 'bold'), textvariable= hoursWorked, bd=2, justify=RIGHT,
                         width=24)
        hoursWorkedEntry.grid(row=4, column=1)

        ratePerHourEntry = Entry(Frame2, font=('arial', 16, 'bold'), textvariable= ratePerHour, bd=2, justify=RIGHT,
                         width=24)
        ratePerHourEntry.grid(row=5, column=1)

        rateOfTaxEntry = Entry(Frame2, font=('arial', 16, 'bold'), textvariable= tax, bd=2, justify=RIGHT,
                         width=24)
        rateOfTaxEntry.grid(row=6, column=1)

        overTimeBonusEntry = Entry(Frame2, font=('arial', 16, 'bold'), textvariable= overTime, bd=2, justify=RIGHT,
                         width=24)
        overTimeBonusEntry.grid(row=7, column=1)

        grossPayEntry = Entry(Frame2, font=('arial', 16, 'bold'), textvariable= grossPayment, bd=2, justify=RIGHT,
                         width=24)
        grossPayEntry.grid(row=8, column=1)

        netPaymentEntry = Entry(Frame2, font=('arial', 16, 'bold'), textvariable= netPay, bd=2, justify=RIGHT,
                         width=24)
        netPaymentEntry.grid(row=9, column=1)

        #############payslip########
        payslip = Label(Frame2, textvariable = payslip,font=('arial', 13, 'bold'), bd=5, fg='black',
                          bg='white')
        payslip.grid(row=10, column=0)

        payslipText = Text(Frame2, height=20, width=50, bd=16, font=('arial', 10, 'bold'), fg="black", bg="white")
        payslipText.grid(row=11, column=0)

        ##################functions for buttons############
        def weeklyWages():
            payslipText.delete("1.0", END)
            numberOfHoursPerWeek = float(hoursWorked.get())
            ratePerHourPerWeek = float(ratePerHour.get())

            wagesDue = numberOfHoursPerWeek * ratePerHourPerWeek
            wage = str('%.2f' % wagesDue)
            grossPayment.set(wage)

            rateOfTax = wagesDue * 0.12
            taxed = str('%.2f' % rateOfTax)
            tax.set(taxed)

            paymentNet = wagesDue - rateOfTax
            netPayment = str('%.2f' % paymentNet)
            netPay.set(netPayment)

            if numberOfHoursPerWeek >= 35:
                overTimeHours = (numberOfHoursPerWeek -35) + ratePerHourPerWeek *1.2
                overTimeBonus = str('%.2f' % overTimeHours)
                overTime.set(overTimeBonus)
                
            elif numberOfHoursPerWeek < 35 :
                payOverTime = (numberOfHoursPerWeek - 35) + ratePerHourPerWeek *1.2
                overTimeHours = str('%.2f' % payOverTime)
                overTime.set(overTimeHours)
            return

        

        def reset():
            fullName.set("")
            address.set("")
            phonenumber.set("")
            hoursWorked.set("")
            ratePerHour.set("")
            tax.set("")
            overTime.set("")
            grossPayment.set("")
            netPay.set("")
            payslipText.delete("1.0", END)


        def viewPayslip():
            payslipText.delete("1.0", END)
            payslipText.insert(END, "\t\tPay Slip\n\n")
            payslipText.insert(END, "Full Name :\t\t" + fullName.get() + "\n\n")
            payslipText.insert(END, "Address :\t\t" + address.get() + "\n\n")
            payslipText.insert(END, "Phone Number :\t\t" + phonenumber.get() + "\n\n")
            payslipText.insert(END, "Hours Worked :\t\t" + hoursWorked.get() + "\n\n")
            payslipText.insert(END, "Rate per Hour :\t\t" + ratePerHour.get() + "\n\n")
            payslipText.insert(END, "Tax :\t\t" + tax.get() + "\n\n")
            payslipText.insert(END, "Over Time Bonus :\t\t" + overTime.get() + "\n\n")
            payslipText.insert(END, "Gross Pay :\t\t" + grossPayment.get() + "\n\n")
            payslipText.insert(END, "Net Pay :\t\t" + netPay.get() + "\n\n")

        def savePayslip():
            file = open(fullName.get(), "w")##write mode
            file.write("Full Name :\t\t" + fullName.get() + "\n\n")
            file.write("Address :\t\t" + address.get() + "\n\n")
            file.write("Phone Number :\t\t" + phonenumber.get() + "\n\n")
            file.write("Hours Worked :\t\t" + hoursWorked.get() + "\n\n")
            file.write("Rate per Hour :\t\t" + ratePerHour.get() + "\n\n")
            file.write("Tax :\t\t" + tax.get() + "\n\n")
            file.write("Over Time Bonus :\t\t" + overTime.get() + "\n\n")
            file.write("Gross Pay :\t\t" + grossPayment.get() + "\n\n")
            file.write("Net Pay :\t\t" + netPay.get() + "\n\n")
            file.close()
            
            

        def exit():
            answer = tkinter.messagebox.askyesno("Confirm Exit", "Are you sure to exit?")
            if answer == 1:
                staff.destroy()
            else:
                return

        ##############Buttons#########
        weeklyWages = Button(Frame2, text='Weekly Wages', padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief="groove", width=14, fg="black",
                              bg="white", command=weeklyWages).grid(row=10, column=1)

        reset = Button(Frame2, text= "Reset", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief="groove", width=14, fg="black",
                       bg="white", command= reset).grid(row=10, column=2)

        paySlip = Button(Frame2, text= "View Payslip", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief="groove", width=14, fg="black",
                       bg="white", command= viewPayslip).grid(row=11, column=1)

        exit = Button(Frame2, text="Exit", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=14, fg='black',
                      bg='white', command=exit).grid(row=11, column=2)

        savePayslip = Button(Frame2, text="Save Payslip", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=14, fg='black',
                      bg='white', command=savePayslip).grid(row=12, column=1)

###################################STAFF INFO########################################
##        addnewprofile
##        currentusers- clicking on one user opens up the window edit then click ok to save

        ##############variables###########
        employeeID = StringVar()
        name = StringVar()
        email = StringVar()
        costPerHour = StringVar()
        phoneNumber = StringVar()
        address= StringVar()
        gender = StringVar()
        userType =StringVar()
####################################FUNCTIONS FOR BUTTONS#############
        def addNewEmployee():
            global screen13
            screen13 = Toplevel(staff)
            screen13.title("Add new employee")
            screen13.geometry("500x500")

            EmployeeID = Label(screen13, text="Employee ID", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white').grid(row=0, column=0)
            employeeIDEntry = Entry(screen13,bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white', textvariable= employeeID).grid(row=0, column=1)

            Name = Label(screen13, text="Name", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white').grid(row=1, column=0)
            nameEntry = Entry(screen13, bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white', textvariable=name).grid(row=1, column=1)

            Email= Label(screen13, text="Email", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white').grid(row=2, column=0)
            emailEntry = Entry(screen13,bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white', textvariable=email).grid(row=2, column=1)

            CostPerHour = Label(screen13, text="Wage Per Hour", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white').grid(row=3, column=0)
            costPerHourEntry = Entry(screen13,bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white', textvariable=costPerHour).grid(row=3, column=1)

            PhoneNumber = Label(screen13, text="Phone Number", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white').grid(row=4, column=0)
            phoneNumberEntry = Entry(screen13,bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white', textvariable=phoneNumber).grid(row=4, column=1)

            Address = Label(screen13, text="Address", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white').grid(row=5, column=0)
            addressEntry = Entry(screen13,bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white', textvariable=address).grid(row=5, column=1)

            Gender = Label(screen13, text="Gender", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white').grid(row=6, column=0)
            genderComboBox = ttk.Combobox(screen13,font=('arial', 10, 'bold'), width=18, state='readonly',
                                          textvariable=gender)
            genderComboBox['value'] = ('', 'Male', 'Female', 'Other')
            genderComboBox.current(0)
            genderComboBox.grid(row=6, column=1)

            UserType = Label(screen13, text="User Type", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=20, fg='black',
                      bg='white').grid(row=7, column=0)
            userTypeComboBox = ttk.Combobox(screen13,font=('arial', 10, 'bold'), width=18, state='readonly',
                                          textvariable=userType)
            userTypeComboBox['value'] = ('', 'Admin', 'Manager', 'Team Member')
            userTypeComboBox.current(0)
            userTypeComboBox.grid(row=7, column=1)



            def addEmployee():
                if employeeID.get() == 0 or name.get()=='' or email.get() =='' or costPerHour.get() == '' or phoneNumber.get() == ''or address.get()=='' or gender.get() =='' or userType.get()=='' :#if fields are empty
                    answer = tkinter.messagebox.showinfo(title="Error", message="All fields are required")
                elif len(employeeID.get())!= 5 :
                    answer = tkinter.messagebox.showinfo(title="Error", message="Employee ID must be equal to 5 characters")
                else:
                    self.txtemployeeDetails.insert(END, employeeID.get()+ "\n")
                    self.txtemployeeDetails.insert(END,name.get()+ "\n")
                    self.txtemployeeDetails.insert(END,email.get()+ "\n")
                    self.txtemployeeDetails.insert(END,costPerHour.get()+ "\n")
                    self.txtemployeeDetails.insert(END,phoneNumber.get()+ "\n")
                    self.txtemployeeDetails.insert(END,address.get()+ "\n")
                    self.txtemployeeDetails.insert(END,gender.get()+ "\n")
                    self.txtemployeeDetails.insert(END,userType.get()+ "\n")
                    file = open(name.get() , "w")
                    file.write(employeeID.get()+ "\n" )
                    file.write(name.get()+"\n")
                    file.write(email.get()+"\n")
                    file.write(costPerHour.get()+"\n")
                    file.write(phoneNumber.get()+"\n")
                    file.write(address.get()+"\n")
                    file.write(gender.get()+"\n")
                    file.write(userType.get()+"\n")
                    file.close()


                    def currentUserDetails():
                        global screen14
                        screen14=Toplevel(screen13)
                        screen14.title("Staff Details")
                        screen14.geometry("350x350")
                        file = open(name.get(), "r") #when a new employee was added its file was saved which is retrieved at this stage to get details.
                        details= str(file.read())
                        detailsLabel = Label(screen14, text=details)
                        detailsLabel.grid()
                        

                    currentEmployee = Label(Frame1, text="Current Employees:")
                    currentEmployee.grid()
                    user = Button(Frame1, text=name.get(),command=currentUserDetails)
                    user.grid()
                    

            def printStaffDetails():
                b= self.txtemployeeDetails.get("1.0", "end-1c")
                print(b)
                filename = tempfile.mktemp(".txt")
                open(filename, "w").write(b)
                os.startfile(filename, "print")

            def reset():
                employeeID.set("")
                name.set("")
                email.set("")
                costPerHour.set("")
                phoneNumber.set("")
                address.set("")
                gender.set("")
                userType.set("")
                self.txtemployeeDetails.delete("1.0", END)

            def exit():
                answer = tkinter.messagebox.askyesno("Confirm Exit", "Are you sure to exit Add new Employee?")
                if answer == 1:
                    screen13.destroy()
                else:
                    return
                
                    

            AddEmployee = Button(screen13, text="Add Employee", font=('arial', 12, 'bold'), fg='black', bg='white', command=addEmployee)
            AddEmployee.grid (row=10, column=0)

            print = Button(screen13, text="Print", font=('arial', 12, 'bold'), fg='black', bg='white', command=printStaffDetails)
            print.grid (row=10, column=1)

            reset = Button(screen13, text="Reset", font=('arial', 12, 'bold'), fg='black', bg='white',command=reset)
            reset.grid (row=11, column=0)

            exit = Button(screen13, text="Exit", font=('arial', 12, 'bold'), fg='black', bg='white',command=exit)
            exit.grid (row=11, column=1)

            self.txtemployeeDetails = Text(screen13,font=('arial', 12, 'bold'), fg='black', bg='white', width=50, height=13)
            self.txtemployeeDetails.grid()
            employeeDetailsText = StringVar()




        addNewprofile = Button(Frame1, text="Add New Employee", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=14, fg='black',
                      bg='white', command=addNewEmployee).grid()
        

#############################################STAFF TIMETABLE ############################################################

        def staffTimetable():
            global screen15
            screen15 = Toplevel(Frame1)
            staffCalendar = Calendar(screen15,selectmode="day")#selectmode= when you click an individual date/day gets selected. could change it to month, it would select the whole month.
            staffCalendar.pack(fill = "both", expand=True)

            retrieveAvailability = open(usernameInfo + "Timetable.txt", "r")
        timetable = Button(Frame1, text="Staff timetable" ,padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=14, fg='black',
                           bg='white', command=staffTimetable).grid()



        ################################### ANALYTICS AND REPORT #########################
        def analytics():
                    #counter is a built in class in python that counts how many times an
            #item has appeared in a list.

            plt.style.use('fivethirtyeight') ##style used for graph

            #this section of the code takes in two data sets as inputs and plots them against
            # one another. plt is the module that graphs the inputs. xlabel and ylabel refer to the labels
            # shown on the x and y axis. title command refers to the title of the graph. without
            # plt.show() command the graph would not be displayed on screen. legend is used to
            # differentiate which data refers to which graph and label indicates the data.


            ##################staff late matplotlib############
            ##here it is opening the file and analysing the number of times the staff member's name is mentioned to analyse the number
            #of times they were late. 

            with open('staffLate.txt') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                lateCounter = Counter()

                for row in csv_reader:
                    lateCounter.update(row['staffLate'].split(';'))

                    
            staff = []
            numberOfLates =[]
               
            ##print(lateCounter)
            for item in lateCounter.most_common(11):#print(lateCounter.most_common(1)) returns the staff with most number of lates
                staff.append(item[0])# this line retrieves the staff name based on the most lates.
                               #index 0 as staff name is before their no. of lates in the tuple that lateCounter prints/gets.
                numberOfLates.append(item[1]) #at index 1 is the number of lates in tuple
                
            print(staff)
            print(numberOfLates)


            plt.bar(staff, numberOfLates)
            plt.xlabel('Staff Member')
            plt.ylabel('Number of lates')
            plt.title('Number of times a staff member is late this week')
            plt.show()

            ###########top ten items sold#################
            ##here it is opening the file and analysing the number of items the item was purchased. 
            with open('itemsSold.txt') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                tenbestSellingItemsCounter = Counter() #this reads the data from the file.

            ##    row = next(csv_reader)
            ##    print(row['itemsSold'].split(';'))#this retrieves the list of languages but only from a single row.
                

                for row in csv_reader: #this retrieves the list of languages from all rows.
                    tenbestSellingItemsCounter.update(row['itemsSold'].split(';'))

            bestSellingItems = []
            numberOfTimesSold =[]
                    
            for item in tenbestSellingItemsCounter.most_common(11):
                bestSellingItems.append(item[0])
                numberOfTimesSold.append(item[1])

            print(bestSellingItems)
            print(numberOfTimesSold)

            plt.barh(bestSellingItems, numberOfTimesSold) #barh refers to horizontal bar chart. x-axis labels are transferred to y axis and vice versa.
            plt.ylabel('Menu Items')
            plt.xlabel('Number of times Bought')
            plt.title('Top ten best selling items of the restaurant')
            plt.tight_layout()
            plt.show()

            
        analyticsButton = Button(Frame1, text="Analytics and report", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=14, fg='black',
                                   bg='white', command=analytics).grid()


        
if __name__== '__main__':
    staff=Tk()
    application=Staff(staff)
    staff.mainloop()

#my advice(can be completely ignored if wished)- create separate buttons for inventory, staff, order and analytics tab
# sir recommended SQLite for databases. 

#https://www.youtube.com/watch?v=H3Ws-OPyMCQ&list=PL1FgJUcJJ03sm4WuVCPMbT0RIf2uMmoAj&index=6 - watch this to learn how to create drop down menu
# https://www.youtube.com/watch?v=VGIK3P9gNkM&list=PL1FgJUcJJ03sm4WuVCPMbT0RIf2uMmoAj&index=11 - watch this to learn how to create tabs for inventory, menu and backoffice.
# https://www.youtube.com/watch?v=3ssnpvRqVEw&list=PL1FgJUcJJ03sm4WuVCPMbT0RIf2uMmoAj&index=13 - watch this to learn how to create menu item events , i.e. sub menus. 
#https://www.youtube.com/watch?v=rtR5wHXPKZ4&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=118- in inventory add item, delete item
# https://www.youtube.com/watch?v=lKiNlSs_cms&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=121- watch from here 

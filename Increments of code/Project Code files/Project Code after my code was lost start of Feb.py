from tkinter import*  # * imports everything from tkinter
import os  # imports operating system
from tkinter import messagebox
import tempfile


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
            pay = tkinter.messagebox.showinfo(title='Payment Successful!', message='Enjoy your meal')
		

        
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

            checkout = Button(pizza, text="Checkout")
            checkout.grid(row=6,column=0)

            def deleteItem():
                pizzaList.delete(0,7)
                

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
        self.inventory.confirgure(background='white')
        
#######################FRAMES########################

        InventoryFrame = Frame(self.inventory, bd=20, bg='white', width=1350, height=700, relief=RIDGE)
        InventoryFrame.grid()

        Frame4 = Frame(InventoryFrame, bd=10, bg='white', width=750, height=600, padx=10, relief=RIDGE)
        Frame4.pack(side=LEFT)

        Frame5 = Frame(InventoryFrame, bd=10, bg='white', width=750, height=600, padx=10, relief=RIDGE)
        Frame5.pack(side=RIGHT)

        #######################BUTTons, labels,  ########################
        

        

###my advice(can be completely ignored if wished)- create separate buttons for inventory, staff, order and analytics tab
# sir recommended SQLite for databases. 

#https://www.youtube.com/watch?v=H3Ws-OPyMCQ&list=PL1FgJUcJJ03sm4WuVCPMbT0RIf2uMmoAj&index=6 - watch this to learn how to create drop down menu
# https://www.youtube.com/watch?v=VGIK3P9gNkM&list=PL1FgJUcJJ03sm4WuVCPMbT0RIf2uMmoAj&index=11 - watch this to learn how to create tabs for inventory, menu and backoffice.
# https://www.youtube.com/watch?v=3ssnpvRqVEw&list=PL1FgJUcJJ03sm4WuVCPMbT0RIf2uMmoAj&index=13 - watch this to learn how to create menu item events , i.e. sub menus.
###13 mins

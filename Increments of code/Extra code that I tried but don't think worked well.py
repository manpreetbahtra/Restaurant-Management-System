def validateAllFields():
    if usernameInfo == "":  # fields can't be empty
        Label(screen5, text="Please enter username to proceed").pack()
    elif len(usernameInfo) < 5:
        messagebox.showinfo("The username has to be at least 5 characters")
    elif password.get() == "":  # fields can't be empty
        messagebox.showinfo("Please enter password to proceed")
    elif confirmPassword.get() == "":  # fields can't be empty
        messagebox.showinfo("Please confirm password to proceed")
    elif password.get() != confirmPassword.get():
        messagebox.showinfo("Password does not match!")
    else:
        messagebox.showinfo("User registered successfully!!")


def validatePassword(passwordVerify):
    specialSymbols = ['!', '£', '%', '*', '@', '#']
    val = True
    if len(passwordVerify) < 8 :
        print("Password length should be at least 8")
        val = False

    if len(passwordVerify) > 13 :
        print ("Password length should not be greater than 13")
        val = False

    if not any(char.isdigit() for char in passwordVerify):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwordVerify):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwordVerify):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in specialSymbols for char in passwordVerify):
        print('Password should have at least one of the symbols ! £ % * @ #')
        val = False
    if val:
        return val

validatePassword(passwordVerify)


# how to create a dropdown menu
self.lblPaymentMethod = Label(changeFrame, font=('arial', 14, 'bold'), text="Payment Method", bd=5)
self.lblPaymentMethod.grid(row=0,column=0, sticky=W, padx=5)
self.cboPaymentMethod = ttk.Combobox(changeFrame, font=('arial', 14, 'bold'), justify= RIGHT, width =24, state='readonly',
                                     textvariable=choice) # combobox is for dropdown menu
self.cboPaymentMethod['value'] = ('', 'Cash', 'Visa Card', 'Master Card')
self.cboPaymentMethod.current(0)
self.cboPaymentMethod.grid(row=0,column=1, sticky=W, padx=5)


##############################################SEARCH AND AUTOFILL FUNCTION FOR MENU#############################################
        searchLabel = Label(root, text="Search for item", font = ("arial", 15)) #creating a label
        searchLabel.grid(pady=20)

        searchEntry = Entry(root, font=("arial",20))#creating an entry box 
        searchEntry.grid()

        searchList = Listbox(root, width=50) # create a listbox
        searchList.grid(pady=40)

        listOfItems = ["chips", "vegBurger", "cinnamonRolls", "pepsi", "coke", "beefStew"] # list of items in menu

        def update(data):
            searchList.delete(0, END)

            for searchItem in data:
                searchList.insert(END, searchItem)

        def fillout(event): #update entry box with listbox clicked
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

        searchList.bind("<<ListboxSelect>>", fillout)
        searchEntry.bind("<KeyRelease>", check )# check to see what we just typed in the search list

        # searching for one of the items displays all the items avaialble to be searched.
####how to create add item,checkout, delete button

        def pizza():
            pizza=Tk()
            pizza.geometry("600x500")
            pizza.title("Order Pizza")

            pizzaToppings = ["Pizza Sauce", "BBQ Sauce", "Cheese", "Gluten Free Cheese", "Vegan Cheese", "Pepperoni", "Sausage", "Mushrooms"]
            pizzaList = Listbox(pizza, selectmode=MULTIPLE) #create pizza list
            pizzaList.grid(row=0, column=0)

            for topping in pizzaToppings:
                pizzaList.insert(0,topping)


            addItem = Button(pizza, text="Add Items")
            addItem.grid(row=5, column=0) # https://www.youtube.com/watch?v=-Vax2_i8ucQ 10 mins

            checkout = Button(pizza, text="Checkout")
            checkout.grid(row=6,column=0)

            delete = Button(pizza, text="Delete Item")
            delete.grid(row=7,column=0)


            pizza.mainloop()
            
##search function for menu items
searchFrame = Frame(screen8)
    Label(searchFrame,text='Item to find:').pack(side=LEFT)
    edit = Entry(searchFrame)
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    edit.focus_set()
    butt = Button(searchFrame,text='Find')
    butt.pack(side=RIGHT)
    searchFrame.pack(side=TOP)


    text = Text(screen8)
    text.insert('1.0','''Type your text here''')
    text.pack(side=BOTTOM)

    def find():
            text.tag_remove('found', '1.0', END)
            s = edit.get()
            if s:
                idx = '1.0'
                while 1:
                    idx = text.search(s, idx, nocase=1,stopindex=END)
                    if not idx: break
                    lastidx = '%s+%dc' % (idx, len(s))
                    text.tag_add('found', idx, lastidx)
                    idx = lastidx
                text.tag_config('found', foreground='red')
            edit.focus_set()
    butt.config(command=find)




            

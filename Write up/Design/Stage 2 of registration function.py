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

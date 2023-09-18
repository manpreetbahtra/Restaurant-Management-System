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

mainScreen()

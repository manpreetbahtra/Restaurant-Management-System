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

    listOfFiles = os.listdir()
    if username1 in listOfFiles:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            Label(screen2, text="Login successful").pack()
            # 1st outcome- username and password correct
        else:
            Label(screen2, text="Password Not Recognised").pack()
            # 2nd outcome- username correct password incorrect
    else:
        Label(screen2, text="User Not Found").pack()# username not found.


def mainScreen():
    global screen # because we want to access it from another function. 
    screen = Tk()
    screen.title("Restaurant Management System")
    screen.geometry("900x750") # screen size
    Label(text = "Restaurant Management System" , bg = "grey" , width = "300", height = "2" , font = ("Calibri" , 14)).pack()
    #header label. bg stands for background..pack() organises widgets
    Label(text = "").pack()
    # leaves a line # Label and Button have to be capital otherwise not recognised
    Button (text = "Login" , height = "2" , width = "30" , command = login).pack()
    #Buttons for login and register
    Label(text = "").pack()
    Button (text = "Register" , height = "2" , width = "30", command = register).pack()
    
    screen.mainloop() #execution of python commands halts here.

mainScreen() 

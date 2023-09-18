#################################Staff module############################
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
from PIL import ImageTk, Image
from tkcalendar import*
from tkinter import*  # * imports everything from tkinter
import os  # imports operating system
import tempfile
import csv
from collections import Counter 
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

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

            
        analyticsButton = Button(Frame1, text="Analytics and report", padx=5, pady=3, bd=2, font=('arial', 10, 'bold'), relief='groove', width=14, fg='black',
                                   bg='white', command=analytics).grid()


        
if __name__== '__main__':
    staff=Tk()
    application=Staff(staff)
    staff.mainloop()

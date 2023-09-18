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

if __name__== '__main__':
    staff=Tk()
    application=Staff(staff)
    staff.mainloop()


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


        
if __name__== '__main__':
    staff=Tk()
    application=Staff(staff)
    staff.mainloop()


from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from datetime import datetime
import time;
import random


class customer:



    def __init__(self, root):
        self.root = root
        self.root.title("Customer Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="powder blue")

        
        ABC = Frame(self.root, bg="powder blue", bd=20, relief=RIDGE)
        ABC.grid()

        ABC1 = Frame(ABC,  bd=14, width=1350, height=100, padx=10, bg="powder blue", relief=RIDGE)
        ABC1.grid(row=0, column=0, columnspan=4, sticky=W)
        ABC2 = Frame(ABC,  bd=14, width=450, height=488, padx=10, bg="cadet blue", relief=RIDGE)
        ABC2.grid(row=1, column=0,  sticky=W)
        
        ABC3 = Frame(ABC,  bd=14, width=450, height=488, padx=10, bg="powder blue", relief=RIDGE)
        ABC3.grid(row=1, column=1,  sticky=W)
        ABC4 = Frame(ABC,  bd=14, width=460, height=488, padx=10, bg="cadet blue", relief=RIDGE)
        ABC4.grid(row=1, column=2,  sticky=W)
        ABC5 = Frame(ABC4,  bd=14, width=370, height=340, padx=10, bg="cadet blue", relief=RIDGE)
        ABC5.grid(row=0, column=0,  sticky=W)
        ABC6 = Frame(ABC4,  bd=14, width=370, height=120, padx=10, bg="cadet blue", relief=RIDGE)
        ABC6.grid(row=1, column=0, columnspan=4, sticky=W)

        Date1 = StringVar()
        Time1 = StringVar()
        Date1.set(time.strftime("%d/%m/%Y"))
        Time1.set(time.strftime("%H:%M:%S"))
        #=================================================================================================================
        self.lblTitle = Label(ABC1, textvariable=Date1,font=('Arial',30,'bold'),pady=9,
                              bd=5,bg='cadet blue', fg="cornsilk").grid(row=0,column=0)
        
        self.lblTitle = Label(ABC1, text="\tCustomer Billing Systems\t\t",font=('Arial',30,'bold'),pady=9,
                              bd=5,bg='cadet blue', fg="cornsilk",justify=CENTER).grid(row=0,column=1)
        
        self.lblTitle = Label(ABC1, textvariable=Time1,font=('Arial',25,'bold'),pady=9,
                              bd=5,bg='cadet blue', fg="cornsilk").grid(row=0,column=2)
        #===================================================================================================================
        #==============================================EXIT=================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Customer Billing System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        #====================================================================================================================
        def Reset():
            self.txtReceipt.delete("1.0",END)
            E_Latta.set("0")
            E_Espresso.set("0")
            E_Iced_Latta.set("0")
            E_Vale_Coffee.set("0")  
            E_Cappuccino.set("0")
            E_African_coffee.set("0")
            E_American_coffee.set("0")
            E_Iced_Cappuccino.set("0")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)

            CustomerRef.set("")
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            Nationality.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            Meal.set("")
            RoomType.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")

        #================================================================================================================
        def chkLatta():
            if (var1.get() == 1):
                
               self.txtLatta.configure(state=NORMAL)
               self.txtLatta.focus()
               self.txtLatta.delete('0',END)
               E_Latta.set("")
            elif var1.get() == 0:
                
                self.txtLatta.configure(state=DISABLED)
                E_Latta.set("0")
                    
        def chkEspresso():
            if (var2.get() == 1):
                
               self.txtEspresso.configure(state=NORMAL)
               self.txtEspresso.focus()
               self.txtEspresso.delete('0',END)
               E_Espresso.set("")
            elif var2.get() == 0:
                
                self.txtEspresso.configure(state=DISABLED)
                E_Espresso.set("0")
        def chkIced_Latta():
            if (var3.get() == 1):
                
               self.txtIced_Latta.configure(state=NORMAL)
               self.txtIced_Latta.focus()
               self.txtIced_Latta.delete(0,END)
               E_Iced_Latta.set("")
            elif var3.get() == 0:
                
                self.txtIced_Latta.configure(state=DISABLED)
                E_Iced_Latta.set("0")

        def chkVale_Coffee():
            if (var4.get() == 1):
                
               self.txtVale_Coffee.configure(state=NORMAL)
               self.txtVale_Coffee.focus()
               self.txtVale_Coffee.delete(0,END)
               E_Vale_Coffee.set("")
            elif var4.get() == 0:
                
                
                self.txtVale_Coffee.configure(state=DISABLED)
                E_Vale_Coffee.set("0")
                
        def chkCappuccino():
            if (var5.get() == 1):
                
               self.txtCappuccino.configure(state=NORMAL)
               self.txtCappuccino.focus()
               self.txtCappuccino.delete(0,END)
               E_Cappuccino.set("")
            elif var5.get() == 0:
                
                self.txtCappuccino.configure(state=DISABLED)
                E_Cappuccino.set("0")
                
        def chkAfrican_coffee():
            if (var6.get() == 1):
                
               self.txtAfrican_coffee.configure(state=NORMAL)
               self.txtAfrican_coffee.focus()
               self.txtAfrican_coffee.delete('0',END)
               E_African_coffee.set("")
            elif var6.get() == 0:
                
                self.txtAfrican_coffee.configure(state=DISABLED)
                E_African_coffee.set("0")

        def chkAmerican_coffee():
            if (var7.get() == 1):
                
               self.txtAmerican_coffee.configure(state=NORMAL)
               self.txtAmerican_coffee.focus()
               self.txtAmerican_coffee.delete('0',END)
               E_American_coffee.set("")
            elif var7.get() == 0:
                
                self.txtAmerican_coffee.configure(state=DISABLED)
                E_American_coffee.set("0")
                
        def chkIced_Cappuccino():
            if (var8.get() == 1):
                
               self.txtIced_Cappuccino.configure(state=NORMAL)
               self.txtIced_Cappuccino.focus()
               self.txtIced_Cappuccino.delete('0',END)
               E_Iced_Cappuccino.set("")
            elif var8.get() == 0:
                
                self.txtIced_Cappuccino.configure(state=DISABLED)
                E_Iced_Cappuccino.set("0")
                

                
        
       #================================================================================================================
        def costofItem():
            CustomerRef.set(random.randint(19800, 9875648))
            Item1=float(E_Latta.get())
            Item2=float(E_Espresso.get())
            Item3=float(E_Iced_Latta.get())
            Item4=float(E_Vale_Coffee.get())
            Item5=float(E_Cappuccino.get())
            Item6=float(E_African_coffee.get())
            Item7=float(E_American_coffee.get())
            Item8=float(E_Iced_Cappuccino.get())


            PriceofDrinks = (Item1 * 1.2) + (Item2 * 2.05)\
                            + (Item4 * 1.89) + (Item5 * 1.99) + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)
            SubTotalofITEMS = "#", str('%.2f'% PriceofDrinks)

            SubTotal.set(SubTotalofITEMS)
            Tax="#", str('%.2f'% ((PriceofDrinks)  * 0.15))
            PaidTax.set(Tax)
            TTax = ((PriceofDrinks)  * 0.15)
            TCost = "#", str('%.2f'% (PriceofDrinks  * TTax))
            TotalCost.set(TCost)
                
            self.txtReceipt.insert(END,'Items\t\t\t\t'+ "Cost of Items \n")
            self.txtReceipt.insert(END,'Customer Ref:\t\t\t\t\t'+ CustomerRef.get()+ "\n")
            self.txtReceipt.insert(END,'Latta:\t\t\t\t\t'+ E_Latta.get()+ "\n")
            self.txtReceipt.insert(END,'Espresso: \t\t\t\t\t' + E_Espresso.get()+ "\n")
            self.txtReceipt.insert(END,'Iced_Latta: \t\t\t\t\t' +E_Iced_Latta.get()+ "\n")
            self.txtReceipt.insert(END,'Vale_Coffee: \t\t\t\t\t' +E_Vale_Coffee.get()+ "\n")
            self.txtReceipt.insert(END,'Cappuccino: \t\t\t\t\t'  +E_Cappuccino.get()+  "\n")
            self.txtReceipt.insert(END,'African_coffee: \t\t\t\t\t'  +E_African_coffee.get()+  "\n")
            self.txtReceipt.insert(END,'American_coffee: \t\t\t\t\t' +E_American_coffee.get()+ "\n")
            self.txtReceipt.insert(END,'Iced_Cappuccino: \t\t\t\t\t' +E_Iced_Cappuccino.get()+  "\n")

                
            self.txtReceipt.insert(END,'Taxpaid:\t\t\t\t' + PaidTax.get()+  "\n")
            self.txtReceipt.insert(END,'SubTotal:\t\t\t\t' + str(SubTotal.get())+  "\n")
            self.txtReceipt.insert(END,'\n Total Cost:\t\t\t\t\t' + str(TotalCost.get()))
                                       
                                   
                                   

          









            
        #================================================Receipt================================================================
        self.txtReceipt = Text(ABC5, height = 19, width = 43, bd = 10, font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0,column=0)
        #=====================================================================================================================
    
        
        CustomerRef = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address= StringVar()
        PostCode=StringVar()
        Mobile=StringVar()
        Email=StringVar()
        Nationality=StringVar()
        DOB=StringVar()
        IDType=StringVar()
        Gender=StringVar()
        CheckInDate=StringVar()
        CheckOutDate=StringVar()
        Meal=StringVar()
        RoomType=StringVar()
        RoomNo=StringVar()
        RoomExtNo=StringVar()
        TotalCost=StringVar()
        SubTotal=StringVar()
        PaidTax=StringVar()
        TotalDays=StringVar()

        CustomerRef.set(random.randint(19800, 9875648))
        

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()


        E_Latta=StringVar()
        E_Espresso=StringVar()
        E_Iced_Latta=StringVar()
        E_Vale_Coffee=StringVar()  
        E_Cappuccino=StringVar()
        E_African_coffee=StringVar()
        E_American_coffee=StringVar()
        E_Iced_Cappuccino=StringVar()

        E_Latta.set("0")
        E_Espresso.set("0")
        E_Iced_Latta.set("0")
        E_Vale_Coffee.set("0")  
        E_Cappuccino.set("0")
        E_African_coffee.set("0")
        E_American_coffee.set("0")
        E_Iced_Cappuccino.set("0")

        #=======================================================================================================================
        self.lblCus_Ref=Label(ABC2,font=('arial',12,'bold'),text="Customer Ref:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblCus_Ref.grid(row=0,column=0, sticky=W)
        self.txtCus_Ref = Entry(ABC2, font=('arial',12,'bold'),textvariable= CustomerRef,width = 20)
        self.txtCus_Ref.grid(row=0,column=1,pady=3, padx=20)

        self.lblFirstname=Label(ABC2,font=('arial',12,'bold'),text="Firstname:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblFirstname.grid(row=1,column=0, sticky=W)
        self.txtFirstname= Entry(ABC2, font=('arial',12,'bold'),textvariable=Firstname,width = 20)
        self.txtFirstname.grid(row=1,column=1,pady=3, padx=20)

        self.lblSurname=Label(ABC2,font=('arial',12,'bold'),text="Surname:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblSurname.grid(row=2,column=0, sticky=W)
        self.txtSurname = Entry(ABC2, font=('arial',12,'bold'),textvariable=Surname,width = 20)
        self.txtSurname.grid(row=2,column=1,pady=3, padx=20)

        self.lblAddress=Label(ABC2,font=('arial',12,'bold'),text="Address:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblAddress.grid(row=3,column=0, sticky=W)
        self.txtAddress = Entry(ABC2, font=('arial',12,'bold'),textvariable=Address,width = 20)
        self.txtAddress.grid(row=3,column=1,pady=3, padx=20)

        self.lblPostCode=Label(ABC2,font=('arial',12,'bold'),text="PostCode:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblPostCode.grid(row=4,column=0, sticky=W)
        self.txtPostCode = Entry(ABC2, font=('arial',12,'bold'),textvariable=PostCode,width = 20)
        self.txtPostCode.grid(row=4,column=1,pady=3, padx=20)
        
        self.lblMobile=Label(ABC2,font=('arial',12,'bold'),text="Mobile:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblMobile.grid(row=5,column=0, sticky=W)
        self.txtMobile = Entry(ABC2, font=('arial',12,'bold'),textvariable=Mobile,width = 20)
        self.txtMobile.grid(row=5,column=1,pady=3, padx=20)

        self.lblEmail=Label(ABC2,font=('arial',12,'bold'),text="Email:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblEmail.grid(row=6,column=0, sticky=W)
        self.txtEmail = Entry(ABC2, font=('arial',12,'bold'),textvariable=Email,width = 20)
        self.txtEmail.grid(row=6,column=1,pady=3, padx=20)

        self.lblNationality=Label(ABC2,font=('arial',12,'bold'),text="Nationality:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblNationality.grid(row=7,column=0, sticky=W)
        self.cboNationality = ttk.Combobox(ABC2,textvariable= Nationality, state='readonly',font=('arial', 12, 'bold'),
                                           width=18)
        self.cboNationality['value']=('','British','Nigeria','Kenya','India','Iran','Morocco','Canada', 'France','Norway')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=7,column=1,pady=3,padx=20)

        self.lblDOB=Label(ABC2,font=('arial',12,'bold'),text="Date of Birth:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblDOB.grid(row=8,column=0, sticky=W)
        self.txtDOB = Entry(ABC2, font=('arial',12,'bold'),textvariable=DOB,width = 20)
        self.txtDOB.grid(row=8,column=1,pady=3, padx=20)

        self.lblIDType=Label(ABC2,font=('arial',12,'bold'),text="Type of ID:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblIDType.grid(row=9,column=0, sticky=W)
        self.cboIDType = ttk.Combobox(ABC2, textvariable=IDType, state='readonly',font=('arial',12,'bold'),width = 18)
        self.cboIDType['value'] =('','pilot license','Driving License','student ID', 'passport')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9,column=1,pady=3,padx=20)
        
        self.lblGender=Label(ABC2,font=('arial',12,'bold'),text="Gender:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblGender.grid(row=10,column=0, sticky=W)
        self.cboGender = ttk.Combobox(ABC2, textvariable=Gender, state='readonly',font=('arial',12,'bold'),width = 18)
        self.cboGender['value'] =('','Male','Female')
        
        self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1,pady=3,padx=20)
        
        self.lblCheckInDate=Label(ABC2,font=('arial',12,'bold'),text="Check In Date:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblCheckInDate.grid(row=11,column=0, sticky=W)
        self.txtCheckInDate = Entry(ABC2, font=('arial',12,'bold'),textvariable=Date1,width = 20)
        self.txtCheckInDate.grid(row=11,column=1,pady=3, padx=20)

        
        self.lblCheckOutDate=Label(ABC2,font=('arial',12,'bold'),text="Check Out Date:",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblCheckOutDate.grid(row=12,column=0, sticky=W)
        self.txtCheckOutDate = Entry(ABC2, font=('arial',12,'bold'),textvariable=Date1,width = 20)
        self.txtCheckOutDate.grid(row=12,column=1,pady=3, padx=20)
   
        
        self.lblMeal =Label(ABC2,font=('arial',12,'bold'),text="Meal :",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblMeal .grid(row=13,column=0, sticky=W)
        self.cboMeal = ttk.Combobox(ABC2, textvariable=Meal, state='readonly',font=('arial',12,'bold'),width = 18)
        self.cboMeal['value'] =('','Breakfast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13,column=1,pady=3,padx=20)
        
        
        self.lblRoomType =Label(ABC2,font=('arial',12,'bold'),text="Room Type :",padx=2,fg="cornsilk",bg="cadet blue")
        self.lblRoomType .grid(row=14,column=0, sticky=W)
        self.cboRoomType = ttk.Combobox(ABC2, textvariable=RoomType, state='readonly',font=('arial',12,'bold'),width = 18)
        self.cboRoomType['value'] =('','Single','Double','Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14,column=1,pady=3,padx=20)


        

        
        
        #=================================================================================================================
        self.Latta  = Checkbutton(ABC3, text="Latta", variable=var1, onvalue = 1, offvalue = 0,
                           font=("arial",12,'bold'),bg="powder blue",command = chkLatta).grid(row=0, sticky=W)
        self.txtLatta  = Entry(ABC3,font=("arial",12,'bold'),  textvariable=E_Latta, bd=8,
                        width=20, justify='left', state= DISABLED)
        self.txtLatta.grid(row=0, column=1)

        self.Espresso  = Checkbutton(ABC3, text="Espresso", variable=var2, onvalue = 1, offvalue = 0,
                           font=("arial",12,'bold'),bg="powder blue",command=chkEspresso).grid(row=1, sticky=W)
        self.txtEspresso  = Entry(ABC3,font=("arial",12,'bold'),  textvariable=E_Espresso, bd=8,
                           width=20, justify='left', state= DISABLED)
        self.txtEspresso.grid(row=1, column=1)

        self.Iced_Latta  = Checkbutton(ABC3, text="Iced_Latta", variable=var3, onvalue = 1, offvalue = 0,
                           font=("arial",12,'bold'),bg="powder blue",command=chkIced_Latta).grid(row=2, sticky=W)
        self.txtIced_Latta  = Entry(ABC3,font=("arial",12,'bold'),  textvariable=E_Iced_Latta, bd=8,
                           width=20, justify='left', state= DISABLED)
        self.txtIced_Latta.grid(row=2, column=1)
        
        self.Vale_Coffee  = Checkbutton(ABC3, text="Vale_Coffee", variable=var4, onvalue = 1, offvalue = 0,
                           font=("arial",12,'bold'),bg="powder blue",command=chkVale_Coffee).grid(row=3, sticky=W)
        self.txtVale_Coffee  = Entry(ABC3,font=("arial",12,'bold'),  textvariable=E_Vale_Coffee, bd=8,
                           width=20, justify='left', state= DISABLED)
        self.txtVale_Coffee.grid(row=3, column=1)

        self.Cappuccino  = Checkbutton(ABC3, text="Cappuccino", variable=var5, onvalue = 1, offvalue = 0,
                           font=("arial",12,'bold'),bg="powder blue",command=chkCappuccino).grid(row=4, sticky=W)
        self.txtCappuccino  = Entry(ABC3,font=("arial",12,'bold'),  textvariable=E_Cappuccino, bd=8,
                           width=20, justify='left', state= DISABLED)
        self.txtCappuccino.grid(row=4, column=1)

        self.African_coffee  = Checkbutton(ABC3, text="African_coffee", variable=var6, onvalue = 1, offvalue = 0,
                           font=("arial",12,'bold'),bg="powder blue",command=chkAfrican_coffee).grid(row=5, sticky=W)
        self.txtAfrican_coffee  = Entry(ABC3,font=("arial",12,'bold'),  textvariable=E_African_coffee, bd=8,
                           width=20, justify='left', state= DISABLED)
        self.txtAfrican_coffee.grid(row=5, column=1)

        self.American_coffee  = Checkbutton(ABC3, text="American_coffee", variable=var7, onvalue = 1, offvalue = 0,
                           font=("arial",12,'bold'),bg="powder blue",command=chkAmerican_coffee).grid(row=6, sticky=W)
        self.txtAmerican_coffee  = Entry(ABC3,font=("arial",12,'bold'),  textvariable=E_American_coffee, bd=8,
                           width=20, justify='left', state= DISABLED)
        self.txtAmerican_coffee.grid(row=6, column=1)

        self.Iced_Cappuccino  = Checkbutton(ABC3, text="Iced_Cappuccino", variable=var8, onvalue = 1, offvalue = 0,
                           font=("arial",12,'bold'),bg="powder blue",command=chkIced_Cappuccino).grid(row=7, sticky=W)
        self.txtIced_Cappuccino  = Entry(ABC3,font=("arial",12,'bold'),  textvariable=E_Iced_Cappuccino, bd=8,
                           width=20, justify='left', state= DISABLED)
        self.txtIced_Cappuccino.grid(row=7, column=1)

        self.lblspace=Label(ABC3, text="Tax and Total sum",font=('arial',18,'bold') ,pady=1, bd=9,bg="cadet Blue",
                            fg="Cornsilk",width=26, justify=CENTER).grid(row=8,column=0,columnspan=4)


        self.lblPaidTax=Label(ABC3,font=('arial',12,'bold'),text="Paid Tax:",padx=2,bg="powder blue")
        self.lblPaidTax.grid(row=9,column=0, sticky=W)
        self.txtPaidTax= Entry(ABC3, font=('arial',12,'bold'),textvariable=PaidTax,width = 20)
        self.txtPaidTax.grid(row=9,column=1,pady=3, padx=20)
        
        
        self.lblSubTotal=Label(ABC3,font=('arial',12,'bold'),text="Sub Total:",padx=2,bg="powder blue")
        self.lblSubTotal.grid(row=10,column=0, sticky=W)
        self.txtSubTotal= Entry(ABC3, font=('arial',12,'bold'),textvariable=SubTotal,width = 20)
        self.txtSubTotal.grid(row=10,column=1,pady=3, padx=20)


        
        self.lblTotalCost=Label(ABC3,font=('arial',12,'bold'),text="Total Cost:",padx=2,bg="powder blue")
        self.lblTotalCost.grid(row=11,column=0, sticky=W)
        self.txtTotalCost= Entry(ABC3, font=('arial',12,'bold'),textvariable=TotalCost,width = 20)
        self.txtTotalCost.grid(row=11,column=1,pady=3, padx=20)
        


        

        


        
        #=================================================================================================================
        self.btnTotal = Button(ABC6, padx=14, pady=7,bd=5,fg="black",font=('arial',16,'bold'), width =5, height=2,
                               bg='powder blue', text="Total",command=costofItem).grid(row=0,column=0)

        self.btnReset = Button(ABC6, padx=14, pady=7,bd=5,fg="black",font=('arial',16,'bold'), width =5, height=2,
                               bg='powder blue', text="Reset",command=Reset).grid(row=0,column=1)

        self.btnExit = Button(ABC6, padx=14, pady=7,bd=5,fg="black",font=('arial',16,'bold'), width =5, height=2,
                               bg='powder blue', text="Exit",command=iExit).grid(row=0,column=2)
        #=================================================================================================================
if __name__ == "__main__":
    root = Tk()
    application = customer(root)
    root.mainloop()
    

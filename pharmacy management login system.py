from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime

def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Urchaug Pharmacy Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()
        



        self.LabelTitle = Label(self.frame,text ='Urchaug Pharmacy Management System',font=('romans',30,'bold'),bd=20,
                                bg='yellow green')
        self.LabelTitle.grid(row=0, column=0, columnspan=2,pady=20)
        #======================================Frames=========================================================

        self.Loginframe1 = Frame(self.frame, width=1010,height=300,bd=20,relief='ridge',bg='yellow green')
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = LabelFrame(self.frame, width=1000,height=100,bd=20 ,relief='ridge',bg='yellow green')
        self.Loginframe2.grid(row=2, column=0)

        
        self.Loginframe3 = LabelFrame(self.frame, width=1000,height=200,bd=20,relief='ridge',bg='yellow green')
        self.Loginframe3.grid(row=3, column=0,pady=2)
        #===============================================================================================
        

        self.lblUsername = Label(self.Loginframe1,text ='Username ',font=('romans',30,'bold'),bd=22)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername= Entry(self.Loginframe1,font=('romans',30,'bold'),bd=20,
                                textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1)
        
        self.lblPassword = Label(self.Loginframe1,text ='Password ',font=('romans',30,'bold'),bd=22)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.Loginframe1,font=('romans',30,'bold'),bd=22,show="*",
                                 textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1,padx=85)

        #======================================Buttons=========================================================
        self.btnLogin = Button(self.Loginframe2,text = "Login",width=17,font=('romans',20,'bold'),
                                      command = self.Login_System)
        self.btnLogin.grid(row = 0, column = 0)

        
        self.btnReset = Button(self.Loginframe2,text = "Reset",width=17,font=('romans',20,'bold'),
                                  command = self.Reset)
        self.btnReset.grid(row = 0, column = 1)
        
        
        self.btnExit = Button(self.Loginframe2,text = "Exit",width=17,font=('romans',20,'bold'),
                                  command = self.iExit)
        self.btnExit.grid(row = 0, column = 2)
        #======================================Buttons=========================================================

        self.btnRegistration = Button(self.Loginframe3,text = "Patients Registration System",width=25,font=('romans',20,'bold'),
                                      state = DISABLED,command = self.Registration_window)
        self.btnRegistration.grid(row = 0, column = 0)

        
        self.btnHospital = Button(self.Loginframe3,text = "Hospital Management System",width=25,font=('romans',20,'bold'),
                                  state = DISABLED,command = self.Hospital_window)
        self.btnHospital.grid(row = 0, column = 1,pady=8,padx=20)
        #======================================================================================================

    def Login_System(self):
        user = (self.Username.get())
        pasword = (self.Password.get())

        if (user == str('urchaug')) and (pasword == str(2345)):
            self.btnRegistration.config(state = NORMAL)
            self.btnHospital.config(state = NORMAL)

        else:
            tkinter.messagebox.askyesno("Pharmacy Login System", "You have entered an invalid login details")
            self.btnRegistration.config(state = DISABLED)
            self.btnHospital.config(state = DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
                
    def Reset(self):
        self.btnRegistration.config(state = DISABLED)
        self.btnHospital.config(state = DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
         self.iExit = tkinter.messagebox.askyesno("Pharmacy Login System", "Confirm if you want to exit")
         if self.iExit > 0:
             self.master.destroy()
             return
            
        
        
        
                
                
                
                
            

        #======================================================================================================
    def Registration_window(self):
        self.newwindow = Toplevel(self.master)
        self.app = Window2(self.newwindow)
    
    def Hospital_window(self):
        self.newwindow = Toplevel(self.master)
        self.app = Window3(self.newwindow)    
         

class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patients Registration System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        #self.frame.configure(background='tomato4')
        self.frame.pack()
        #======================================================================================================

         
        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))


         
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()


        
        Firstname = StringVar()
        Surname = StringVar()
        Address= StringVar()
        PostCode=StringVar()
        Telephone=StringVar()
        Ref=StringVar()
        

        
        Membership=StringVar()
        Membership.set("0")
        #===================================Functions DEclaration==========================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Patients Registration", "Confirm if you want to exit")
            if iExit > 0:
                self.master.destroy()
                return

        def Reset():
            
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Telephone.set("")
            Ref.set("")
            Membership.set("0")

                
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_payment.current(0)
        
        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("Club Member Registration", "Confirm if you want to add a new\
record")
            if iResetRecord > 0:
               Reset()
            elif iResetRecord <= 0:
               Reset()
               self.txtReceipt.delete("1.0",END)
            
               return
        def Ref_No():
            Member_Ref=StringVar()
            x = random.randint(10903, 600873)
            randomRef = str(x)
            Member_Ref.set(randomRef)
            Ref.set(randomRef)
        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END, "\t" + Ref.get()+ "\t\t" + Firstname.get() + "\t\t" + Surname.get()
                                   + "\t\t" +Address.get() + "\t\t" +DateofOrder.get() + "\t\t" + Telephone.get()
                                   + "\t\t" + Membership.get() + "\n")

        def Membership_fees():
            
        

            if (var4.get() == 1):
                self.txtMembership.configure(state = NORMAL)
                Item1 = float(2500)
                Membership.set("#" + str(Item1))
                
            elif (var4.get() == 0):
                self.txtMembership.configure(state = DISABLED)
                Membership.set("0")
        

            
                
        
        #===================================Frame======================================================================
        Mainframe = Frame(self.frame)
        Mainframe.grid()

        TitleFrame = Frame(Mainframe, width=1350,padx=26,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial',50,'bold'),text=" Patients Registration System ", padx=2)
        self.lblTitle.grid()
        #===================================LowerFrames=======================================================

        MemberDetailsFrame = LabelFrame(Mainframe,width=1350,height=500,bd=20,
                                        pady=5,relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails =  LabelFrame(MemberDetailsFrame, bd=10,width=1350,height=400,relief=RIDGE)
        #FrameDetails.pack(side=LEFT)

        MemberName_F = LabelFrame(MemberDetailsFrame,bd=10,width=350,height=400,
                                  font=('arial',12,'bold'),text='Customer Name',relief=RIDGE)
        MemberName_F.grid(row=0,column=0)

        Receipt_ButtonFrame = LabelFrame(MemberDetailsFrame,bd=10,width=1000,height=400,
                                         relief=RIDGE)
        Receipt_ButtonFrame.grid(row=0,column=1)
        #=====================================================================================================
         
        self.lblReferenceNo=Label(MemberName_F,font=('arial',14,'bold'),text=" Reference No ", bd=7)
        self.lblReferenceNo.grid(row=0,column=0,sticky=W)
        self.txtReferenceNo=Entry(MemberName_F,font=('arial',14,'bold'), bd=7,textvariable=Ref,
                                  state = DISABLED,insertwidth=2)
        self.txtReferenceNo.grid(row=0,column=1)

        
        self.lblFirstname=Label(MemberName_F,font=('arial',14,'bold'),text=" First name ", bd=7)
        self.lblFirstname.grid(row=1,column=0,sticky=W)
        self.txtFirstname=Entry(MemberName_F,font=('arial',14,'bold'), bd=7,insertwidth=2,textvariable=Firstname)
        self.txtFirstname.grid(row=1,column=1)

        
        self.lblSurname=Label(MemberName_F,font=('arial',14,'bold'),text=" Surname ", bd=7)
        self.lblSurname.grid(row=2,column=0,sticky=W)
        self.txtSurname=Entry(MemberName_F,font=('arial',14,'bold'), bd=7,insertwidth=2,textvariable=Surname)
        self.txtSurname.grid(row=2,column=1)

        
        self.lblAddress=Label(MemberName_F,font=('arial',14,'bold'),text=" Address ", bd=7)
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress=Entry(MemberName_F,font=('arial',14,'bold'), bd=7,insertwidth=2,textvariable=Address)
        self.txtAddress.grid(row=3,column=1)

        
        self.lblPostCode=Label(MemberName_F,font=('arial',14,'bold'),text=" Post Code ", bd=7)
        self.lblPostCode.grid(row=4,column=0,sticky=W)
        self.txtPostCode=Entry(MemberName_F,font=('arial',14,'bold'), bd=7,insertwidth=2,textvariable=PostCode)
        self.txtPostCode.grid(row=4,column=1)

        
        self.lblTelephone=Label(MemberName_F,font=('arial',14,'bold'),text=" Telephone", bd=7)
        self.lblTelephone.grid(row=5,column=0,sticky=W)
        self.txtTelephone=Entry(MemberName_F,font=('arial',14,'bold'), bd=7,insertwidth=2,textvariable=Telephone)
        self.txtTelephone.grid(row=5,column=1)

        
        self.lblDate=Label(MemberName_F,font=('arial',14,'bold'),text=" Date", bd=7)
        self.lblDate.grid(row=6,column=0,sticky=W)
        self.txtDate=Entry(MemberName_F,font=('arial',14,'bold'), bd=7,insertwidth=2,textvariable=DateofOrder)
        self.txtDate.grid(row=6,column=1)
        #========================================combo button========================================================
        
        
        self.lblProve_of_ID = Label(MemberName_F,font=('arial',14,'bold'),text="Prove_of_ID:",bd=7)
        self.lblProve_of_ID.grid(row=7,column=0, sticky=W)
        self.cboProve_of_ID = ttk.Combobox(MemberName_F,textvariable= var1, state='readonly',font=('arial', 14, 'bold'),
                                           width=19)
        self.cboProve_of_ID['value']=('','Pilot License','Driving License','Passport','Student ID',)
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7,column=1)

        
        self.lblType_of_Member = Label(MemberName_F,font=('arial',14,'bold'),text="Type of Member:",bd=7)
        self.lblType_of_Member.grid(row=8,column=0, sticky=W)
        self.cboType_of_Member = ttk.Combobox(MemberName_F,textvariable= var2, state='readonly',font=('arial', 14, 'bold'),
                                           width=19)
        self.cboType_of_Member['value']=('','Full Member','Annual  Membership','Pay As You Go','Honorary Member')
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8,column=1)
        

        
        self.lblMethod_of_payment = Label(MemberName_F,font=('arial',14,'bold'),text="Method of payment:",bd=7)
        self.lblMethod_of_payment.grid(row=9,column=0, sticky=W)
        self.cboMethod_of_payment = ttk.Combobox(MemberName_F,textvariable= var3, state='readonly',font=('arial', 14, 'bold'),
                                           width=19)
        self.cboMethod_of_payment['value']=('','Visa Card','Master Card','Debit Card','Cash')
        self.cboMethod_of_payment.current(0)
        self.cboMethod_of_payment.grid(row=9,column=1)
        
        #==================================================check button===========================================================
        self.chkMembership = Checkbutton(MemberName_F,text="Membership Fees",variable=var4, onvalue=1,
                                         offvalue = 0,font=('arial',16,'bold'),command = Membership_fees).grid(row=10,column=0,sticky=W)

        self.txtMembership = Entry(MemberName_F,font=('arial',14,'bold'),textvariable=Membership,bd=7,
                                   insertwidth=2,state=DISABLED, justify=RIGHT)
        
        self.txtMembership.grid(row=10,column=1)
         

        #===================================================Receipt==========================================================
        
        self.lblLabel = Label(Receipt_ButtonFrame,font=('arial',10,'bold'),bd=7,pady=10,
                              text="Patient Ref\t Firstname\t Surname\t Address\t\t Date Reg.\t Telephone\t Patient Paid")
        self.lblLabel.grid(row=0,column=0, columnspan=4)

        
        self.txtReceipt = Text(Receipt_ButtonFrame,font=('arial',10,'bold'),width = 112,height=22)
        self.txtReceipt.grid(row=1,column=0, columnspan=4)
        
        #=================================================buttons============================================================
        self.btnReceipt = Button(Receipt_ButtonFrame,padx=18,bd=7,font=('arial', 16,'bold'),width=13,
                                 text='Receipt',command=Receipt).grid(row=2,column=0)

        self.btnReset = Button(Receipt_ButtonFrame,padx=18,bd=7,font=('arial', 16,'bold'),width=13,
                                 text='Reset',command=iResetRecord).grid(row=2,column=1)

        self.btnExit = Button(Receipt_ButtonFrame,padx=18,bd=7,font=('arial', 16,'bold'),width=13,
                                 text='Exit',command = iExit).grid(row=2,column=2)
        
        #=============================================================================================================
        #======================================================================================================


class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        #=====================================================================================================

         
        cboNameTablets = StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberTablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpDate = StringVar()
        DailyDose = StringVar()
        PossibleSideEffects = StringVar()
        FurtherInfo = StringVar()
        StorageAdvice = StringVar()
        DrivingUsingMachines = StringVar()
        HowToUseMedication = StringVar()
        PatientID = StringVar()
        PatientNHSNo = StringVar()
        PatientName = StringVar()
        DateOfBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        #===============================================functions declaration============================================================
         
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hospital Management System", "Confirm if you want to exit")
            if iExit > 0:
                self.master.destroy()
                return

        def iReset():
                
            cboNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("") 
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInfo.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowToUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            
            return
        def iDelete():
            
            cboNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("") 
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInfo.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowToUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)
            return
        def iPrescription():
            
            self.txtPrescription.insert(END,'Name of Tablets: \t\t\t\t' +   cboNameTablets.get() + "\n")
            self.txtPrescription.insert(END,'Reference No: \t\t\t\t' + Ref.get() + "\n")
            self.txtPrescription.insert(END,'Dose: \t\t\t\t' + Dose.get() + "\n")
            self.txtPrescription.insert(END,'Number of Tablets: \t\t\t\t' + NumberTablets.get() + "\n")
            self.txtPrescription.insert(END,'Lot: \t\t\t\t' + Lot.get() + "\n")
            self.txtPrescription.insert(END,'Issued Date: \t\t\t\t' + IssuedDate.get() + "\n")
            self.txtPrescription.insert(END,'Expiry Date: \t\t\t\t' + ExpDate.get() + "\n")
            self.txtPrescription.insert(END,'Possible Side Effects: \t\t\t\t' + PossibleSideEffects.get() + "\n")
            self.txtPrescription.insert(END,'Further Information: \t\t\t\t' + FurtherInfo.get() + "\n")
            self.txtPrescription.insert(END,'Storage Advice:   \t\t\t\t' +   StorageAdvice.get() + "\n")
            self.txtPrescription.insert(END,'Driving or UsingMachines: \t\t\t\t' + DrivingUsingMachines.get() + "\n")
            self.txtPrescription.insert(END,'How To Use Medication: \t\t\t\t' +    HowToUseMedication.get() + "\n")
            self.txtPrescription.insert(END,'Patient ID: \t\t\t\t' + PatientID.get() + "\n")
            self.txtPrescription.insert(END,'Patient NHS no: \t\t\t\t' + PatientNHSNo.get() + "\n")
            self.txtPrescription.insert(END,'Patient Name: \t\t\t\t' +  PatientName.get() + "\n")
            self.txtPrescription.insert(END,'Date Of Birth: \t\t\t\t' +   DateOfBirth.get() + "\n")
            self.txtPrescription.insert(END,'Patient Address: \t\t\t\t' + PatientAddress.get() + "\n")
            
            

            return

        def iPrescriptionData():
            
            self.txtFrameDetail.insert(END,"\t"+ cboNameTablets.get()+"\t\t"+Ref.get()+"\t"+Dose.get()+"\t"+
            NumberTablets.get() + "\t"+ Lot.get()+ "\t\t"+IssuedDate.get() +"\t\t"+ExpDate.get() +"\t" +
            DailyDose.get() + "\t"+ StorageAdvice.get()+ "\t\t"+PatientNHSNo.get() +"\t\t"+ PatientName.get() +"\t"
                                       + DateOfBirth.get()+"\t"+ PatientAddress.get() + "\n")
            

            return
        
        
        
        #===============================================frames============================================================
        
        MainFrame = Frame(self.frame)
        MainFrame.grid()

        
        TitleFrame = Frame(MainFrame, width=1350, padx=20,bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        
        self.lblTitle = Label(TitleFrame,width=39,font=('arial',35,'bold'),text="\tUrchaug Hospital Management Systems\t",padx=2)
        self.lblTitle.grid()

        
        FrameDetail = Frame(MainFrame, width=1350,height=100, padx=20,bd=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        
        ButtonFrame = Frame(MainFrame, width=1350,height=50, padx=20,bd=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        
        DataFrame = Frame(MainFrame, width=1350,height=400, padx=20,bd=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        
        DataFrameLEFT = LabelFrame(DataFrame, width=800,height=300, padx=20,bd=10, relief=RIDGE,
                                   font=('arial',12,'bold'), text="Patient Information:",)
        DataFrameLEFT.pack(side=LEFT)

        
        DataFrameRIGHT = LabelFrame(DataFrame, width=450,height=300, padx=20,bd=10, relief=RIDGE,
                               font=('arial',12,'bold'), text=" Prescription:",)
        DataFrameRIGHT.pack(side=RIGHT)

        
        #=====================================DataFrameLEFT widgets=====================================================================
        self.lblNameTablet = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Name Of Tablet:", padx=2,pady=2)
        self.lblNameTablet.grid(row=0, column=0, sticky=W)

        self.cboNameTablet = ttk.Combobox(DataFrameLEFT, font=('arial',12,'bold'), state='readonly',textvariable=cboNameTablets,
                                          width = 23)
        self.cboNameTablet['value']=('','Ibuprofen','Co-codamol','Paracetamol','Amlodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)
        
        self.lblFurtherInfo = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Further Information:", padx=2,pady=2)
        self.lblFurtherInfo.grid(row=0, column=2, sticky=W)
        self.txtFurtherInfo = Entry(DataFrameLEFT, font=('arial',12,'bold') ,textvariable=FurtherInfo,width = 25)
        self.txtFurtherInfo.grid(row=0, column=3)

        
        self.lblRef = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Reference No:", padx=2,pady=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Ref, width = 25)
        self.txtRef.grid(row=1, column=1)

        
        self.lblStorageAdvice = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Storage Advice:", padx=2,pady=2)
        self.lblStorageAdvice.grid(row=1, column=2, sticky=W)
        self.txtStorageAdvice = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable=StorageAdvice,width = 25)
        self.txtStorageAdvice.grid(row=1, column=3)

        self.lblDose = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Dose:", padx=2,pady=2)
        self.lblDose.grid(row=2, column=0, sticky=W)
        self.txtDose = Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Dose, width = 25)
        self.txtDose.grid(row=2, column=1)

        
        self.lblDrivingUsingMachines = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Driving Machines:", padx=2,pady=2)
        self.lblDrivingUsingMachines.grid(row=2, column=2, sticky=W)
        self.txtDrivingUsingMachines = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable=DrivingUsingMachines,width = 25)
        self.txtDrivingUsingMachines.grid(row=2, column=3)

        
        self.lblNumberTablets = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Number Of Tablets:", padx=2,pady=2)
        self.lblNumberTablets.grid(row=3, column=0, sticky=W)
        self.txtNumberTablets = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable=NumberTablets,width = 25)
        self.txtNumberTablets.grid(row=3, column=1)

        
        self.lblHowToUseMedication = Label(DataFrameLEFT, font=('arial',12,'bold'), text="How To Use Medication:", padx=2,pady=2)
        self.lblHowToUseMedication.grid(row=3, column=2, sticky=W)
        self.txtHowToUseMedication = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable=HowToUseMedication,width = 25)
        self.txtHowToUseMedication.grid(row=3, column=3)

        
        self.lblLot  = Label(DataFrameLEFT, font=('arial',12,'bold'), text="  Lot :", padx=2,pady=2)
        self.lblLot.grid(row=4, column=0, sticky=W)
        self.txtLot  = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable= Lot ,width = 25)
        self.txtLot.grid(row=4, column=1)

        
        self.lblPatientID  = Label(DataFrameLEFT, font=('arial',12,'bold'), text="  Patient ID :", padx=2,pady=2)
        self.lblPatientID.grid(row=4, column=2, sticky=W)
        self.txtPatientID  = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable= PatientID ,width = 25)
        self.txtPatientID.grid(row=4, column=3)

        
        self.lblIssuedDate  = Label(DataFrameLEFT, font=('arial',12,'bold'), text="  Issued Date :", padx=2,pady=2)
        self.lblIssuedDate.grid(row=5, column=0, sticky=W)
        self.txtIssuedDate = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable= IssuedDate ,width = 25)
        self.txtIssuedDate.grid(row=5, column=1)

        
        self.lblPatientNHSNo  = Label(DataFrameLEFT, font=('arial',12,'bold'), text="  NHS Number :", padx=2,pady=2)
        self.lblPatientNHSNo.grid(row=5, column=2, sticky=W)
        self.txtPatientNHSNo = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable= PatientNHSNo ,width = 25)
        self.txtPatientNHSNo.grid(row=5, column=3)

        
        self.lblExpDate  = Label(DataFrameLEFT, font=('arial',12,'bold'), text="  Expiry Date :", padx=2,pady=2)
        self.lblExpDate.grid(row=6, column=0, sticky=W)
        self.txtExpDate = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable= ExpDate ,width = 25)
        self.txtExpDate.grid(row=6, column=1)

        
        self.lblPatientName  = Label(DataFrameLEFT, font=('arial',12,'bold'), text="  Patient Name :", padx=2,pady=2)
        self.lblPatientName.grid(row=6, column=2, sticky=W)
        self.txtPatientName = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable= PatientName ,width = 25)
        self.txtPatientName.grid(row=6, column=3)

        
        
        self.lblDailyDose  = Label(DataFrameLEFT, font=('arial',12,'bold'), text="  Daily Dose:", padx=2,pady=2)
        self.lblDailyDose.grid(row=7, column=0, sticky=W)
        self.txtDailyDose = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable= DailyDose ,width = 25)
        self.txtDailyDose.grid(row=7, column=1)

        
        self.lblDateOfBirth  = Label(DataFrameLEFT, font=('arial',12,'bold'), text="  Date Of Birth:", padx=2,pady=2)
        self.lblDateOfBirth.grid(row=7, column=2, sticky=W)
        self.txtDateOfBirth = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable= DateOfBirth ,width = 25)
        self.txtDateOfBirth.grid(row=7, column=3)

        
        
        self.lblPossibleSideEffects  = Label(DataFrameLEFT, font=('arial',12,'bold'), text="  Side Effects:", padx=2,pady=2)
        self.lblPossibleSideEffects.grid(row=8, column=0, sticky=W)
        self.txtPossibleSideEffects = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable= PossibleSideEffects,width = 25)
        self.txtPossibleSideEffects.grid(row=8, column=1)

        
        self.lblPatientAddress  = Label(DataFrameLEFT, font=('arial',12,'bold'), text=" Patient Address:", padx=2,pady=2)
        self.lblPatientAddress.grid(row=8, column=2, sticky=W)
        self.txtPatientAddress = Entry(DataFrameLEFT, font=('arial',12,'bold'), textvariable= PatientAddress,width = 25)
        self.txtPatientAddress.grid(row=8, column=3)


        #=====================================DataFrameRIGHT widgets==========================================================
        self.txtPrescription = Text(DataFrameRIGHT, font=('arial',12,'bold'),width=43,height=14, padx=2,pady=6)
        self.txtPrescription.grid(row=0, column=0)
        #=====================================BUTTONFRAME widgets==========================================================
        self.btnPrescription=Button(ButtonFrame, text= 'Prescription',font=('arial', 12,'bold'),
                                   width=24, bd=4,command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)

        self.btnPrescriptionData=Button(ButtonFrame, text= 'Prescription Data',font=('arial', 12,'bold')
                                        , width=24, bd=5,command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0, column=1)

        
        self.btnDelete=Button(ButtonFrame, text= 'Delete',font=('arial', 12,'bold'), width=24, bd=4,command=iDelete)
        self.btnDelete.grid(row=0, column=2)

        self.btnReset=Button(ButtonFrame, text= 'Reset',font=('arial', 12,'bold'), width=24, bd=4,command=iReset)
        self.btnReset.grid(row=0, column=3)

        self.btnExit=Button(ButtonFrame, text= 'Exit',font=('arial', 12,'bold'), width=24, bd=4,command=iExit)
        self.btnExit.grid(row=0, column=4)

        
        
        #=====================================Framedetail widgets==========================================================
        
        self.lblLabel = Label(FrameDetail,font=('arial',10,'bold'),pady=8,
        text="Name of Tablets\t Reference No.\t Dossage\t No. of Tablets\t Lot\t Issued Date\t Expiry Date\
        \tDaily Dose\tStorage Adv.\tNHS Number\t Patient Name\t DOB\t Address",)
        self.lblLabel.grid(row=0, column=0)

        
        self.txtFrameDetail = Text(FrameDetail, font=('arial',12,'bold'),width=140,height=4, padx=2,pady=8)
        self.txtFrameDetail.grid(row=1, column=0)
        #======================================================================================================
        
        
        




if __name__ == '__main__':
    main()
    

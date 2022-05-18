from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox

import sqlite3
sqliteConnection = sqlite3.connect("hms1.db")
cursor = sqliteConnection.cursor()
 
class Hospital:
  def __init__(self,root):
    self.root=root
    self.root.title("Hospital Management System")
    self.root.geometry("1540x800+0+0")

    lbltitle=Label(self.root, bd=20, relief=RIDGE, text = "HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="orchid1", font=("times new roman", 50, "bold"))
    lbltitle.pack(side=TOP, fill=X)

    # Dataframe
    DataFrame = Frame(self.root, bd=20, relief=RIDGE)
    DataFrame.place(x=0,y=130,width=1530,height=400)

    DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE,fg="black", padx=10, font=("times new roman", 12, "bold"), text="Patient Information")
    DataFrameLeft.place(x=0,y=5,width=980,height=350)

    DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
    DataFrameRight.place(x=990,y=5,width=460,height=350)


# Buttonframe
    ButtonFrame = Frame(self.root)
    ButtonFrame.place(x=0,y=530,width=1530,height=70)


    # Detailsframe
    DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
    DetailsFrame.place(x=0,y=600,width=1530,height=190)


    # DataframeLeft
    lblDoctorName = Label(DataFrameLeft, text="Name of Doctor", font=("arial", 20, "bold"),fg="firebrick", padx=2, pady=6)
    lblDoctorName.grid(row=0,column=0)
    comDoctorName = ttk.Combobox(DataFrameLeft,font=("arial", 20, "bold"), width=33)
    comDoctorName["values"] = ("HG PANKAJ GOP P","HG ADIGOPAL P")
    comDoctorName.current(0)
    comDoctorName.grid(row=0,column=1)

    lblName = Label(DataFrameLeft, font=("arial", 20, "bold"),fg="firebrick", text="Name of Patient", padx=2)
    lblName.grid(row=1,column=0,sticky=W)
    txtName = Entry(DataFrameLeft, font=("arial", 20, "bold"), width=35)
    txtName.grid(row=1,column=1)

    lblBloodGroup = Label(DataFrameLeft, text="Blood Group", font=("arial", 20, "bold"),fg="firebrick", padx=2, pady=6)
    lblBloodGroup.grid(row=2,column=0)
    comBloodGroup = ttk.Combobox(DataFrameLeft,font=("arial", 20, "bold"), width=33)
    comBloodGroup["values"] = ("A+","B","AB","O+","A-","B-","AB-","o-" )
    comBloodGroup.current(0)
    comBloodGroup.grid(row=2,column=1)

    lblAge = Label(DataFrameLeft, font=("arial", 20, "bold"), text="Age of Patient",fg="firebrick", padx=2,pady=4)
    lblAge.grid(row=3,column=0,sticky=W)
    txtAge = Entry(DataFrameLeft, font=("arial", 20, "bold"), width=35)
    txtAge.grid(row=3,column=1)



    lblSex = Label(DataFrameLeft, text="Sex of Patient", font=("arial", 20, "bold"),fg="firebrick", padx=2, pady=6)
    lblSex.grid(row=4,column=0)
    comSex = ttk.Combobox(DataFrameLeft,font=("arial", 20, "bold"), width=33)
    comSex["values"] = ("Male","Female","Unspecified")
    comSex.current(0)
    comSex.grid(row=4,column=1)        

    lblDisease = Label(DataFrameLeft, font=("arial", 20, "bold"), text="Disease",fg="firebrick", padx=2,pady=6)
    lblDisease.grid(row=5,column=0,sticky=W)
    txtDisease = Entry(DataFrameLeft, font=("arial", 20, "bold"), width=35)
    txtDisease.grid(row=5,column=1)

    
    
    #DataFrameRight
    self.txtPrescription = Text(DataFrameRight,font=("arial", 20, "bold"), width=45, height=16,pady=6)
    self.txtPrescription.grid(row=0,column=0)


    #Buttons
    btnPrescription=Button(ButtonFrame,text="Prescription",bg="plum1",fg="white",font=("arial",12,"bold"),width=25,height=16,pady=6)
    btnPrescription.grid(row=0,column=0)

    btnPrescriptionData = Button(ButtonFrame,text="Prescription Data", bg="pink", fg="white", font=("arial", 12, "bold"), width=25, height=16,pady=6)
    btnPrescriptionData.grid(row=0,column=1)

    btnUpdate = Button(ButtonFrame,text="Update", bg="plum1", fg="white", font=("arial", 12, "bold"), width=25, height=16,pady=6)
    btnUpdate.grid(row=0,column=2)

    btnDelete = Button(ButtonFrame,text="Delete", bg="pink", fg="white", font=("arial", 12, "bold"), width=25, height=16,pady=6)
    btnDelete.grid(row=0,column=3)

    btnClear = Button(ButtonFrame,text="Clear", bg="plum1", fg="white", font=("arial", 12, "bold"), width=25, height=16,pady=6)
    btnClear.grid(row=0,column=4)

    btnExit = Button(ButtonFrame,text="Exit", bg="pink", fg="white", font=("arial", 12, "bold"), width=25, height=16,pady=6)
    btnExit.grid(row=0,column=5)


  

root = Tk()
btn = Hospital(root)
root.mainloop()
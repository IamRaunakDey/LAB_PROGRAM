# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 19:02:20 2023

@author: ISHITA KAR
"""

from tkinter import *
import re
import datetime
import csv
from tkinter import messagebox
import tkinter.ttk as ttk

datafile = 'datarecords.csv'
with open(datafile, 'r+',newline='',encoding='utf-8') as csvfile:
    csvread = [line for line in csv.reader(csvfile)]
    if len(csvread) == 0:
        fields = ['ID','Name','Mobile Number','Date of Birth','Address 1','Address 2','State','Guardian\'s Name','Email ID','College','Course','Department','Year']
        csvwrite = csv.writer(csvfile,lineterminator='\n')
        csvwrite.writerow(fields)

root=Tk()
root.title("Data Entry")
root.configure(bg='grey')
root.geometry("1000x1000")

#define style
style=ttk.Style(root)
style.theme_use("default")

#submit window
def submitWindow():
    top=Toplevel()
    top.geometry("1000x1000")
    top.title("form submission")
    style=ttk.Style(top)
    style.theme_use("clam")

    #Personal details
    l0=ttk.Label(top,text="PERSONAL DETAILS",font=('Times', 16))
    l0.grid(row=0,column=0,padx=20,pady=20)
    lName=ttk.Label(top,text="NAME")
    lName.grid(row=1,column=0,padx=10,pady=10)
    lMnum=ttk.Label(top,text="MOBILE NUMBER")
    lMnum.grid(row=2,column=0,padx=10,pady=10)
    ldob=ttk.Label(top,text="DATE OF BIRTH")
    ldob.grid(row=3,column=0,padx=10,pady=10)
    lad1=ttk.Label(top,text="ADDRESS(LINE 1)")
    lad1.grid(row=5,column=0,padx=10,pady=10)
    lad2=ttk.Label(top,text="ADDRESS(LINE 2)")
    lad2.grid(row=8,column=0,padx=10,pady=10)
    lState=ttk.Label(top,text="STATE")
    lState.grid(row=10,column=0,padx=10,pady=10)
    lgname=ttk.Label(top,text="GUARDIAN'S NAME")
    lgname.grid(row=11,column=0,padx=10,pady=10)
    lemail=ttk.Label(top,text="EMAIL ID")
    lemail.grid(row=12,column=0,padx=10,pady=10)
    lacad=ttk.Label(top,text="ACADEMIC DETAILS",font=('Times', 16))
    lacad.grid(row=13,column=0,padx=20,pady=20)
    lncol=ttk.Label(top,text="NAME OF COLLEGE")
    lncol.grid(row=14,column=0,padx=10,pady=10)
    lcname=ttk.Label(top,text="COURSE NAME")
    lcname.grid(row=15,column=0,padx=10,pady=10)
    ldep=ttk.Label(top,text="DEPARTMENT")
    ldep.grid(row=16,column=0,padx=10,pady=10)
    lyr=ttk.Label(top,text="YEAR")
    lyr.grid(row=17,column=0,padx=10,pady=10)
    #Entry Fields
    eName=ttk.Entry(top,width=30)
    eName.grid(row=1,column=1,columnspan=100)
    eMnum=ttk.Entry(top,width=30)
    eMnum.grid(row=2,column=1,columnspan=100)
    eDOB=ttk.Entry(top,width=30)
    eDOB.grid(row=3,column=1,columnspan=100)
    eDOB.insert(0,"DD/MM/YYYY")
    eAd1=ttk.Entry(top,width=30)
    eAd1.grid(row=5,column=1,columnspan=100)
    eAd2=ttk.Entry(top,width=30)
    eAd2.grid(row=8,column=1,columnspan=100)
    #dropdown boxes
    eState=StringVar()
    dropState=ttk.OptionMenu(top,eState,"West Bengal","Bihar","Jharkhand")
    dropState.grid(row=10,column=1)
    eGname=ttk.Entry(top,width=30)
    eGname.grid(row=11,column=1,columnspan=100)
    eMail=ttk.Entry(top,width=30)
    eMail.grid(row=12,column=1,columnspan=100)
    #academic details
    eNcol=ttk.Entry(top,width=30)
    eNcol.grid(row=14,column=1,columnspan=100)
    eCname=ttk.Entry(top,width=30)
    eCname.grid(row=15,column=1,columnspan=100)
    eDept=ttk.Entry(top,width=30)
    eDept.grid(row=16,column=1,columnspan=100)
    #dropdown boxes
    eyr=StringVar()
    dropYear=ttk.OptionMenu(top,eyr,'1st',"1st","2nd","3rd","4th")
    dropYear.grid(row=17,column=1)
    #checkbox
    cAgree=IntVar()
    cag=ttk.Checkbutton(top,text="All the informations furnished above are correct",variable=cAgree)
    cag.grid(row=19,column=0)

    #show warning
    def popup():
        messagebox.showwarning("Warning","Please tick the checkbox")

    def checkValues():
        #check if eName has correct parameters
        errors=''
        data=eName.get()
        if(len(data)<1 or re.search('[^A-Za-z ]',data)):
            errors='Incorrect parameters in Name Field\n'
        #check eMnum
        data=eMnum.get()
        if(len(data)<1 or len(data)>10 or re.search('[^0-9]',data)):
            errors+='Incorrect parameters in Mobile Number Field\n'
        #check eDOB
        data=eDOB.get().split('/')
        try:
            datetime.datetime(int(data[2]),int(data[1]),int(data[0]))
        except ValueError:
            errors+='Incorrect parameters in Date Field\n'
        #check eGname
        data=eGname.get()
        if(len(data)<1 or re.search('[^A-Za-z ]',data)):
            errors+='Incorrect parameters in Guardian Name Field\n'
        #check email
        data=str(eMail.get())
        if(not re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',data)):
            errors+='Incorrect Email\n'
        #check encol
        data=eNcol.get()
        if(len(data)<1):
            errors+='Incorrect parameters in Name of College Field\n'
        #check eCname
        data=eCname.get()
        if(len(data)<1):
            errors+='Incorrect parameters in Course Name Field\n'
        #check eDept
        data=eDept.get()
        if(len(data)<1):
            errors+='Incorrect parameters in Department Field'
        if(len(errors)>0):
            messagebox.showerror('Error(s)',errors)
            top.focus_set()
            return False
        return True

    def click():
        if cAgree.get()==0:
            popup()
            top.focus_set()
            return
        if not checkValues():
            return
        with open(datafile,'a',newline='',encoding='utf-8') as csvfile:
            csvwrite = csv.writer(csvfile,lineterminator='\n')
            #generate UID for name
            uid = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            datarow=[uid,eName.get(),eMnum.get(),eDOB.get(),eAd1.get(),eAd2.get(),
                eState.get(),eGname.get(),eMail.get(),eNcol.get(),eCname.get(),eDept.get(),eyr.get()]
            #write data in file
            csvwrite.writerow(datarow)
            messagebox.showinfo('Success','UID : '+uid+'\nName : '+eName.get())
            #destroy submit window
            top.destroy()

    #submit button
    button_sub=ttk.Button(top,text="SUBMIT",command=click)
    button_sub.grid(row=20,column=1,padx=10,pady=10)
        
        
        
        
# height=3       


#main window
l=ttk.Label(root,text="FORM FILLING UP", font=('Times', 20))
button_1=ttk.Button(root,text="SUBMIT NEW ",width=13,command=submitWindow)
button_2=ttk.Button(root,text="VIEW DATA",width=13)
button_1.place(x=200,y=200)
button_2.place(x=500,y=200)
l.pack(padx=200)



root.mainloop()
from tkinter import *
root=Tk()
def getvals():
    print("it works")
root.geometry("644x344")
Label(root,text="Welcome to Shivam Travels",font="comicsansms 16 bold",pady=15).grid(row=0,column=3)
name=Label(root,text="name")
phone=Label(root,text="phone")
gender=Label(root,text="gender")
emergencycontact=Label(root,text="emergencycontact")
paymentmode=Label(root,text="paymentmode")
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergencycontact.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencycontactvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencycontactentry=Entry(root,textvariable=emergencycontactvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)





nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencycontactentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

foodservice=Checkbutton(text="want to get your meal?",variable=foodservicevalue)
foodservice.grid(row=6,column=3)
Button(text="Submit",command=getvals).grid(row=7,column=3)
root.mainloop()
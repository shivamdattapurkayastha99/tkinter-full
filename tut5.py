from tkinter import *
root=Tk()
def getvals():
    print(uservalue.get(),passvalue.get())
root.geometry("655x333")
user=Label(root,text="username")
password=Label(root,text="password")
user.grid()
password.grid(row=1)
uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(text="submit",command=getvals).grid()


root.mainloop()
from tkinter import *
root=Tk()
root.geometry("655x333")
fl=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
fl.pack(side=LEFT,fill=Y)
f2=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
l=Label(fl,text="tkinter project-text editor")
l.pack(pady=42)

l=Label(f2,text="Welcome to Shivam text editor",font="Helvetica 16 bold",fg="black")
l.pack()
root.mainloop()
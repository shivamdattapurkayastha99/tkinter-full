from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("733x566")
root.title("Shivam's IDE")
def myfunc():
    print("It is working")
def help():
    print(" help")
    tmsg.Message("help","Shivam will help you")
def Rateus():
    
    value=tmsg.askquestion("Was your experience good","Was your experience good with this gui")
    print(value)
    if value=="yes":
        msg="Rate us please"
    else:
        msg="Tell us what went wrong"
    tmsg.showinfo("Experience",msg)
def shivam():
    
    ans=tmsg.askretrycancel("work hard","dont work hard")
    if ans:
        print("try harder")
    else:
        print("enjoy working")
# mymenu=Menu(root)
# mymenu.add_command(label="File",command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)
yourmenubar=Menu(root)
m1=Menu(yourmenubar,tearoff=0)
m1.add_command(label="New Project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save as",command=myfunc)
m1.add_command(label="Print",command=myfunc)
yourmenubar.add_cascade(label="File",menu=m1)

m2=Menu(yourmenubar,tearoff=0)
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_separator()
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Find",command=myfunc)
yourmenubar.add_cascade(label="Edit",menu=m2)
root.config(menu=yourmenubar)

m3=Menu(yourmenubar,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=Rateus)
m3.add_command(label="Shivam",command=shivam)
yourmenubar.add_cascade(label="Help",menu=m3)
root.config(menu=yourmenubar)
root.mainloop()
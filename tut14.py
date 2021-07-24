from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x233")
root.title("Radio button")
def order():
    tmsg.showinfo("Order Received",f"Order Received for {var.get()}")
# var=IntVar()
# var.set(1)
var=StringVar()
var.set("radio")
Label(root,text="what would you like to eat",justify=LEFT,padx=14,font="lucida 19 bold").pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Idli",padx=14,variable=var,value="Idli").pack(anchor="w")
radio=Radiobutton(root,text="Chicken",padx=14,variable=var,value="Chicken").pack(anchor="w")
Button(text="Order Now",command=order).pack()
root.mainloop()
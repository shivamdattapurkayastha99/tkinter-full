from tkinter import *
import tkinter.messagebox as tmsg
def getdollar():
    print(f"{myslider2.get()}dollars have been delivered")
    tmsg.showinfo("Amount Deliverd",f"{myslider2.get()}dollars have been delivered")


root=Tk()
root.geometry("455x233")
root.title("Slider")
# myslider=Scale(root,from_=0,to=100)
# myslider.pack()
Label(root,text="how many dollars do you want?").pack()
myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(10)

myslider2.pack()
Button(root,text="Get dollars",command=getdollar).pack()
root.mainloop()
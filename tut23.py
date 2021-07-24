from tkinter import *
root=Tk()
root.geometry("455x233")
root.title("Window resizer gui")
def update():
    print("updating the gui")
    root.geometry(f"{width.get()}x{height.get()}")
width=StringVar()
height=StringVar()
Entry(root,textvariable=width).pack()
Entry(root,textvariable=height).pack()
Button(root,text="apply",command=update).pack()
root.mainloop()
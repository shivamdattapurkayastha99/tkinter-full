from tkinter import *
root=Tk()
root.geometry("733x566")
root.title("Shivam's IDE")
def myfunc():
    print("It is working")
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

root.mainloop()
from tkinter import *
root=Tk()
root.geometry("455x233")
root.title("status bar")
def upload():
    statusvar.set("Busy")
    sbar.update()
    import time
    time.sleep(3)
    statusvar.set("Ready")
statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=upload).pack()
root.mainloop()
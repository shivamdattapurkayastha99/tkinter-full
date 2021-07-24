from tkinter import *
root=Tk()
root.geometry("444x233")
root.title("my gui with shivam")
# important label options
# bd-background
# fg-foreground
# font-sets the font
# padx-xpadding
# pady-ypadding
# releif-borderstyling-SUNKEN,RAISED,GROOVE,RIDGE
title_label=Label(text="my name is shivam",bg="red",fg="white",padx=23,pady=94,font="comicsansms 19 bold",borderwidth=3,relief=SUNKEN)
# title_label.pack(anchor="nw")
# title_label.pack(side=BOTTOM,anchor="sw")
# title_label.pack(side=BOTTOM,anchor="sw",fill=X)
title_label.pack(side=LEFT,fill=Y,padx=34,pady=34)

root.mainloop()
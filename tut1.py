from tkinter import *
from PIL import Image,ImageTk
root=Tk()
# gui logic
root.geometry("644x534")

# widthxheight
# root.minsize(300,100)
# # width,height
# root.maxsize(1200,988)
# label=Label(text="shivam is a good boy")
# label.pack()
photo=PhotoImage(file="shivam1.png")
label=Label(image=photo)
label.pack()







root.mainloop()


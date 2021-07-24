from tkinter import *
root=Tk()
root.geometry("655x444")
root.title("title")
root.configure(background="blue")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
print(f"{width}x{height}")
Button(text="close",command=root.destroy).pack()

root.mainloop()
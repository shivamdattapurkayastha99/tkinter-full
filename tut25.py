from tkinter import *
class GUI(Tk):
# self is root 
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvar=self.var,relief=SUNKEN,anchor="w").pack(side=BOTTOM,fill=X)
    def createButton(self,inptext):
        Button(text=inptext,command=self.click).pack()
    def click(self):
        print("Button clicked")
if __name__ == "__main__":
    window=GUI()
    # window is root
    window.status()
    window.createButton("Click me")
    window.mainloop()

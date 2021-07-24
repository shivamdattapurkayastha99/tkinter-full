from tkinter import *
def shivam(event):
    print(f"you clicked at {event.x},{event.y}")
root=Tk()
canvas_width=644
canvas_height=334

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Shivam da event")
widget=Button(root,text="click me")
widget.pack()
widget.bind('<Button-1>',shivam)
widget.bind('<Double-1>',quit)
root.mainloop()
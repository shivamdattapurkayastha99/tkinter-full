from tkinter import *
root=Tk()
canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Shivam da dhaba")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()
can_widget.create_line(0,200,800,0,fill="blue")
can_widget.create_rectangle(3,5,700,300,fill="blue")
can_widget.create_text(200,200,text="shivam is best")
can_widget.create_oval(3,5,700,300,fill="yellow")
img=PhotoImage(file="shivam1.png")
can_widget.create_image(165,20,image=img)
root.mainloop()
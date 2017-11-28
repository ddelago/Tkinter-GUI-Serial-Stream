import tkinter
root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.pack()

def moved(event):
    canvas.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))

canvas.bind("<Motion>", moved)
tag = canvas.create_text(10, 10, text="", anchor="nw")  

root.mainloop()
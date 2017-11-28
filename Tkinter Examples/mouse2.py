from tkinter import *

class App():
    def __init__(self):
        root = Tk()

        self.last_point = (0, 0)

        self.prev_var = StringVar(value='-:-')
        self.curr_var = StringVar(value='-:-')

        labels = Frame(root)
        labels.pack()

        Label(labels, text='Last Point Clicked: ').pack(side=LEFT)
        prev = Label(labels, textvariable=self.prev_var)
        prev.pack(side=LEFT)
        Label(labels, text='Current point: ').pack(side=LEFT)
        curr = Label(labels, textvariable=self.curr_var)
        curr.pack(side=LEFT)

        self.canvas = Canvas(root, background='white')
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.on_click)

        self.canvas.bind('<Motion>', self.on_motion)
        self.line = self.canvas.create_line(0, 0, 0, 0)
        self.curr_text = self.canvas.create_text(0, 0)

        root.mainloop()
    def on_click(self, event):
        # Last click in absolute coordinates
        self.prev_var.set('%s:%s' % self.last_point)
        # Current point in relative coordinates
        self.curr_var.set('%s:%s' % (event.x - self.last_point[0], event.y - self.last_point[1]))
        self.last_point = event.x, event.y
    def on_motion(self, event):
        self.canvas.coords(self.line, self.last_point[0], self.last_point[1], event.x, event.y)
        self.canvas.coords(self.curr_text, event.x, event.y)
        self.canvas.itemconfigure(self.curr_text, text="%s\n%s\n\n\n" % (event.x - self.last_point[0], event.y - self.last_point[1]))

App()
from tkinter import *
import threading, time

class Threader(threading.Thread):

    def __init__(self, *args, **kwargs):

        threading.Thread.__init__(self, *args, **kwargs)
        self.daemon = True
        self.start()

    def run(self):

         while True:
            print("Look a while true loop that doesn't block the GUI!")
            print("Current Thread: %s" % self.name)
            time.sleep(1)

if __name__ == '__main__':

    root = Tk()
    leftFrame = Frame(root)
    leftFrame.pack(side=LEFT)
    rightFrame = Frame(root)
    rightFrame.pack(side=RIGHT)
    playButton = Button(leftFrame, text="Play", fg="blue", 
        command= lambda: Threader(name='Play-Thread'))
    stopButton = Button(rightFrame, text="Stop", fg="red", 
        command= lambda: Threader(name='Stop-Thread'))
    playButton.pack(side=TOP)
    stopButton.pack(side=BOTTOM)
    root.mainloop()
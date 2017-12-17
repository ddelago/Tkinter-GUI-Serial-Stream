#!/usr/bin/python
from Tkinter import *
import ttk
import ScrolledText

def demo():
    main = Tk()
    main.title('Notebook Demo')
    main.geometry('500x500')

    # gives weight to the cells in the grid
    rows = 0
    while rows < 50:
        main.rowconfigure(rows, weight=1)
        main.columnconfigure(rows, weight=1)
        rows += 1
     
    # Defines and places the notebook widget
    nb = ttk.Notebook(main)
    nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
     
    # Adds tab 1 of the notebook
    page1 = ttk.Frame(nb)
    nb.add(page1, text='Live Stream')
     
    # Adds tab 2 of the notebook
    page2 = ttk.Frame(nb)    
    nb.add(page2, text='Discretes')

    # Adds tab 2 of the notebook
    page3 = ttk.Frame(nb)    
    nb.add(page3, text='ARINC-429')

    # Adds tab 2 of the notebook
    page4 = ttk.Frame(nb)    
    nb.add(page4, text='Extended Squitter')
    
    main.mainloop()
 

if __name__ == "__main__":
    demo()
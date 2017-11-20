#!/usr/bin/env python
# Daniel Delago
# ddelago0596@gmail.com
# GUI that displays live transponder data
#!/usr/bin/python
from Tkinter import *
import ttk

def demo():
    main = Tk()
    main.title('Transponder Stream')
    main.geometry('800x600')

    # gives weight to the cells in the grid
    rows = 0
    while rows < 50:
        main.rowconfigure(rows, weight=1)
        main.columnconfigure(rows, weight=1)
        rows += 1
     
    # Defines and places the notebook widget
    nb = ttk.Notebook(main)
    nb.grid(row=0, column=0, columnspan=50, rowspan=49, sticky='NESW')
     
    # Adds tab 0 of the notebook
    page0 = ttk.Frame(nb)
    nb.add(page0, text='Home')

    # Adds tab 1 of the notebook
    page1 = ttk.Frame(nb)
    nb.add(page1, text='Serial Stream')
     
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
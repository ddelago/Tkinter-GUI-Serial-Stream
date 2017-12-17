#!/usr/bin/env python
# Daniel Delago
# ddelago0596@gmail.com
from Tkinter import *
import ttk
import serial
from random import *
import time

# /dev/pts/## is a virtual serial port used for simulating a live serial stream. See README.
ser = serial.Serial('/dev/pts/21')
ser.baudrate = 9600

# Creates GUI
def GUI():
    main = Tk()
    main.title('Transponder Stream')
    main.geometry('800x600')

    # gives weight to the cells in the grid
    rows = 0
    while rows < 45:
        main.rowconfigure(rows, weight=1)
        main.columnconfigure(rows, weight=1)
        rows += 1

    ### Drop-down Menus ###
    menu = Menu(main)
    main.config(menu=menu)

    fileMenu = Menu(menu)
    menu.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New Project...", command=doNothing)
    fileMenu.add_command(label="New...", command=doNothing)
    fileMenu.add_command(label="New...", command=doNothing)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=doNothing)

    editMenu = Menu(menu)
    menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Redo", command=doNothing)


    toolsMenu = Menu(menu)
    menu.add_cascade(label="Tools", menu=toolsMenu)
    toolsMenu.add_command(label="Select Port", command=doNothing)
    toolsMenu.add_command(label="New...", command=doNothing)
    toolsMenu.add_command(label="New...", command=doNothing)

    ### Tabs ###
    nb = ttk.Notebook(main)
    tabs = create_tabs(nb)

    ### Update GUI ###
    while(True):
        update_GUI(main, nb, tabs)
        time.sleep(.1)

    main.mainloop()

# Temp function for drop-down menus
def doNothing():
    print("Nothing")

# Add tabs to GUI
def create_tabs(nb):
    # Defines and places the notebook widget
    nb.grid(row=0, column=0, columnspan=50, rowspan=30, sticky='NESW')
     
    ##### Home #####
    page0 = ttk.Frame(nb)

    # Home Labels
    home_label0 = Label(page0, text="").grid(row=0, column=0, padx=4, sticky='W')
    home_label1 = Label(page0, text="Home", font=(None,14)).grid(row=1,column=0, padx=4, sticky="W")

    # Add tab to notebook
    nb.add(page0, text='Tab 1')
    
    ##### Page 1 #####
    page1 = ttk.Frame(nb) 
    
    # First Column of Labels
    discrete_label0 = Label(page1, text="").grid(row=0, column=0, padx=4, sticky='W')
    discrete_label1 = Label(page1, text="Title One", font=(None,14)).grid(row=1,column=0, padx=4, sticky="W")
    discrete_label2 = Label(page1, text="Label:").grid(row=2,column=0, padx=4, sticky='W')
    discrete_label3 = Label(page1, text="Label:").grid(row=3,column=0, padx=4, sticky='W')
    discrete_label4 = Label(page1, text="Label:").grid(row=4,column=0, padx=4, sticky='W')
    discrete_label5 = Label(page1, text="Label:").grid(row=5,column=0, padx=4, sticky='W')       
    discrete_label6 = Label(page1, text="Label:").grid(row=6,column=0, padx=4, sticky='W')

    # First Column of Labels
    discrete_label7 = Label(page1, text="").grid(row=7,column=0, padx=4, sticky='W')
    discrete_label8 = Label(page1, text="Title Two:", font=(None,14)).grid(row=8,column=0, padx=4, sticky="W")
    discrete_label9 = Label(page1, text="Label:").grid(row=9,column=0, padx=4, sticky='W')
    discrete_label10 = Label(page1, text="Label:").grid(row=10,column=0, padx=4, sticky='W')
    discrete_label11 = Label(page1, text="Label:").grid(row=11,column=0, padx=4, sticky='W')
    discrete_label12 = Label(page1, text="Label:").grid(row=12,column=0, padx=4, sticky='W')

    # Table 1 Values
    nb.discrete_value2 = Label(page1, text="N/A")
    nb.discrete_value2.grid(row=2,column=1, padx=4, sticky='W')
    nb.discrete_value3 = Label(page1, text="N/A")
    nb.discrete_value3.grid(row=3,column=1, padx=4, sticky='W')
    nb.discrete_value4 = Label(page1, text="N/A")
    nb.discrete_value4.grid(row=4,column=1, padx=4, sticky='W')
    nb.discrete_value5 = Label(page1, text="N/A")
    nb.discrete_value5.grid(row=5,column=1, padx=4, sticky='W')        
    nb.discrete_value6 = Label(page1, text="N/A")
    nb.discrete_value6.grid(row=6,column=1, padx=4, sticky='W')            

    # Table 2 Values
    nb.discrete_value9 = Label(page1, text="N/A")
    nb.discrete_value9.grid(row=9,column=1, padx=4, sticky='W')
    nb.discrete_value10 = Label(page1, text="N/A")
    nb.discrete_value10.grid(row=10,column=1, padx=4, sticky='W')
    nb.discrete_value11 = Label(page1, text="N/A")
    nb.discrete_value11.grid(row=11,column=1, padx=4, sticky='W')
    nb.discrete_value12 = Label(page1, text="N/A")
    nb.discrete_value12.grid(row=12,column=1, padx=4, sticky='W')

    # Button
    nb.home_button0 = Button(page1, text='Quit', command=doSomething("Hello"))
    nb.home_button0.grid(row=14, column=0, padx=4, sticky='W')

    # Add tab to notebook
    nb.add(page1, text='Tab 2')

    ##### ARINC #####
    page2 = ttk.Frame(nb)    
    nb.add(page2, text='Tab 3')

    ##### Extended Squitter #####
    page3 = ttk.Frame(nb)
    nb.add(page3, text='Tab 4')

    return [page0, page1, page2, page3]

# Gets message from stream and updates tabs 
def update_GUI(main, nb, tabs):
    # Update GUI
    main.update()

    # Generate randome values to display
    message = random()

    # Update tab data that the GUI is currently viewing
    update_tabs(nb, nb.index("current"), tabs[nb.index("current")], message)

# Populate Tabs
def update_tabs(nb,page_num, page, message):

    temp_value = message

    # Discrete message
    if(page is not None): 
        nb.discrete_value2.config(text=temp_value)
        nb.discrete_value3.config(text=temp_value)
        nb.discrete_value4.config(text=temp_value)
        nb.discrete_value5.config(text=temp_value)
        nb.discrete_value6.config(text=temp_value)
        nb.discrete_value9.config(text=temp_value)
        nb.discrete_value10.config(text=temp_value)
        nb.discrete_value11.config(text=temp_value)
        nb.discrete_value12.config(text=temp_value)

# Main
if __name__ == "__main__":
    # Begin GUI and Serial Stream
    GUI()

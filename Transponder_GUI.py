#!/usr/bin/env python
# Daniel Delago
# ddelago0596@gmail.com
# This file reads a stream of data representing aircraft in the ARINC 429 data format and decodes those messages and displays on a GUI.
import Transponder_Decoder
from Tkinter import *
import ttk
from PIL import Image, ImageTk
import serial
import time
import datetime


# /dev/pts/21 is a virtual serial port used for simulating a live serial stream. See README.
# ser = serial.Serial('/dev/pts/21')
# ser.baudrate = 9600
ser = serial.Serial()

# Serial Port chosen boolean
ser_bool = False

# Create GUI Window
main = Tk()
main.title('Transponder Stream')
main.geometry('800x600')

# Create NoteBook for tabs
nb = ttk.Notebook(main)


# Creates GUI
def GUI(log_file):
    # gives weight to the cells in the grid
    rows = 0
    while rows < 45:
        main.rowconfigure(rows, weight=1)
        main.columnconfigure(rows, weight=1)
        rows += 1
    # main.rowconfigure(0, weight=1)
    # main.columnconfigure(0, weight=1)

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
    tabs = create_tabs(nb)

    ### Update GUI ###
    while(True):
        update_GUI(main, nb, tabs, log_file)

# Temp function for drop-down menus
def doNothing():
    print("Nothing")

# Attempts to open serial port entered
def serial_open():
    global ser_bool, ser

    try:
        ser = serial.Serial(nb.home_entry0.get())
        ser.baudrate = nb.home_entry1.get()
        ser_bool = True
    except:
        ser_bool = False
        print("Serial port not available.")

# Attempts to open serial port entered
def serial_close():
    global ser_bool
    ser_bool = False
    print("Port Closed")


# Add tabs to GUI
def create_tabs(nb):
    # Defines and places the notebook widget
    nb.grid(row=0, column=0, columnspan=50, rowspan=30, sticky='NESW')
     
    ##### Home #####
    page0 = ttk.Frame(nb)

    # Image
    img = Image.open("Nasa-Logo-Transparent-Background-download.png")
    img = img.resize((94,78),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(page0, image = img)
    panel.image = img
    # panel.grid(row=0, column=0, padx=1, pady=4, sticky="W")

    # Home Labels
    # home_label0 = Label(page0, text="").grid(row=0, column=0, padx=4, sticky='W')
    home_label1 = Label(page0, text="Home", font=(None,14)).grid(row=1,column=0, padx=4, sticky="W")
    home_label2 = Label(page0, text="Specify the desination you want to connect to:").grid(row=2,column=0, padx=4, sticky='W')
    home_label3 = Label(page0, text="Serial Line").grid(row=3,column=0, padx=4, sticky='W')
    home_label4 = Label(page0, text="Speed").grid(row=3,column=1, padx=4, sticky='W')
    home_label5 = Label(page0, text="Incoming Message:").grid(row=6,column=0, padx=4, sticky='W')
    
    # Entry widgets for Serial Port and Speed
    nb.home_entry0 = Entry(page0)
    nb.home_entry1 = Entry(page0)
    
    # Insert placeholder text
    nb.home_entry0.insert(0,'/dev/ttyS0')    
    nb.home_entry1.insert(0,'9600')

    # Display onto GUI
    nb.home_entry0.grid(row=4,column=0, padx=4, sticky='W')
    nb.home_entry1.grid(row=4,column=1, padx=4, sticky='W')

    # Button Open Serial
    nb.home_button0 = Button(page0, text='Open Port', command=serial_open)
    nb.home_button0.grid(row=5,column=0, padx=4, sticky='W')

    # Button Close Serial
    nb.home_button1 = Button(page0, text='Close Port', command=serial_close)
    nb.home_button1.grid(row=5,column=1, padx=4, sticky='W')


    # Home Values
    nb.home_value0 = Label(page0, text="N/A")
    nb.home_value0.grid(row=6,column=1, padx=4, sticky='W')

    # Add tab to notebook
    nb.add(page0, text='Home')
    
    ##### Discretes #####
    page1 = ttk.Frame(nb) 
    
    # First Column of Discrete Labels
    discrete_label0 = Label(page1, text="").grid(row=0, column=0, padx=4, sticky='W')
    discrete_label1 = Label(page1, text="Discretes", font=(None,14)).grid(row=1,column=0, padx=4, sticky="W")
    discrete_label2 = Label(page1, text="Air/Gnd 2:").grid(row=2,column=0, padx=4, sticky='W')
    discrete_label3 = Label(page1, text="Air/Gnd 1:").grid(row=3,column=0, padx=4, sticky='W')
    discrete_label4 = Label(page1, text="Alt Source Sel:").grid(row=4,column=0, padx=4, sticky='W')
    discrete_label5 = Label(page1, text="Standby/On:").grid(row=5,column=0, padx=4, sticky='W')       
    discrete_label6 = Label(page1, text="Selected GPS:").grid(row=6,column=0, padx=4, sticky='W')

    # First Column of Variable Labels
    discrete_label7 = Label(page1, text="").grid(row=7,column=0, padx=4, sticky='W')
    discrete_label8 = Label(page1, text="Variables:", font=(None,14)).grid(row=8,column=0, padx=4, sticky="W")
    discrete_label9 = Label(page1, text="Air/Gnd:").grid(row=9,column=0, padx=4, sticky='W')
    discrete_label10 = Label(page1, text="PP Config Avail:").grid(row=10,column=0, padx=4, sticky='W')
    discrete_label11 = Label(page1, text="ADS-B Fail:").grid(row=11,column=0, padx=4, sticky='W')
    discrete_label12 = Label(page1, text="XPDR Fail:").grid(row=12,column=0, padx=4, sticky='W')
    discrete_label13 = Label(page1, text="").grid(row=13, column=0, padx=4, sticky='W')
    discrete_label14 = Label(page1, text="Raw Message Received:").grid(row=14,column=0, padx=4, sticky='W')
    discrete_label15 = Label(page1, text="Decoded Message Received:").grid(row=15,column=0, padx=4, sticky='W')

    # Discretes Values
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

    # Variables Values
    nb.discrete_value9 = Label(page1, text="N/A")
    nb.discrete_value9.grid(row=9,column=1, padx=4, sticky='W')
    nb.discrete_value10 = Label(page1, text="N/A")
    nb.discrete_value10.grid(row=10,column=1, padx=4, sticky='W')
    nb.discrete_value11 = Label(page1, text="N/A")
    nb.discrete_value11.grid(row=11,column=1, padx=4, sticky='W')
    nb.discrete_value12 = Label(page1, text="N/A")
    nb.discrete_value12.grid(row=12,column=1, padx=4, sticky='W')
    nb.discrete_value13 = Label(page1, text="N/A")
    nb.discrete_value13.grid(row=14,column=1, padx=4, sticky='W')
    nb.discrete_value14 = Label(page1, text="N/A")
    nb.discrete_value14.grid(row=15,column=1, padx=4, sticky='W')

    # Add tab to notebook
    nb.add(page1, text='Discretes')

    ##### ARINC #####
    page2 = ttk.Frame(nb)    
    nb.add(page2, text='ARINC-429')

    ##### Extended Squitter #####
    page3 = ttk.Frame(nb)
    nb.add(page3, text='Extended Squittere')

    return [page0, page1, page2, page3]

# Gets message from stream and updates tabs 
def update_GUI(main, nb, tabs, log_file):
    # Update GUI
    main.update()

    # Serial message variable
    message = ""

    # If a serial port has been opened or not
    if(ser_bool):
        # If port successfully opened, get message
        message = read_stream(ser)

        # Update tab data that the GUI is currently viewing
        update_tabs(nb, nb.index("current"), tabs[nb.index("current")], message)

# Read Serial Stream
def read_stream(ser):
    # Store decoded serial message
    serial_message = ser.readline().decode().strip()

    # Read message from stream
    message = Transponder_Decoder.decode_stream(serial_message, log_file)

    # Return decoded message
    return message

# Populate Tabs
def update_tabs(nb,page_num, page, message):
    # Print raw hex value for debugging
    nb.home_value0.config(text=message[1])

    # Get Decoded Binary List
    bin_list = message[0]

    # Discrete message
    if((bin_list is not None) and (page is not None) and (len(bin_list) == 16)): 
        # Discretes
        if (bin_list[0] == 1): 
            nb.discrete_value2.config(text="In-Air")
        elif (bin_list[0] == 0):
            nb.discrete_value2.config(text="On-Ground")

        if (bin_list[1] == 1): 
            nb.discrete_value3.config(text="In-Air")
        elif (bin_list[1] == 0):
            nb.discrete_value3.config(text="On-Ground")

        if (bin_list[2] == 1): 
            nb.discrete_value4.config(text="ADC 1")
        elif (bin_list[2] == 0):
            nb.discrete_value4.config(text="ADC 2")

        if (bin_list[3] == 1): 
            nb.discrete_value5.config(text="On")     
        elif (bin_list[3] == 0):
            nb.discrete_value5.config(text="Standby")   

        if (bin_list[8] == 1): 
            nb.discrete_value6.config(text="GPS 2")      
        elif (bin_list[8] == 0):
            nb.discrete_value6.config(text="GPS 1")        

        # Variables
        if (bin_list[4] == 1): 
            nb.discrete_value9.config(text="On-Ground")
        elif (bin_list[4] == 0):
            nb.discrete_value9.config(text="In-Air")

        if (bin_list[5] == 1): 
            nb.discrete_value10.config(text="Avail")
        elif (bin_list[5] == 0):
            nb.discrete_value10.config(text="Not Avail")

        if (bin_list[6] == 1): 
            nb.discrete_value11.config(text="Failed")
        elif (bin_list[6] == 0):
            nb.discrete_value11.config(text="Not Fail")

        if (bin_list[7] == 1): 
            nb.discrete_value12.config(text="Failed")
        elif (bin_list[7] == 0):
            nb.discrete_value12.config(text="Not Fail")

        # Display Raw Values
        nb.discrete_value13.config(text=message[1])
        nb.discrete_value14.config(text=bin_list)

    # ARINC message
    elif((bin_list is not None) and (page is not None) and (len(bin_list) == 32)):
        print("ARINC")

    # Extended Squitter message
    elif((bin_list is not None) and (page is not None) and (len(bin_list) == 56)):
        print("ES")

# Main
if __name__ == "__main__":
    # Get System Date and Time
    sys_date_time = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    sys_time = str(datetime.datetime.now().time())

    # Log File Name: Year-Month-Day_Hour:Minute:Second_log.txt
    filename = sys_date_time + '_log.txt'

    # Create log file
    log_file = open('flight_logs/' + filename,'w+')
    
    # Begin GUI and Serial Stream
    GUI(log_file)

    # Close File
    log_file.close()
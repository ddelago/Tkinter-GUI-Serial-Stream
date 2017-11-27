#!/usr/bin/env python
# Daniel Delago
# ddelago0596@gmail.com
# This file reads a stream of data representing aircraft in the ARINC 429 data format and decodes those messages and displays on a GUI.
import serial
import time
import datetime
from Tkinter import *
import ttk

ser = serial.Serial('/dev/pts/21')
ser.baudrate = 9600

# Temp function
def doNothing():
    print("Nothing")

# Gets message from stream and updates tabs 
def update_GUI(main, nb, log_file, updated):
    # Update GUI
    main.update()

    # Read message from stream
    message = read_stream(log_file)

    # Update tab data (Am currently printing the same data to all pages thats why they are identical)
    update_tabs(nb, nb.select(1), message, updated)

    # Loop
    main.after(0, update_GUI(main, nb, log_file, 1))

# Creates GUI
def GUI(log_file):
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

    ### Tabs ###
    nb = ttk.Notebook(main)
    nb = create_tabs(nb)

    ### Update GUI ###
    main.after(0, update_GUI(main, nb, log_file, 0))
    main.mainloop()

# Add tabs to GUI
def create_tabs(nb):
    # Defines and places the notebook widget
    nb.grid(row=0, column=0, columnspan=50, rowspan=30, sticky='NESW')
     
    # Home
    page1 = ttk.Frame(nb)
    nb.add(page1, text='Home')
    
    # Discrete
    page2 = ttk.Frame(nb) 
    nb.add(page2, text='Discretes')

    # ARINC
    page3 = ttk.Frame(nb)    
    nb.add(page3, text='ARINC-429')

    # Extended Squitter
    page4 = ttk.Frame(nb)
    nb.add(page4, text='Extended Squitter')

    return nb


# Populate Tabs
def update_tabs(nb, page, bin_list, updated):
    # Only update to screen once
    if(updated == 0):
        # First Column of Discrete Fields
        Label(page, text="").grid(row=0, column=0, padx=4, sticky='W')
        Label(page, text="Discretes", font=(None,14)).grid(row=1,column=0, padx=4, sticky="W")
        Label(page, text="Air/Gnd 2:").grid(row=2,column=0, padx=4, sticky='W')
        Label(page, text="Air/Gnd 1:").grid(row=3,column=0, padx=4, sticky='W')
        Label(page, text="Alt Source Sel:").grid(row=4,column=0, padx=4, sticky='W')
        Label(page, text="Standby/On:").grid(row=5,column=0, padx=4, sticky='W')       
        Label(page, text="Selected GPS:").grid(row=6,column=0, padx=4, sticky='W')

        # First Column of Variable Fields
        Label(page, text="").grid(row=7,column=0, padx=4, sticky='W')
        Label(page, text="Variables:", font=(None,14)).grid(row=8,column=0, padx=4, sticky="W")
        Label(page, text="Air/Gnd:").grid(row=9,column=0, padx=4, sticky='W')
        Label(page, text="PP Config Avail:").grid(row=10,column=0, padx=4, sticky='W')
        Label(page, text="ADS-B Fail:").grid(row=11,column=0, padx=4, sticky='W')
        Label(page, text="XPDR Fail:").grid(row=12,column=0, padx=4, sticky='W')

    # If Empty List
    if(bin_list is not None): 
        # Discretes
        # Discrete: Air/Gnd 2       = bit 1     VALUES: 1=In-Air,    0=On-Ground
        # Discrete: Air/Gnd 1       = bit 2     VALUES: 1=In-Air,    0=On-Ground
        # Discrete: Alt Source Sel  = bit 3     VALUES: 1=ADC 1,     0=ADC 2
        # Discrete: Standby/On      = bit 4     VALUES: 1=On,        0=Standby
        # Discrete: Sel GPS         = bit 9     VALUES: 1=GPS2,      0=GPS1

        if (bin_list[0] == 1): 
            Label(page, text="In-Air").grid(row=2,column=1, padx=4, sticky='W')
        elif (bin_list[0] == 0):
            Label(page, text="On-Ground").grid(row=2,column=1, padx=4, sticky='W')

        if (bin_list[1] == 1): 
            Label(page, text="In-Air").grid(row=3,column=1, padx=4, sticky='W')
        elif (bin_list[1] == 0):
            Label(page, text="On-Ground").grid(row=3,column=1, padx=4, sticky='W')

        if (bin_list[2] == 1): 
            Label(page, text="ADC 1").grid(row=4,column=1, padx=4, sticky='W')
        elif (bin_list[2] == 0):
            Label(page, text="ADC 2").grid(row=4,column=1, padx=4, sticky='W')

        if (bin_list[3] == 1): 
            Label(page, text="On").grid(row=5,column=1, padx=4, sticky='W')       
        elif (bin_list[3] == 0):
            Label(page, text="Standby").grid(row=5,column=1, padx=4, sticky='W')     

        if (bin_list[8] == 1): 
            Label(page, text="GPS 2").grid(row=6,column=1, padx=4, sticky='W')       
        elif (bin_list[8] == 0):
            Label(page, text="GPS 1").grid(row=6,column=1, padx=4, sticky='W')         

        # Variables
        # Variable: Air/Gnd         = bit 5     VALUES: 1=On-Ground, 0=In-Air
        # Variable: PP Config Avail = bit 6     VALUES: 1=Avail,     0=Not Avail
        # Variable: ADS-B Fail      = bit 7     VALUES: 1=Failed,    0=Not Fail
        # Variable: XPDR Fail       = bit 8     VALUES: 1=Failed,    0=Not Fail

        if (bin_list[4] == 1): 
            Label(page, text="On-Ground").grid(row=9,column=1, padx=4, sticky='W')
        elif (bin_list[4] == 0):
            Label(page, text="In-Air").grid(row=9,column=1, padx=4, sticky='W')

        if (bin_list[5] == 1): 
            Label(page, text="Avail").grid(row=10,column=1, padx=4, sticky='W')
        elif (bin_list[5] == 0):
            Label(page, text="Not Avail").grid(row=10,column=1, padx=4, sticky='W')

        if (bin_list[6] == 1): 
            Label(page, text="Failed").grid(row=11,column=1, padx=4, sticky='W')
        elif (bin_list[6] == 0):
            Label(page, text="Not Fail").grid(row=11,column=1, padx=4, sticky='W')

        if (bin_list[7] == 1): 
            Label(page, text="Failed").grid(row=12,column=1, padx=4, sticky='W')
        elif (bin_list[7] == 0):
            Label(page, text="Not Fail").grid(row=12,column=1, padx=4, sticky='W')
    else:
        print("Exception")

    return page


########### DECODER CODE BELOW ###########

# Read serial stream
def read_stream(log_file):
    # Store decoded serial message
    message = ser.readline().decode().strip()
    
    # Update Time
    sys_time = str(datetime.datetime.now().time())
    
    # Write time-stamped message to log file
    log_file.write(sys_time + ' ' + message + '\n')

    # Print raw message for debugging
    # print(message)

    # If a Discrete Message
    if(len(message)==6):
        message = decode_discrete(message)

    # If an ARINC Message
    elif(len(message)==10):
        message = decode_ARINC(message)

    # If an Extended Squitter Message
    elif(len(message)==16):
        message = decode_ES(message)

    return message

# Decode Discrete messages
def decode_discrete(hexstr):
    # Convert hex message to binary
    hexstr = hexstr[2:]
    binstr = bin(int(hexstr,16))
    binstr = binstr[2:]

    # Converts binstr to list of ints (1's and 0's)
    bin_list = list(map(int,binstr))

    # Print decoded message for debugging
    # print(bin_list)

    return bin_list

# Decode ARINC-429 messages
def decode_ARINC(hexstr):
    # Temp Message
    # print("ARINC Message Received")
    return

# Decode Extended Squitter messages
def decode_ES(hexstr):
    # Temp Message
    # print("Extended Squitter Message Received")
    return
 
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
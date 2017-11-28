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
def update_GUI(main, nb, tabs, log_file, updated):
    # Update GUI
    main.update()

    # Read message from stream
    message = read_stream(log_file)

    # Update tab data
    update_tabs(nb.index("current"), tabs[nb.index("current")], message, updated)

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
    tabs = create_tabs(nb)

    ### Update GUI ###
    updated = 0
    while(True):
        update_GUI(main, nb, tabs, log_file, updated)
        updated = 1
    # main.bind("<Motion>", update_GUI(main, nb, tabs, log_file, 0))

    main.mainloop()

# Add tabs to GUI
def create_tabs(nb):
    # Defines and places the notebook widget
    nb.grid(row=0, column=0, columnspan=50, rowspan=30, sticky='NESW')
     
    ##### Home #####
    page0 = ttk.Frame(nb)
    nb.add(page0, text='Home')
    
    ##### Discretes #####
    page1 = ttk.Frame(nb) 
    
    # First Column of Discrete Fields
    page1.label0 = Label(page1, text="").grid(row=0, column=0, padx=4, sticky='W')
    page1.label1 = Label(page1, text="Discretes", font=(None,14)).grid(row=1,column=0, padx=4, sticky="W")
    page1.label2 = Label(page1, text="Air/Gnd 2:").grid(row=2,column=0, padx=4, sticky='W')
    page1.label3 = Label(page1, text="Air/Gnd 1:").grid(row=3,column=0, padx=4, sticky='W')
    page1.label4 = Label(page1, text="Alt Source Sel:").grid(row=4,column=0, padx=4, sticky='W')
    page1.label5 = Label(page1, text="Standby/On:").grid(row=5,column=0, padx=4, sticky='W')       
    page1.label6 = Label(page1, text="Selected GPS:").grid(row=6,column=0, padx=4, sticky='W')

    # First Column of Variable Fields
    page1.label7 = Label(page1, text="").grid(row=7,column=0, padx=4, sticky='W')
    page1.label8 = Label(page1, text="Variables:", font=(None,14)).grid(row=8,column=0, padx=4, sticky="W")
    page1.label9 = Label(page1, text="Air/Gnd:").grid(row=9,column=0, padx=4, sticky='W')
    page1.label10 = Label(page1, text="PP Config Avail:").grid(row=10,column=0, padx=4, sticky='W')
    page1.label11 = Label(page1, text="ADS-B Fail:").grid(row=11,column=0, padx=4, sticky='W')
    page1.label12 = Label(page1, text="XPDR Fail:").grid(row=12,column=0, padx=4, sticky='W')

    # Discretes Values
    page1.value2 = Label(page1, text="N/A").grid(row=2,column=1, padx=4, sticky='W')
    page1.value3 = Label(page1, text="N/A").grid(row=3,column=1, padx=4, sticky='W')
    page1.value4 = Label(page1, text="N/A").grid(row=4,column=1, padx=4, sticky='W')
    page1.value5 = Label(page1, text="N/A").grid(row=5,column=1, padx=4, sticky='W')        
    page1.value6 = Label(page1, text="N/A").grid(row=6,column=1, padx=4, sticky='W')            

    # Variables Values
    page1.value9 = Label(page1, text="N/A").grid(row=9,column=1, padx=4, sticky='W')
    page1.value10 = Label(page1, text="N/A").grid(row=10,column=1, padx=4, sticky='W')
    page1.value11 = Label(page1, text="N/A").grid(row=11,column=1, padx=4, sticky='W')
    page1.value12 = Label(page1, text="N/A").grid(row=12,column=1, padx=4, sticky='W')

    # Add tab to notebook
    nb.add(page1, text='Discretes')

    ##### ARINC #####
    page2 = ttk.Frame(nb)    
    nb.add(page2, text='ARINC-429')

    ##### Extended Squitter #####
    page3 = ttk.Frame(nb)
    nb.add(page3, text='Extended Squitter')

    return [page0, page1, page2, page3]


# Populate Tabs
def update_tabs(page_num, page, bin_list, updated):

    # Discrete message
    if((bin_list is not None) and (len(bin_list) == 16)): 
        # Discretes
        if (bin_list[0] == 1): 
            page.value2.config(text="In-Air")
        elif (bin_list[0] == 0):
            page.value2.config(text="On-Ground")

        if (bin_list[1] == 1): 
            page.value3.config(text="In-Air")
        elif (bin_list[1] == 0):
            page.value3.config(text="On-Ground")

        if (bin_list[2] == 1): 
            page.value4.config(text="ADC 1")
        elif (bin_list[2] == 0):
            page.value4.config(text="ADC 2")

        if (bin_list[3] == 1): 
            page.value5.config(text="On")     
        elif (bin_list[3] == 0):
            page.value5.config(text="Standby")   

        if (bin_list[8] == 1): 
            page.value6.config(text="GPS 2")      
        elif (bin_list[8] == 0):
            page.value6.config(text="GPS 1")        

        # Variables
        if (bin_list[4] == 1): 
            page.value9.config(text="On-Ground")
        elif (bin_list[4] == 0):
            page.value9.config(text="In-Air")

        if (bin_list[5] == 1): 
            page.value10.config(text="Avail")
        elif (bin_list[5] == 0):
            page.value10.config(text="Not Avail")

        if (bin_list[6] == 1): 
            page.value11.config(text="Failed")
        elif (bin_list[6] == 0):
            page.value11.config(text="Not Fail")

        if (bin_list[7] == 1): 
            page.value12.config(text="Failed")
        elif (bin_list[7] == 0):
            page.value12.config(text="Not Fail")

        print("ARINCCC")
    # ARINC message
    elif((bin_list is not None) and (len(bin_list) == 32)):
        print("ARINC")
    # Extended Squitter message
    elif((bin_list is not None) and (len(bin_list) == 56)):
        print("ES")

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

    # Discretes
    # Discrete: Air/Gnd 2       = bit 1     VALUES: 1=In-Air,    0=On-Ground
    # Discrete: Air/Gnd 1       = bit 2     VALUES: 1=In-Air,    0=On-Ground
    # Discrete: Alt Source Sel  = bit 3     VALUES: 1=ADC 1,     0=ADC 2
    # Discrete: Standby/On      = bit 4     VALUES: 1=On,        0=Standby
    # Discrete: Sel GPS         = bit 9     VALUES: 1=GPS2,      0=GPS1

    # Variables
    # Variable: Air/Gnd         = bit 5     VALUES: 1=On-Ground, 0=In-Air
    # Variable: PP Config Avail = bit 6     VALUES: 1=Avail,     0=Not Avail
    # Variable: ADS-B Fail      = bit 7     VALUES: 1=Failed,    0=Not Fail
    # Variable: XPDR Fail       = bit 8     VALUES: 1=Failed,    0=Not Fail

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
    # try:
    GUI(log_file)
    # except:
    #     print("Window Closed")

    # Close File
    log_file.close()
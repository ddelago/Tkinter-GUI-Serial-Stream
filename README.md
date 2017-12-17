# Transponder Serial Stream Decoder and GUI

## Introduction
This repository will explain the steps to monitoring and logging a transponder serial stream live inflight. 

Be sure to have the following installed:
- [Python 2.7](https://www.python.org/downloads/)
- [Tkinter](http://effbot.org/tkinterbook/tkinter-whats-tkinter.htm)
- [socat](https://www.howtoinstall.co/en/ubuntu/utopic/socat) (For simulating serial port while testing)
- [sublime](https://www.sublimetext.com/3) (Best text editor to use)
- [vmware](https://www.vmware.com/products/workstation-player.html) (For testing in linux environment if that is prefered)
  - [Ubuntu](https://www.ubuntu.com/download/desktop) (Will need Ubuntu image for virtual machine)

Tkinter Documentation
- http://effbot.org/tkinterbook/tkinter-index.htm#class-reference
- https://www.devdungeon.com/content/gui-programming-python
- https://smallguysit.com/index.php/category/python-programming/tkinter/
- http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
- http://www.tkdocs.com/tutorial/

## Setting up Virtual Serial Ports
- In a terminal enter the following command: 
- socat -d -d pty,raw,echo=0 pty,raw,echo=0
- This will create 2 virtual serial ports. 
- Whichever port you write to, can be read from the other port and vice versa.
- To test writing to port enter this in another terminal:
- echo "test string" > /dev/pts/#
- Now in another terminal enter:
- cat </dev/pts/#

## File Descriptions
- Tkinter Examples is a list of exmaple programs that can be used.
- flight_logs are the created timestamped logs
- ARINC_stream.py simulates the transponder by outputing dataRecording.txt to a virtual serial port.
- All Excel files are decoded data of a flight. Use them to write our own decoder. 
- flight_log_Tyler.txt is a flight log that also contains commands that were sent to the transponder. 
- Transponder_Decoder.py is where the decoding of the serial stream occurs.
- Transponder_GUI.py is where the GUI is created and updated. RUN THIS: python Transponder_GUI.py

## How It Works
1. Transponder_GUI.py main function gets the current system date and time and creates the log file for the flight. 
2. The log file is then passed to the GUI to begin recording.
3. GUI function first adds weight to the cells of the grid (change this to dynamically change with window size) then adds drop down menus and creates the tabs for the GUI. 
4. While loop at botton of GUI function is how the GUI updates.
5. update_GUI first updates the GUI window, then waits for a serial connection to be opened. ser_bool is a boolean value that tells if a serial connection is open or not.
6. update_tabs then updates the values of the message fields according to the decoded message being received.
7. To test GUI and decoder, create virtual serial ports using socat and run the ARINC_stream.py program 

## Future Work
- Finish the sections for ARINC 429  and Extended Squitter for the Transponder_Decoder.py program. These require hex to binary conversions as well as bit manipulations such as the reversing of the binary string. Ask Tyler Thompson for details. Use the Discrete decoder as a guide on how to return values so that it can be used by the GUI.
- Finish the ARINC 429 and Extended Squitter tabs on the GUI. Use the Discrete tab as a guide on how to format and display data. 
- Implement a way to send commands to the transponder. Commands such as DR to start the transponder stream or commands that will display various configuration data. See flight_log_Tyler.txt for details.
- Implement a window or terminal into the GUI that will show the serial stream live. 

## Contacts
- Tyler Thompson
- Daniel Delago (ddelago0596@gmail.com or daniel.b.delago@nasa.gov)

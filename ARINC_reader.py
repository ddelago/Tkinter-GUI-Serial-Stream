#!/usr/bin/env python
# Daniel Delago
# ddelago0596@gmail.com
# This file reads a stream of data representing aircraft in the ARINC 429 data format and decodes those messages.
import serial
import time
import datetime
from Tkinter import *

ser = serial.Serial('/dev/pts/21')
ser.baudrate = 9600

# Read serial stream
def read_stream():
	# Get System Date and Time
	sys_date_time = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
	sys_time = str(datetime.datetime.now().time())

	# Log File Name: Year-Month-Day_Hour:Minute:Second_log.txt
	filename = sys_date_time + '_log.txt'

	# Create log file
	file = open('flight_logs/' + filename,'w+')

	# Transponder message variable
	message = ""

	# Begin reading in stream
	while(1):
		# Store decoded serial message
		message = ser.readline().decode().strip()

		# Update Time
		sys_time = str(datetime.datetime.now().time())

		# Write time-stamped message to log file
		file.write(sys_time + ' ' + message + '\n')

		# Print message for debugging
		print(message)

		# If a Discrete Message
		if(len(message)==6):
			decode_discrete(message)

		# If an ARINC Message
		elif(len(message)==10):
			decode_ARINC(message)

		# If an Extended Squitter Message
		elif(len(message)==16):
			decode_ES(message)

	# Close File
	file.close()

# Decode Discrete messages
def decode_discrete(hexstr):
	# Convert hex message to binary
	hexstr = hexstr[2:]
	binstr = bin(int(hexstr,16))
	binstr = binstr[2:]

	# Converts binstr to list of ints (1's and 0's), then converts to Boolean values 
	# bin_list = list(map(bool,map(int,binstr)))

	# Converts binstr to list of ints (1's and 0's)
	bin_list = list(map(int,binstr))

	# Print for debugging
	print(bin_list)

	# Discrete: Air/Gnd 2 		= bit 1		VALUES: 1=In-Air, 	 0=On-Ground
	# Discrete: Air/Gnd 1 		= bit 2		VALUES: 1=In-Air, 	 0=On-Ground
	# Discrete: Alt Source Sel 	= bit 3		VALUES:	1=ADC 1, 	 0=ADC 2
	# Discrete: Standby/On 		= bit 4		VALUES:	1=On, 		 0=Standby
	# Variable: Air/Gnd 		= bit 5		VALUES:	1=On-Ground, 0=In-Air
	# Variable: PP Config Avail = bit 6		VALUES:	1=Avail, 	 0=Not Avail
	# Variable: ADS-B Fail 		= bit 7		VALUES:	1=Failed, 	 0=Not Fail
	# Variable: XPDR Fail 		= bit 8		VALUES:	1=Failed, 	 0=Not Fail
	# Discrete: Sel GPS 		= bit 9		VALUES:	1=GPS2, 	 0=GPS1

	return

# Decode ARINC-429 messages
def decode_ARINC(hexstr):
	# Temp Message
	print("ARINC Message Received")
	return

# Decode Extended Squitter messages
def decode_ES(hexstr):
	# Temp Message
	print("Extended Squitter Message Received")
	return

if __name__ == '__main__':
	# Start Stream
	read_stream()

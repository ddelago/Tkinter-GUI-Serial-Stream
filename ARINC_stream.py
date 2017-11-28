#!/usr/bin/env python
# Daniel Delago
# ddelago0596@gmail.com
# This file creates a stream of data representing aircraft in the ARINC 429 data format.
import serial
import time

ser = serial.Serial('/dev/pts/20')
ser.baudrate = 9600

def publish():
	# Open example ARINC dump file
	file = open('dataRecording.txt','r')

	for line in file:
		# Write to serial stream and terminal
		ser.write(line.encode())
		
		# print for debugging
		# print(line)

		# Time delay
		time.sleep(.05)

if __name__ == '__main__':
    publish()

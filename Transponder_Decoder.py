#!/usr/bin/env python
# Daniel Delago
# ddelago0596@gmail.com
# This file reads a stream of data representing aircraft in the ARINC 429 data format and decodes those messages.
import time
import datetime

# Decode serial stream
def decode_stream(serial_message, log_file):
    # Update Time
    sys_time = str(datetime.datetime.now().time())
    
    # Write time-stamped message to log file
    log_file.write(sys_time + ' ' + serial_message + '\n')

    message = ""

    # If a Discrete Message
    if(len(serial_message)==6):
        message = decode_discrete(serial_message)

    # If an ARINC Message
    elif(len(serial_message)==10):
        message = decode_ARINC(serial_message)

    # If an Extended Squitter Message
    elif(len(serial_message)==16):
        message = decode_ES(serial_message)

    return message

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

# Decode Discrete messages
def decode_discrete(hexstr):
    # Convert hex message to binary
    hexstr = hexstr[2:]
    binstr = bin(int(hexstr,16))
    binstr = binstr[2:]

    # Converts binstr to list of ints (1's and 0's)
    bin_list = list(map(int,binstr))

    # Print messages for debugging
    # print(bin_list)
    # print(hexstr)

    return [bin_list, hexstr]

# Decode ARINC-429 messages
def decode_ARINC(hexstr):
    # Temp Message
    # print("ARINC Message Received")
    return [[0], hexstr]

# Decode Extended Squitter messages
def decode_ES(hexstr):
    # Temp Message
    # print("Extended Squitter Message Received")
    return [[0], hexstr]
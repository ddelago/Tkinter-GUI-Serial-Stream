# ARINC-429-Decoder

## Setting up Virtual Serial Ports
- In a terminal enter the following command: 
- socat -d -d pty,raw,echo=0 pty,raw,echo=0
- This will create 2 virtual serial ports. 
- Whichever port you write to, can be read from the other port and vice versa.
- To test writing to port enter this in another terminal:
- echo "test string" > /dev/pts/#
- Now in another terminal enter:
- cat </dev/pts/#
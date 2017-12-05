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

# Title
- Repository for Nav Data Recorder software.  
- Current master version is v1.401.  
- You will need to create a Git Token to push/pull. See [here](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) to learn how to create and use one.

## Todo (in order of priority)
1. Add GPS/IRS select for MTS, NASDAT, and serial streams.  Use existing as default.
2. Rename data files to correct start date/time once NTP sync achieved.  This will avoid hunting for the right file if the nav data recorder time has been reset and no NTP sync when recording starts.
3. Use jumpers to indicate N926/N927/N928.  Need two pins to do this.  Will automatically switch MTS keys and other details without needing to change the software configuration.  
Requires interfacing with the secondary I/O card (analog w/ discretes).  
**NOTE:**  When no jumpers are installed, use NLABNA and NASALAB for tail number and callsign, respectively.
    
	| Box Location | J2 Pin 42 – DIO 0 | J2 Pin 41 – DIO 1 |
	|:---:|:---:|:---:|
	| LAB | OPEN | OPEN |
	| 926 |	OPEN | GROUND | 
	| 927 |	GROUND | OPEN |
	| 928 |	GROUND | GROUND |
	
4. Determine what else is required to achieve NASDAT/MTS equivalency.  Requires trip out to Ames and Armstrong.  
	**Armstrong:** Determine what the ER-2, Global Hawk, etc. do with their NASDAT besides the state data broadcast messages.  
	**Ames:** Determine how to streamline MTS integration and create payload-specific pages for MTS.  This feature could then be setup for payloads ahead of time if desired, or AOD test programs could use the feature as well.
5. Figure out how to record analog data.  Drivers are installed and can communicate with card, but haven't written any test programs to gather actual data.
6. Write cron job or other to remove files as they are more than ~60 days old so that the hard drive never fills up.

## Building Package
The [AB3000](https://www.astronics.com/ballard-technology/small-form-factor-systems/ab3000-series-avionics-i-o-computers) Nav Data Recorder runs on an embedded Linux operating system. The OS that was used to compile these packages was CentOS 6.4 32-bit.
```bash
# Navigate to source location
$ cd ~/wbnav_wc/Linux/src

# Delete old executable
$ make clean

# Compile, executable will be in release32/
$ make
```

## Running Testbed
1. Find testbed room at B990
2. Turn on Ballard, PC, and then PS1
3. Log in (Username and password will be under keyboard):  
	**User:** wb_tech **Pass:** qsse%%55%%55
4. Open CoPilot, press Play button to start
5. Open "NLAB ETH0 MAIN" and "NLAB ETH0 RT DISPLAY" for information on CoPilot and AB3000
6. Open Putty, SSH into **192.168.1.33**  
	**User:** root **Pass:** rootpass
7. cd into **/home/wb** to see output .DAT files. Filenames should be dates in the form of:  
	N(dayNumber)(hour)\_(min)(sec)\_(TAIL-NUMBER)\_v(1.401000).dat  
	Example: N19001_3102_LAB_v1.401000.dat  
8. Open Win-SCP. **192.168.1.33**  
	**User:** root **Pass:** rootpass
9. Transfer .DAT files from AB3000 to PC
10. Run "NAV DATA EXTRACT" program and choose a .DAT file, highlighted fields will display on load
11. wb3400 executable is located at **/home/omni**
12. Edit **/etc/rc3.d/S99rc-local** to change which wb3400 executable to run on startup (look at README)
13. Transfer executables from PC to **/home/omni** to test. Make file executable by:  
	chmod +x wb3400_new_executable
14. Run: "top" in terminal to view running executables. Stop executable by running: "kill [PID #]"
15. To run a new executable, Copy the example parameters from **/etc/rc3.d/S99rc-local**
15. Make sure CoPilot is running while you test!

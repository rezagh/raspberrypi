"""
This reads the serial port.
First make Arduino to write to serial port.
need to install serial library in a venv

source ./venv/bin/activate
./venv/bin/python3 lab4_task4.py

Find the port by lsusb or ls /dev/tty*

close Arduino IDE Serial Monitor if it is open otherwise it gives a port busy error.
    
"""

import serial
ser = serial.Serial('/dev/tty.usbmodem1101',9600)
while True:
    line = ser.readline()
    print(line)
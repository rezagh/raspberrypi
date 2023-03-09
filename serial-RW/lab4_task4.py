# get arduino to write to serial port.
# connect arduino to rpi
# read from serial port where arduino is connected. find the port by lsusb or ls /dev/tty*

import serial
ser = serial.Serial('/dev/ttyACM0',9600)
while True:
    line = ser.readline()
    print(line)
# https://pyserial.readthedocs.io/en/latest/pyserial.html
import serial
ser = serial.Serial('/dev/tty.usbmodem1101')  # open serial port
print(ser.name)         # check which port was really used
#ser.write(b'123')     # write a string
ser.close()  

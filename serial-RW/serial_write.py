import serial
ser = serial.Serial('/dev/ttyACM0')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'123')     # write a string
ser.close()  

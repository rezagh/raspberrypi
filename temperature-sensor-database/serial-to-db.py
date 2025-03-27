# install MariaDB or mysql and create user pi and the following db/table. 

# the read serial for incoming arduino temperature data

import serial
import MySQLdb
device = '/dev/tty'

arduino = serial.Serial(device, 9600)

data = arduno.readline()

print (data)

# here we are just connecting to the db. make sure not putting table name here.
dbConn = MySQLdb.connect("localhost","pi","","temperature_db") or die("couldn't connect to db")

print (dbConn)

with dbConn:
    cursor = dbConn.cursor()
    cursor.execute("insert into tempLog (Temperature) values (%s)" % (data))
    dbConn.commit()
    cursor.close()


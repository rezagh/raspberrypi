
import MySQLdb

dbConn = MySQLdb.connect("localhost","pi","password1","iot") or die("couldn't connect to db")

print (dbConn)
data = ('2024-08-09 12:34:56', 23.45);
with dbConn:
    cursor = dbConn.cursor()
    cursor.execute("insert into temperature_readings (timestamp, temperature) values (%s, %s)" , data)
    dbConn.commit()
    cursor.close()



Install MariaDB on Pi

```

sudo apt update
sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config
sudo apt install python3-pip
sudo apt install python-mysqldb # this is for python import MySQLdb
sudo apt install mariadb-server


# the following command will not work
mysql 

# you should run this to set a password for root

sudo mysql_secure_installation
    Enter current password for root (enter for none): <enter your os root password>
    Switch to unix_socket authentication [Y/n] y
	Change the root password? [Y/n] y
	Remove anonymous users? [Y/n] y
	Disallow root login remotely? [Y/n] y
	Remove test database and access to it? [Y/n] y
	Reload privilege tables now? [Y/n] y


mysql -u root -p
    
    show databases;
    create database iot;
    use iot;
    CREATE TABLE temperature_readings ( id INT AUTO_INCREMENT PRIMARY KEY, timestamp DATETIME NOT NULL, temperature DECIMAL(5,2) NOT NULL);

	show tables;
	select * from temperature_readings;
	INSERT INTO temperature_readings (timestamp, temperature) VALUES ('2024-08-09 12:34:56', 23.45);

	select * from temperature_readings;

	#create user pi
	CREATE USER 'pi'@localhost IDENTIFIED BY 'password1';
	GRANT ALL PRIVILEGES ON iot.* TO 'pi'@localhost;

	exit



```

Now install mysql client for python

`pip install mysqlclient`




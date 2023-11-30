sudo apt-get install mosquitto mosquitto-clients
sudo systemctl start mosquitto.service
sudo systemctl enable mosquitto.service


mosquitto_sub -t topic/example

mosquitto_pub -h <BROKER_IP_ADDRESS> -t <TOPIC> -m '<MESSAGE>'

mosquitto_pub -h 192.168.1.196 -t topic/example -m "xxx"



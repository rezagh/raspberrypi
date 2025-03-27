working with mqtt in command line step by step

first install on pi:
sudo apt install mosquitto mosquitto-clients
sudo systemctl start mosquitto.service
sudo systemctl enable mosquitto.service
sudo systemctl status mosquitto.service



test subscribe to a topic
`mosquitto_sub -t topic/example`


in another window, publish to that topic
`mosquitto_pub -h <BROKER_IP_ADDRESS> -t <TOPIC> -m '<MESSAGE>'`
example
`mosquitto_pub -h localhost -t topic/example -m "xxx"`


you should see an output on that subscriber window


now install client library for python
`pip install paho.mqtt`




![alt text](mqtt.png)


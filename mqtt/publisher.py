import paho.mqtt.publish as publish

publish.single("/edge_device/data", "msg",hostname="xx")



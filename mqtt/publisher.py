import paho.mqtt.publish as publish

publish.single("topic/example", "this is a msg",hostname="localhost")



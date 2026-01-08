import paho.mqtt.client as mqtt


# for when client receives a conn ack from server
def on_connect(client, userdata, flags, rc, props):
    print("connected with result code"  + str(rc))

    client.subscribe("topic/example")


def on_message(client, usserdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.67.2", 1883,60)

client.loop_forever()
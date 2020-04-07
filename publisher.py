# libraries
import paho.mqtt.client as mqtt

# create mqtt client object
client = mqtt.Client()

# connect client with broker
client.connect("localhost", 1883, 60)

# publish a message
client.publish("topic/string", "This is a testing message...")

# disconnect client
client.disconnect()

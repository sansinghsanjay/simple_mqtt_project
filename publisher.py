# libraries
import paho.mqtt.client as mqtt

# create mqtt client object
client = mqtt.Client()

# connect client with broker
client.connect("test.mosquitto.org", 1883, 60)
#client.connect("localhost", 1883, 60)

# publish a message
choice = ""
while(choice != "q"):
	message = str(raw_input("Enter message to publish: "))
	client.publish("topic/string", message)
	choice = str(raw_input("Enter 'q' to quit: "))
	print("")

# disconnect client
client.disconnect()

# libraries
import paho.mqtt.client as mqtt

# function to execute on-connection with broker
def on_connect(client, user_data, flags, return_code):
	# update on terminal about the connection
	print("Connection established with broker with return code : " + str(return_code))
	# subscribe for the topic string
	client.subscribe("topic/string")

# function to execute on recieving message from broker (actually sent by publisher)
def on_message(client, user_data, message):
	print("Message received: " + str(message.payload.decode()))

# create object of client
client = mqtt.Client()

# connect with broker
client.connect("test.mosquitto.org", 1883, 60)
#client.connect("localhost", 1883, 60)

# specify functions for on_connect and on_message
client.on_connect = on_connect
client.on_message = on_message

# loop this code forever
client.loop_forever()

import ubinascii
import machine
from umqtt.simple import MQTTClient

# Declare the MQTT server

mqtt_server = 'test.mosquitto.org'

# Create a unique ID to this device. In a larger environment
# this will come in handy

client_id = ubinascii.hexlify(machine.unique_id())


# MQTT connection function.  Need to add Docstring

def mqtt_client(topic, msg):

    client = MQTTClient(client_id, mqtt_server)
    client.connect()

    client.publish(topic, msg)
    client.disconnect()

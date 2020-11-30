import ubinascii
import machine
from umqtt.simple import MQTTClient


mqtt_server = 'test.mosquitto.org'
client_id = ubinascii.hexlify(machine.unique_id())


def mqtt_client(topic, msg):

    client = MQTTClient(client_id, mqtt_server)
    client.connect()

    client.publish(topic, msg)
    client.disconnect()

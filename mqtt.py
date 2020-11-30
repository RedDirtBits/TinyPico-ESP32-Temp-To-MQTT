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


# class MqttConnect:

#     mqtt_server = 'test.mosquitto.org'
#     client_id = ubinascii.hexlify(machine.unique_id())

#     def __init__(self, topic, msg, port=1883):

#         self.topic = topic
#         self.msg = msg
#         self.port = port

#     def client(self):

#         client = MQTTClient(self.client_id, self.mqtt_server, self.port)
#         client.connect()

#         client.publish(self.topic, self.msg)
#         client.disconnect()

import utime
import sensors
import machine

from boot import NetworkConnection
from mqtt import mqtt_client

# Theres a lot of opportunity in here for not only better code, but battery savings
# due to the sleep cycles.  As well, no where is there any Error handling.  That will
# have to be added, especially on the network connectivity side.

# Connect to WiFi
NetworkConnection().wifi_connect()

# The device seemed to be able to process faster than the connection
# being fully established and stable, so sleep for a few secs.

utime.sleep(3)

# Read from the sensor and store results

temp_c = sensors.read_dht11()[0]
temp_f = sensors.read_dht11()[1]
humidity = sensors.read_dht11()[2]

# Sleep again just to be sure the sensor read completes

utime.sleep(3)

# Take everything and form the MQTT message and publish to the topic

mqtt_client('RedDirt/ESP32',
            'Current Temperature C: {}\nCurrent Temperature F: {}\nHumidity: {}%'.format(temp_c, temp_f, humidity))

# Yeah, I know, sleep again.

utime.sleep(1)

# Disconnect from WiFi
NetworkConnection().wifi_disconnect()

# Start a simple sleep cycle to provide time to reset or upload/update
# code while in development

utime.sleep(10)

# The deepsleep time is in microseconds.  Therefore
# to calculate deepsleep time, multiple the time in seconds you want to wait for the
# next cycle by 1000.  For example, 15 minutes would be 900 seconds.  A 15 minute
# deepsleep would be 900 x 1000 or 90000.

machine.deepsleep(300000)

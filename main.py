# This is your main script.
import utime
import sensors
import machine

from boot import NetworkConnection
from mqtt import mqtt_client

# Connect to WiFi
NetworkConnection().wifi_connect()

utime.sleep(3)

temp_c = sensors.read_dht11()[0]
temp_f = sensors.read_dht11()[1]
humidity = sensors.read_dht11()[2]

utime.sleep(3)

# Get temperature from sensor and send results as message to Pushover

mqtt_client('RedDirt/ESP32',
            'Current Temperature C: {}\nCurrent Temperature F: {}\nHumidity: {}%'.format(temp_c, temp_f, humidity))

utime.sleep(1)

# Disconnect from WiFi
NetworkConnection().wifi_disconnect()

# Start a simple sleep cycle to provide time to reset or upload/update
# code while in development

utime.sleep(10)

# This deepsleep is for only 10s.  The deepsleep time is in microseconds.  Therefore
# to calculate deepsleep time, multiple the time in seconds you want to wait for the
# next cycle by 1000.  For example, 15 minutes would be 900 seconds.  A 15 minute
# deepsleep would be 900 x 1000 or 90000.

machine.deepsleep(300000)

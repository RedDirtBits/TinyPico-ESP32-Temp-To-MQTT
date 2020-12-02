import utime
import sensors
import machine
import ujson

from boot import NetworkConnection
from mqtt import mqtt_client

# Theres a lot of opportunity in here for not only better code, but battery savings
# due to the sleep cycles.  As well, no where is there any Error handling.  That will
# have to be added, especially on the network connectivity side.


# Connect to WiFi
NetworkConnection().wifi_connect()

# The device seemed to be able to process faster than the connection
# being fully established and stable, so sleep for a few secs.

utime.sleep(1)

sensor_data = {
    'DHT11': {
        'Current Temperature (C)': round(float(sensors.read_dht11()[0]), 2),
        'Current Temperature (F)': round(float(sensors.read_dht11()[1]), 2),
        'Current Humidity (%)': round(float(sensors.read_dht11()[2]), 2)
    },
    'BMP180': {
        'Current Temperature (F)': round(((sensors.read_bmp180()[0] * 1.8) + 32), 2),
        'Current Atmospheric Pressure (inHg)': round(sensors.read_bmp180()[1] * 0.00030, 2),
        'Current Altitude (Ft)': round(sensors.read_bmp180()[2] * 3.2808, 2)
    },
    'BH1750': {
        'Current Light Level (Lux)': round(sensors.read_bh1750(), 2)
    }
}

mqtt_client('RedDirt/ESP32', ujson.dumps(sensor_data))

# Yeah, I know, sleep again.

utime.sleep(1)

# Disconnect from WiFi
NetworkConnection().wifi_disconnect()

# Start a simple sleep cycle to provide time to reset or upload/update
# code while in development

utime.sleep(10)

# The deepsleep time is in microseconds.  Therefore, to calculate deepsleep time,
# multiple the time in seconds you want to wait for the next cycle by 1000.
# For example, 15 minutes would be 900 seconds.  A 15 minute deepsleep would
# be 900 x 1000 or 90000.

machine.deepsleep(300000)

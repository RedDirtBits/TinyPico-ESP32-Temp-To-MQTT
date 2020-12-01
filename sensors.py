import machine
import utime
import onewire
import ds18x20
import dht

from machine import I2C, Pin
from bmp180 import BMP180
from bh1750 import BH1750


def read_ds18b20():
    """
     Function to read externally connected DS18B20 Temperature sensor

    Returns:
        tuple: Temperature in Fahrenheit and Celcius
    """

    temp_sense = machine.Pin(12)
    wire = onewire.OneWire(temp_sense)
    sensor = ds18x20.DS18X20(wire)

    sensor_address = sensor.scan().pop()
    sensor.convert_temp()

    utime.sleep(1)

    temperature_c = sensor.read_temp(sensor_address)
    temperature_f = (temperature_c * 1.8) + 32

    return temperature_f, temperature_c


def read_dht11():
    """
     Function to read externally connected Temperature DHT11 sensor

    Returns:
        tuple: Temperature in Fahrenheit and Celcius, Humidity
    """

    dht11 = dht.DHT11(machine.Pin(4))
    dht11.measure()

    utime.sleep(1)

    temperature_c = dht11.temperature()
    temperature_f = temperature_c * (9/5) + 32.0
    humidity = dht11.humidity()

    return float(temperature_c), temperature_f, humidity


def read_bmp180():
    """
     Function to read externally connected BMP180 Temperature,
     Barometric Pressure and Altitude sensor

    Returns:
        tuple: Temperature in Celcius, Altitude in Meters and,
        Pressure in Pascals
    """

    bus = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
    bmp180 = BMP180(bus)
    bmp180.oversample_sett = 2
    bmp180.baseline = 101325

    temperature = bmp180.temperature
    pressure = bmp180.pressure
    altitude = bmp180.altitude

    return temperature, pressure, altitude


def read_bh1750():
    """
     Function to read externally connected BH1750 Light Sensor

    Returns:
        float: Light intensity in lumens
    """

    bus = I2C(scl=Pin(22), sda=Pin(21), freq=100000)

    s = BH1750(bus)

    return s.luminance(BH1750.ONCE_HIRES_1)

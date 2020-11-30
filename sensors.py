import machine
import utime
import onewire
import ds18x20
import dht


# DS18B20 Temperature Sensor
def read_ds18b20():
    """
     Function to read externally connected Temperature sensor

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

    dht11 = dht.DHT11(machine.Pin(4))
    dht11.measure()

    utime.sleep(1)

    temperature_c = dht11.temperature()
    temperature_f = temperature_c * (9/5) + 32.0
    humidity = dht11.humidity()

    return float(temperature_c), temperature_f, humidity

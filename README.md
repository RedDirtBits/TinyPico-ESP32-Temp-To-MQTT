# TinyPico Temperature To MQTT

A simple project set up for the purpose of testing power consumption of the TinyPico while reading room temperature and humidity sensors and publishing to MQTT

# Purpose

This is parallel project of my [ESP32 Temperature](https://github.com/RedDirtBits/ESP32-Temp-To-Pushover.git) project in which room temperature was read then sent via WiFi to the Android Pushover service.

The [TinyPico](https://www.tinypico.com/) differs from the garden variety [Espressif ESP32](https://www.espressif.com/en/products/modules/esp32) in that it uses the ESP32 D4 and is specifically built to minimize power consumption.

The idea here is the same as my other repo mentioned. Continue to develop Python coding skills (I really love working with MicroPython and Microcontrollers) and generally experiment with all that can be done with these tiny, power sipping, microcontrollers.

Initial checks for power consumption, and do keep in mind these are simple tests with a multimeter, show the following:

- Idle Current: 28mA
- WiFi Connect Current: ~110mA
- Deepsleep Current: 0.6mA

Based on the [DigiKey](https://www.digikey.ch/en/resources/conversion-calculators/conversion-calculator-battery-life) battery life calculator, assuming an overall average current consumption of 20mA, a 2300mAh battery should be able to power the TinyPico for approx. 115 hours. Of course, real world conditons such as temperature, battery quality, etc. all play into what might be observed in a working, production type setting.

# Next Steps

As time allows, I would like to do a few more things with each of the variant ESP32 devices I have:

1. Add more sensors such as light levels, barometric pressure, etc.
2. Make the overall codebase more compact and efficient
3. Flash the final working codebase into the ESP32 firmware itself

I believe there are more power savings to be had from writing the code more effiently and 'baking' it into the ESP32 firmware.

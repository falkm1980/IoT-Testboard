# ESP8266 Module on the board

## Installation Prerequisites
Before we can start using the ESP8266 Module we need to install some prerequisites.
check out: https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/flash-firmware

or alternatively:
http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#deploying-the-firmware

This python file is necessary to update the MicroPython firmare installed on the module.

latest firmware can be found here:
http://micropython.org/download

## Communication with the module
in order to be able to establish a connection between the ESP8266 module and the Raspberry we need a USB cable
to connect the 2 devices.

once connected you should see a new device on the Raspberry  "/dev/ttyUSB0". ttyUSB0 can also have another name.
ttyUSB0 is a vitual serial device

Install command "screen" on the Raspberry to open up a serial terminal
sudo apt-get install screen

ince installed you can use the following command:
screen /dev/ttyUSB0 115200

now you should have a terminal open that can "talk" to the ESP8266 module.
Type: 1+1 or print ("Hello world") and see what happens.
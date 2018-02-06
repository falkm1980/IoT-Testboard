#!/usr/bin/python

import time
from neopixel import *


# LED strip configuration:
LED_COUNT      = 6      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

def MakeStrip():
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	return strip

def Test(strip):
	val = 5
	colors = [Color(val,0,0), Color(0,val,0), Color(0,0,val), Color(val,val,0), Color(val,0,val), Color(0,val,val), Color(val,val,val)]
	for col in colors:
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, col)
		strip.show()
		time.sleep(0.5)

def LedOff(strip):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0,0,0))
	strip.show()

if __name__ == "__main__":

	strip = MakeStrip()
	try:

		while True:
			Test(strip)

	except KeyboardInterrupt:
		LedOff(strip)
		print ("bye-bye....")



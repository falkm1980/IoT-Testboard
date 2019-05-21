#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import ws2812bEvalBoard as ws2812
import displayEvalBoard as displayEvalBoard
import dhtSensorEvalBoard as DHT

import mcp3008 as ADC

 
ledOutput = [14,15,23,12,16,20,21,26]

btnInput = [5,6,13]

ledStrip = None

def Btn1_Click(channel):
	global ledStrip
	GPIO.output(ledOutput[0], GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(ledOutput[0], GPIO.LOW)
	for i in range(5):
		ws2812.Test(ledStrip)

	ws2812.LedOff(ledStrip)

def Btn2_Click(channel):
	GPIO.output(ledOutput[1], GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(ledOutput[1], GPIO.LOW)

def Btn3_Click(channel):
	GPIO.output(ledOutput[2], GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(ledOutput[2], GPIO.LOW)

def Setup():
	global ledStrip

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(ledOutput, GPIO.OUT)
	GPIO.setup(btnInput, GPIO.IN)

	GPIO.add_event_detect(btnInput[0], GPIO.RISING, callback=Btn1_Click)
	GPIO.add_event_detect(btnInput[1], GPIO.RISING, callback=Btn2_Click)
	GPIO.add_event_detect(btnInput[2], GPIO.RISING, callback=Btn3_Click)

	ledStrip = ws2812.MakeStrip()

def CleanUp():
	GPIO.cleanup()



def main():
	print ("Main...")

#	displayEvalBoard.Test()

	GPIO.output(ledOutput, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(ledOutput, GPIO.LOW)

	displayEvalBoard.Test()

if __name__ == "__main__":
	Setup()

	try:
		main()
	except KeyboardInterrupt:
		CleanUp()
		print ("bye-bye....")

#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import ws2812bEvalBoard as ws2812
import displayEvalBoard as displayEvalBoard
import dhtSensorEvalBoard as DHT

import mcp3008 as ADC
from threading import Thread


ledOutput = [14,15,23,12,16,20,21,26]

btnInput = [5,6,13]

ledStrip = None

gRunning = True

def threaded_functionRGB(arg):
	global gRunning
	while gRunning:
		ws2812.Test(ledStrip)

def threaded_functionLed(arg):
	global gRunning
	while gRunning:
		for x in ledOutput:
			GPIO.output(x, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(x, GPIO.LOW)
			


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


thread1 = None
thread2 = None

def main():
	global thread1
	global thread2
	print "Main..."

#	displayEvalBoard.Test()

#	GPIO.output(ledOutput, GPIO.HIGH)
#	time.sleep(2)
#	GPIO.output(ledOutput, GPIO.LOW)

	thread1 = Thread(target = threaded_functionRGB, args = (10, ))
	thread1.start()
	thread2 = Thread(target = threaded_functionLed, args = (10, ))
	thread2.start()


	displayEvalBoard.Test2()

if __name__ == "__main__":
	Setup()

	try:
		main()
	except KeyboardInterrupt:
		gRunning = False
		thread1.join()
		ws2812.LedOff(ledStrip)
		thread2.join()
		CleanUp()
		print "bye-bye...."

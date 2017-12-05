#!/usr/bin/python

import RPi.GPIO as GPIO
import time

TRIG = 27
ECHO = 22

def Setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	GPIO.output(TRIG, False)

	print "Waiting For Sensor To Settle"
	time.sleep(2)

def MeasureDistance():
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)	

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()
	
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()  

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	return round(distance, 2)

def Test():
	Setup()
	while True:
		dist = MeasureDistance()
		print "Distance:",dist,"cm"
		time.sleep(1)


if __name__ == "__main__":
	try:
		Test()
	except KeyboardInterrupt:
		GPIO.cleanup()
		print "bye-bye...."


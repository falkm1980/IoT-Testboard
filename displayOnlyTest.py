#!/usr/bin/python

from ili9341AdafruitWrapper import ili9341AdafruitWrapper as display
import displayCanvas
import time
import datetime, pytz
from PIL import Image, ImageDraw, ImageFont

import dhtSensorEvalBoard as DHT
import distanceEvalBoard as ultrasonicSensor
import mcp3008 as ADC

fontDigital = ImageFont.truetype('font/digital-7.ttf', 35)
font1 = ImageFont.truetype('font/atwriter.ttf', 30)
fontSanchez = ImageFont.truetype('font/Sanchezregular.otf', 20)

MARGIN_Y = 5

def GetDateTimeByTimezone(tz = "Europe/Vienna"):
    def GetDayOfWeek(i):
        if i == 0:
            return "Montag"
        elif i == 1:
            return "Dienstag"
        elif i == 2:
            return "Mittwoch"
        elif i == 3:
            return "Donnerstag"
        elif i == 4:
            return "Freitag"
        elif i == 5:
            return "Samstag"
        elif i == 6:
            return "Sonntag"
        else:
            return "unknown day"
            
    now =  datetime.datetime.now(pytz.timezone(tz))
    dateString = "{0}, {1}.{2}.{3}".format(GetDayOfWeek(now.weekday()), now.day, now.month, now.year)
    timeString = "{0:02}:{1:02}".format(now.hour, now.minute)
    return (dateString, timeString)

def Test():
	tft = display((320,240))
	canvas = displayCanvas.DisplayCanvas(tft)

#	ultrasonicSensor.Setup()
#	ADC.Open()

	logo = Image.open("logo.png");

	while True:
		with(canvas):
#			humidity, temperature = DHT.GetTempAndHumidity(11, 4)
			humidity=39
			temperature=20.2
			dateTime = GetDateTimeByTimezone()
#			dist = ultrasonicSensor.MeasureDistance()
			dist = 12.3
			sDistance = 'Distance: {0:0.1f} cm'.format(dist)
#			w = ADC.GetVoltageValue(0)
			w = 3.45
			sz = canvas.DrawTextCenter(10, "IoT-EvalBoard", font=font1, fill=(0,255,0))
			sz = canvas.DrawTextCenter(10+sz[1]+5, dateTime[1], font=fontDigital, fill=(0,255,0))
			sz = canvas.DrawLineCenter(sz[2] + MARGIN_Y, 200, fill=(255,0,0))
			s = 'Temp={0:0.1f}  Humidity={1:0.1f}%'.format(temperature, humidity)
			sz = canvas.DrawTextCenter(sz[2]+MARGIN_Y, s, font=fontSanchez, fill=(255,165,0))
			sz = canvas.DrawTextCenter(sz[2]+MARGIN_Y, sDistance, font=fontSanchez, fill=(255,165,0))

			sADC = 'CH0: {0:0.2f} V'.format(w)
			sz = canvas.DrawTextCenter(sz[2]+MARGIN_Y+5, sADC, font=fontSanchez, fill=(255,165,0))
			canvas.DrawBitmap((10,10), logo)
		time.sleep(1)
		break

def Test2():
	tft = display((320,240))
	canvas = displayCanvas.DisplayCanvas(tft)

#	ultrasonicSensor.Setup()
#	ADC.Open()

	logo = Image.open("logo.png");

	while True:
		with(canvas):
			dateTime = GetDateTimeByTimezone()
			humidity, temperature = DHT.GetTempAndHumidity(11, 4)
			canvas.DrawBitmap((10,10), logo)
			sz = canvas.DrawText(65, 15, "HTL Saalfelden", font=font1, fill=(0,255,255))
			sz = canvas.DrawTextCenter(20 + sz[2], "Tag der offenen Tuer", font=font1, fill=(0,255,0))
			sz = canvas.DrawTextCenter(10+sz[2]+5, dateTime[0], font=fontDigital, fill=(0,255,0))
			sz = canvas.DrawTextCenter(10+sz[2]+5, dateTime[1], font=fontDigital, fill=(0,255,0))
			s = 'Temp={0:0.1f}  Feuchtigkeit={1:0.1f}%'.format(temperature, humidity)
			sz = canvas.DrawTextCenter(sz[2]+MARGIN_Y, s, font=fontSanchez, fill=(255,165,0))
			canvas.DrawLineCenter(65, 300, fill=(255,0,0))
		time.sleep(1)
#		break

if __name__ == "__main__":
	Test()

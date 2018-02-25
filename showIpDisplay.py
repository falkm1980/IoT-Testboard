#!/usr/bin/python

import netifaces as ni
from ili9341AdafruitWrapper import ili9341AdafruitWrapper as display
import displayCanvas
import time
import datetime, pytz
from PIL import Image, ImageDraw, ImageFont

fontDigital = ImageFont.truetype('font/digital-7.ttf', 35)
font1 = ImageFont.truetype('font/atwriter.ttf', 30)
fontSanchez = ImageFont.truetype('font/Sanchezregular.otf', 20)


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

def GetIpAddress(ifName):
	try:
		ni.ifaddresses(ifName)
		ip = ni.ifaddresses(ifName)[2][0]['addr']
		return ip
	except:
		return "---"


def ShowIpInDisplay():
	tft = display((320,240))
	canvas = displayCanvas.DisplayCanvas(tft)

	ipWLAN = GetIpAddress("wlan0")
	ipETH = GetIpAddress("eth0")

	with(canvas):
		dateTime = GetDateTimeByTimezone()
		sz = canvas.DrawTextCenter(10+15, dateTime[0], font=fontDigital, fill=(0,255,0))
		sz = canvas.DrawTextCenter(10+sz[2]+5, dateTime[1], font=fontDigital, fill=(0,255,0))
		sz = canvas.DrawLineCenter(sz[2]+5, 300, fill=(255,0,0))

		canvas.DrawText(15, sz[2]+10, "WLAN0:", font=fontDigital, fill=(0,255,255))
		sz = canvas.DrawText(150, sz[2]+10, ipWLAN, font=fontDigital, fill=(0,255,255))
		canvas.DrawText(15, sz[2]+10, "ETH0:", font=fontDigital, fill=(0,255,255))
		sz = canvas.DrawText(150, sz[2]+10, ipETH, font=fontDigital, fill=(0,255,255))


if __name__ == "__main__":
	ShowIpInDisplay()


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:54:44 2016

@author: Markus
"""
from PIL import Image

import ILI9341 as TFT
#import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

# Raspberry Pi configuration.
DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0


class ili9341AdafruitWrapper():
    def __init__(self, (width, height)):
        self.disp = disp = TFT.ILI9341x(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))
        self.screenSize = (width, height)
        self.disp.begin()
        
    def display(self, image):
        image.save("./thumbnail.jpg")
        self.disp.display(image)


        
        

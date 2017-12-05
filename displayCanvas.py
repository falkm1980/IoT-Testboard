#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:38:14 2016

@author: Markus
"""
from PIL import Image, ImageDraw
      
    
class DisplayCanvas():
    def __init__(self, drawingDevice):
        self.drawingDevice = drawingDevice
        self.image = Image.new("RGB", self.drawingDevice.screenSize, (0,0,0))
#        self.image = Image.new("RGB", (320,240), (0,0,0))
        self.draw = None
        
    def __enter__(self):
        if self.image != None:
            self.image.close()
            
        self.image = Image.new("RGB", self.drawingDevice.screenSize, (0,0,0))
#        self.image = Image.new("RGB", (320,240), (0,0,0))
        self.draw = ImageDraw.Draw(self.image)
        return self.draw

    def getDisp(self):
        return self.drawingDevice
        
    def __exit__(self, type, value, traceback):
#        self.image = self.image.rotate(90)#.resize((240,320))
        self.drawingDevice.display(self.image)
        del self.draw 
    
    def DrawTextCenter(self, yPos, text, font=None, fill=(255,255,255)):
        size = self.draw.textsize(text, font=font)
        xPos = (self.drawingDevice.screenSize[0] - size[0]) / 2
        self.draw.text((xPos, yPos), text, font=font, fill=fill)
        return size + (yPos + size[1],)
        
    def DrawTextLeft(self, yPos, text, font=None, fill=(255,255,255), margin=10):
        size = self.draw.textsize(text, font=font)
        xPos = margin
        self.draw.text((xPos, yPos), text, font=font, fill=fill)
        return size + (yPos + size[1],)

    def DrawText(self, xPos, yPos, text, font=None, fill=(255,255,255)):
        size = self.draw.textsize(text, font=font)
        self.draw.text((xPos, yPos), text, font=font, fill=fill)
        return size + (yPos + size[1],)

    def DrawTextRight(self, yPos, text, font=None, fill=(255,255,255), margin=10):
        size = self.draw.textsize(text, font=font)
        xPos = self.drawingDevice.screenSize[0] - size[0] - margin
        self.draw.text((xPos, yPos), text, font=font, fill=fill)
        return size + (yPos + size[1],)

    def DrawLineCenter(self, yPos, length, fill=(255,255,255)):
        xPos = (self.drawingDevice.screenSize[0] - length) / 2
        self.draw.line((xPos,yPos, xPos+length,yPos), fill=fill)
        return (length, yPos, yPos+1)

    def DrawBitmap(self, xy, bmp):
        self.image.paste(bmp, box=xy);

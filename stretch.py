import os
import time
import urllib.request
import json
import ast
import datetime
import RPi.GPIO as GPIO
from datetime import date
from dateutil import parser
from lib.waveshare_epd import epd2in9_V2
from lib.functions import indent
from PIL import Image, ImageDraw, ImageFont

pic_dir = '/home/pi/eink-29/pics'

try:
    # Display init, clear
    display = epd2in9_V2.EPD()
    display.init()
    display.Clear(0) # 0: Black, 255: White

    w = display.height
    h = display.width
    #print('width:', w) 296
    #print('height:', h) 128

    runText = ImageFont.truetype(os.path.join(pic_dir,'Oswald.ttf'),54,index=0)
    goodText = ImageFont.truetype(os.path.join(pic_dir,'Oswald.ttf'),80,index=0)
    badText = ImageFont.truetype(os.path.join(pic_dir,'Oswald.ttf'),80,index=0)
    image = Image.new(mode='1', size=(w, h), color=255)
    draw = ImageDraw.Draw(image)
    
    firstLine = "Did you"
    secondLine = "stretch today?"

    draw.text((indent(firstLine,runText,w), -10), firstLine, font=runText, fill=0, align='center')
    draw.text((indent(secondLine,runText,w), 54), secondLine, font=runText, fill=0, align='center')
    display.display(display.getbuffer(image))

    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
    LED_PIN = 27
    GPIO.setup(LED_PIN, GPIO.OUT)

    timeout = 1800  #1800 = 30 minutes
    timeout_start = time.time()
    buttonPressed = False
 
    try:
        while time.time() < timeout_start + timeout:
            button_state = GPIO.input(23)
            GPIO.output(LED_PIN, GPIO.HIGH)
            if button_state == False:
                goodLine = "Good!"
                buttonPressed = True
                display.init()
                display.Clear(0) # 0: Black, 255: White
                image = Image.new(mode='1', size=(w,h),color=255)
                draw = ImageDraw.Draw(image)
                draw.text((indent(goodLine,goodText,w),-10),goodLine,font=goodText,fill=0, align='center')
                display.display(display.getbuffer(image))
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(20)
                exec(open("month-stats.py").read())
                break

        if buttonPressed == False:
            badLine = "Bad! :("
            display.init()
            display.Clear(0)
            image = Image.new(mode='1', size=(w,h),color=255)
            draw = ImageDraw.Draw(image)
            draw.text((indent(badLine,badText,w),-10),badLine,font=badText,fill=0,align='center')
            display.display(display.getbuffer(image))
            GPIO.output(LED_PIN,GPIO.LOW)
            time.sleep(20)
            exec(open("month-stats.py").read()) 
    except:
        GPIO.cleanup()

except IOError as e:
    print(e)

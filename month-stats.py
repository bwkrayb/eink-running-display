import os
import time
import urllib.request
import json
import ast
import datetime
from datetime import date
from dateutil import parser
from settings import SMASHRUN_TOKEN
from lib.waveshare_epd import epd2in9_V2
from lib.functions import indent
from lib.functions import indentThirds
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
    
    today = date.today()

    year = today.strftime("%Y")

    month = today.strftime("%m")

    byte_str = urllib.request.urlopen("https://api.smashrun.com/v1/my/stats/" + year + "/" + month + "?access_token=" + SMASHRUN_TOKEN).read()

    str_str = byte_str.decode('utf-8').strip("[]")

    json_str = json.loads(str_str)

    totalDist = str(round((json_str["totalDistance"] * 0.621), 2))
    #print(totalDist)

    runCount = str(json_str["runCount"])
    #print(runCount)

    longRun = str(round((json_str["longestRun"] * 0.621), 2))
    #print(longRun)

    avgLen = str(round((json_str["averageRunLength"] * 0.621), 2))
    #print(avgLen) 


    dateText = ImageFont.truetype(os.path.join(pic_dir,'BebasNeue-Regular.ttf'), 30, index=0)
    runText = ImageFont.truetype(os.path.join(pic_dir,'Oswald.ttf'),45,index=0)
    labelText = ImageFont.truetype(os.path.join(pic_dir,'Oswald.ttf'),20,index=0)
    image = Image.new(mode='1', size=(w, h), color=255)
    draw = ImageDraw.Draw(image)

    datePrint = "Stats: " + today.strftime("%B") + " " + year

    draw.text((indent(datePrint,dateText,w), 0), datePrint, font=dateText, fill=0, align='left')
    draw.text((indent(totalDist + "mi",runText,w/2), 20), totalDist + "mi", font=runText, fill=0, align='center')
    draw.text((indent(runCount + "runs",runText,w/2), 70), runCount + "runs", font=runText, fill=0, align='center')
    draw.text((indentThirds(longRun + "mi",runText,w) - 15, 20), longRun + "mi", font=runText, fill=0, align='center')
    draw.text((indentThirds(avgLen + "mi",runText,w) - 15, 70), avgLen + "mi", font=runText, fill=0, align='center')

    draw.text((270,95), "avg", font=labelText, fill=0, align='left') 
    draw.text((270,45), "top", font=labelText, fill=0, align='left') 
    #draw.text((0,0), datePrint, font=dateText, fill=0, align='left') 
    #draw.text((0,0), datePrint, font=dateText, fill=0, align='left') 

    display.display(display.getbuffer(image))

except IOError as e:
    print(e)

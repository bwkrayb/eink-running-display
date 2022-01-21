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

    byte_str = urllib.request.urlopen("https://api.smashrun.com/v1/my/activities/search?count=1&access_token=" + SMASHRUN_TOKEN).read()

    str_str = byte_str.decode('utf-8').strip("[]")

    json_str = json.loads(str_str)

    time = parser.parse(json_str["startDateTimeLocal"])

    timeStr = time.strftime("%x")

    today = date.today()

    todayStr = today.strftime("%x")

    yesterday = (today - datetime.timedelta(days=1)).strftime("%x")

    if timeStr == todayStr:
        runDate = "Today"
    elif timeStr == yesterday:
        runDate = "Yesterday"
    else:
        runDate = timeStr
    
    distanceInt = round((json_str["distance"] * 0.621), 2)
    distance = str(distanceInt)
    duration = json_str["duration"]
    timeMin = str(int(duration / 60))
    timeSec = str(int(duration % 60)).zfill(2)
    calories = str(json_str["calories"])
    paceMin = str(int((duration / distanceInt) / 60)) 
    paceSec = str(int((duration / distanceInt) % 60)).zfill(2)
 
    dateText = ImageFont.truetype(os.path.join(pic_dir,'BebasNeue-Regular.ttf'), 30, index=0)
    runText = ImageFont.truetype(os.path.join(pic_dir,'Oswald.ttf'),45,index=0)
    
    image = Image.new(mode='1', size=(w, h), color=255)
    draw = ImageDraw.Draw(image)
    
    datePrint = "Last Run: " + runDate

    draw.text((indent(datePrint,dateText,w), 0), datePrint, font=dateText, fill=0, align='left')
    #draw.text((0,0), datePrint, font=dateText, fill=0, align='left')   

    draw.text((indent(distance + " mi",runText,w/2), 20), distance + " mi", font=runText, fill=0, align='center')
    draw.text((indent(timeMin + ":" + timeSec,runText,w/2), 70),timeMin + ":" + timeSec, font=runText, fill=0, align='center')
    draw.text((indentThirds(paceMin + ":" + paceSec + "/mi",runText,w), 20),paceMin + ":" + paceSec + "/mi", font=runText, fill=0, align='center')
    draw.text((indentThirds(calories + " cals",runText,w), 70), calories + " cals", font=runText, fill=0, align='center')
    display.display(display.getbuffer(image))


except IOError as e:
    print(e)

import os
import time
import urllib.request
import json
import ast
from settings import SMASHRUN_TOKEN
from lib.waveshare_epd import epd2in9_V2

from PIL import Image, ImageDraw, ImageFont

pic_dir = '/home/pi/eink-29/pics'

try:
    # Display init, clear
    display = epd2in9_V2.EPD()
    display.init()
    display.Clear(0) # 0: Black, 255: White

    w = display.height
    h = display.width
    #print('width:', w)
    #print('height:', h)

    byte_str = urllib.request.urlopen("https://api.smashrun.com/v1/my/activities/search?count=1&access_token=" + SMASHRUN_TOKEN).read()

    str_str = byte_str.decode('utf-8').strip("[]")

    json_str = json.loads(str_str)
    
    distanceInt = round((json_str["distance"] * 0.621), 2)
    distance = str(distanceInt)
    duration = json_str["duration"]
    timeMin = str(int(duration / 60))
    timeSec = str(int(duration % 60))
    calories = str(json_str["calories"])
    paceMin = str(int((duration / distanceInt) / 60)) 
    paceSec = str(int((duration / distanceInt) % 60))
 
    body = ImageFont.truetype(os.path.join(pic_dir,'BebasNeue-Regular.ttf'), 20, index=0)
    other = ImageFont.truetype(os.path.join(pic_dir,'Anton-Regular.ttf'),25,index=0)
    
    image = Image.new(mode='1', size=(w, h), color=255)
    draw = ImageDraw.Draw(image)

    #draw.text((0, 0), weatherTempShort, font=body, fill=0, align='left')
    draw.text((0, 0), "Last Run:", font=body, fill=0, align='left')
    
    draw.text((0, 18), "Distance: " + distance + " miles", font=other, fill=0, align='center')
    draw.text((0, 44), "Time: " + timeMin + ":" + timeSec, font=other, fill=0, align='center')
    draw.text((0, 70), "Pace: " + paceMin + ":" + paceSec + "/mi", font=other, fill=0, align='center')
    draw.text((0, 97), "Calories: " + calories, font=other, fill=0, align='center')
    display.display(display.getbuffer(image))


except IOError as e:
    print(e)

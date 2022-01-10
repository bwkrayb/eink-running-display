import datetime
import os
import PIL
import time
import logging
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

logging.basicConfig(level=logging.INFO,filename='/home/pi/eink-29/logs/eink.log')


def paste(image: Image, position: tuple = (0, 0)) -> None:
    """
    Paste an image onto the buffer
    :param image: Image to paste
    :param position: tuple position to paste at
    :return: None
    """
    image.paste(image, position)


def indent(input,font,width):
    return int((width - font.getsize(input)[0]) / 2)

def indentThirds(input,font,width):
    return int(((width*1.5) - font.getsize(input)[0]) / 2)

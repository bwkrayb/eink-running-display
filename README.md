You can use this display to show information about your most recent run to use as motivation or bragging rights or anything you want really. 

This is a small project that I started to just experiment with another eink display connected to a raspberry pi. This only supports the 2.9 inch waveshare eink screen as far as I know. The file last-run.py will display the information for your most recent run. 


Prerequisites:
enable SPI interface in raspi-config
python3-pip
python3-pil
python3-numpy
RPi.GPIO
spidev
waveshare drivers installed from https://github.com/waveshare/e-Paper


The plan is to add more displays, possibly add a weather component for forecast information. I also want to find a way to schedule future runs or exercise or similar things. Need to create a crontab to have it update automatically



Screen information
width: 296
height: 128

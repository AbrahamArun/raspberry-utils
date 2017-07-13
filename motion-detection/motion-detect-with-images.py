from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import yaml
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

camera = PiCamera()
pir = MotionSensor(4)
while True:
    pir.wait_for_motion()

    saveDir = datetime.now().strftime("%Y-%m-%d")
    filename = datetime.now().strftime(cfg["image-path"] + saveDir + "/" + "%H.%M.%S.png")
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    camera.capture(filename)
    pir.wait_for_no_motion()

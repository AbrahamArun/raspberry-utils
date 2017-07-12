from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

camera = PiCamera()
pir = MotionSensor(4)
while True:
    pir.wait_for_motion()
    filename = datetime.now().strftime(cfg["image-path"] + "%Y-%m-%d_%H.%M.%S.png")
    camera.capture(filename)
    pir.wait_for_no_motion()

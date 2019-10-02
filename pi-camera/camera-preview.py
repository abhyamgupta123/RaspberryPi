from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)   #put the delay time in seconds in sleep brackets. 

camera.stop_preview()

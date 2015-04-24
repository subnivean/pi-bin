"""From p121 of "Getting Started with Raspberry Pi"
"""
from SimpleCV import Camera
#from time import sleep
import time

myCamera = Camera(prop_set={'width': 1280, 'height': 720})
frame = myCamera.getImage()
frame.save('test.jpg')

myCamera.stop()

#while not myDisplay.isDone():
#  myCamera.getImage().save(myDisplay)
#  sleep(0.1)

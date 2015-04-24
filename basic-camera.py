"""From p121 of "Getting Started with Raspberry Pi"
"""
from SimpleCV import Camera, Display
from time import sleep

myCamera = Camera(prop_set={'width': 320, 'height': 240})

myDisplay = Display(resolution=(320, 240))

while not myDisplay.isDone():
  myCamera.getImage().save(myDisplay)
  sleep(0.1)

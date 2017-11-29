#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

ObstaclePin = 10

def setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def loop():
  while True:
    if (1 == GPIO.input(ObstaclePin)):
      print "DETECTED: Obstacle"
      time.sleep(0.2)

def destroy():
  print "cleanup"
  GPIO.cleanup()


if __name__ == '__main__':
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()





import time
import RPi.GPIO as GPIO
from gpiozero import Motor

L1 = 19
L2 = 26
R1 = 6
R2 = 13

def init():
    left_motor = Motor(L1, L2)
    right_motor = Motor(R1, R2)

def stop():
    left_motor.stop()
    right_motor.stop()

def cleanup():
  GPIO.cleanup()

def front_back(front):
    print "moving front {}\n".format(front)
    if front:
        left_motor.forward()
        right_motor.forward()
    else:
        left_motor.backward()
        right_motor.backward()

def loop():
  ip = ' '
  while ip != 'a':
    print 'enter '
    ip = raw_input()
    if ip == 'q':
      front_back(True)
      time.sleep(2)
    elif ip == 'z':
      front_back(False)
      time.sleep(2)
  stop()


def main():
    init()
    try:
      loop()
      cleanup()
    except: 
      print "exception handled"
      #print e.message
      cleanup()

if __name__ == '__main__':
  main()

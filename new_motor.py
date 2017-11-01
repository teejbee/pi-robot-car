import sys
import time
import traceback
from gpiozero import Motor

L1 = 19
L2 = 26
R1 = 6
R2 = 13


left_motor = None
right_motor = None

def init():
    global left_motor
    global right_motor
    left_motor = Motor(L1, L2)
    right_motor = Motor(R1, R2)

def stop():
    global left_motor
    global right_motor
    left_motor.stop()
    right_motor.stop()

def cleanup():
    print "cleanup code"

def front_back(front):
    global left_motor
    global right_motor
    print "moving front {}\n".format(front)
    if front:
        left_motor.forward()
        right_motor.forward()
    else:
        left_motor.backward(speed=0.2)
        right_motor.backward(speed=0.2)

def loop():
  ip = ' '
  while ip != 'a':
    stop()
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
    except NameError as e:
      print "NameError"
      print e
      traceback.print_exc()
    except: 
      print "exception handled"
      print "Unexpected error:" + str(sys.exc_info()[0])
      cleanup()

if __name__ == '__main__':
  main()

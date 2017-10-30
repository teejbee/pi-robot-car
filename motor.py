import time 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

L1 = 19
L2 = 26
R1 = 6
R2 = 13

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)

def front_back(front):
    print "moving front {}\n".format(front)
    GPIO.output(L1, front)
    GPIO.output(L2, not front)
    GPIO.output(R1, front)
    GPIO.output(R2, not front)


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


GPIO.cleanup()


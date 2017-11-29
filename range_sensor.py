import sys
import RPi.GPIO as GPIO
import time

TRIG = 23 
ECHO = 24

class Ultrasound:
    def __init__(self, delay=1):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        self.delay = delay
        self.settle()

    def settle(self):
        GPIO.output(TRIG, False)
        print "Waiting For Sensor To Settle"
        time.sleep(self.delay)

    def get_distance(self, settle=False):
        if settle:
            self.settle()

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        print "Distance:",distance,"cm"

        return distance

    def cleanup(self):
        GPIO.cleanup()




if __name__=='__main__':
    us = Ultrasound()
    print us.get_distance()
    us.cleanup()


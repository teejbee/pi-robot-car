#!/usr/bin/env python
import socket
import time 
import RPi.GPIO as GPIO
import range_sensor as us_sensor


L1 = 19
L2 = 26
R1 = 6
R2 = 13
sensor = us_sensor.Ultrasound()
s = socket.socket()


def init():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(L1, GPIO.OUT)
  GPIO.setup(L2, GPIO.OUT)
  GPIO.setup(R1, GPIO.OUT)
  GPIO.setup(R2, GPIO.OUT)
  sensor.settle()


def honk():
    print "honk! \n"

def halt():
    print "halt \n"
    GPIO.output(L2, False)
    GPIO.output(L1, False)
    GPIO.output(R2, False)
    GPIO.output(R1, False)


def move_back():
    print "moving back \n"
    GPIO.output(L2, True)
    GPIO.output(L1, False)
    GPIO.output(R2, True)
    GPIO.output(R1, False)


def move_front():
    print "moving front \n"
    GPIO.output(L1, True)
    GPIO.output(L2, False)
    GPIO.output(R1, True)
    GPIO.output(R2, False)


def cleanup():
  print "cleaning up GPIO"
  GPIO.cleanup()


def start_server():
    a,p = s.getsockname()
    if p != 0:
        print "server already running"
        return
    print "starting server"
    s.bind(('', 43423))
    s.listen(1)
    s.settimeout(0.2)


def get_input():
    try:
        sc,t = s.accept()
        data = sc.read(100)
        data = data[0]
        return data
    except:
        return ' '

def engine_on():
    print "engine turned on"
    move_front()

def engine_off():
    print "engine turned off"
    halt()

def start_left_turn():
    print "turning left"

def start_right_turn():
    print "turning right"

def net_loop():
    start_server()
    ip = ' '
    while ip != 'a':
        ip = get_input()
        if ip == 'A':
            engine_on()
        elif ip == 'B':
            start_left_turn()
        elif ip == 'b':
            stop_left_turn()
        elif ip == 'C':
            start_right_turn()
        elif ip == 'c':
            stop_right_turn()

    engine_off()

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

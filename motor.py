#!/usr/bin/env python
import socket
import time 
import RPi.GPIO as GPIO
import range_sensor as us_sensor


L1 = 19
L2 = 26
R1 = 6
R2 = 13
THRESHOLD = 30

sensor = us_sensor.Ultrasound()
s = socket.socket()
sc = None


def init():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(L1, GPIO.OUT)
  GPIO.setup(L2, GPIO.OUT)
  GPIO.setup(R1, GPIO.OUT)
  GPIO.setup(R2, GPIO.OUT)
  sensor.settle()


def honk():
    print "honk! honk!!\n"

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
        data = ''
        if sc:
            data = sc.recv(100)
        if data == '':
            sc,t = s.accept()
            data = sc.recv(100)
        data = data[0]
        return data
    except:
        return ' '

def engine_on():
    print "engine turned on"
    honk()
    time.sleep(1)
    move_front()

def engine_off():
    print "engine turned off"
    halt()

def left_turn(dur=0.5):
    print "turning left"
    time.sleep(dur)
    halt()

def right_turn(dur=0.5):
    print "turning right"
    time.sleep(dur)
    halt()

def drive_safe():
    obs = sensor.get_distance(settle=True)
    if obs < THRESHOLD:
        honk()
        halt()
        time.sleep(1.0)
        move_back(dur=1.0)
        turn_right(dur=1.0)
    else:
        move_front()


def net_loop():
    start_server()
    run = True
    while run:
        ip = get_input()
        if ip == 'A':
            engine_on()
        elif ip == 'a':
            run = False
        elif ip.lower() == 'b':
            left_turn()
        elif ip.lower() == 'c':
            right_turn()

        drive_safe()

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

import sys
import time
import traceback
from gpiozero import Motor
from flask import Flask
from flask import Response
from flask import request

app = Flask(__name__)

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
        left_motor.forward(speed=0.3)
        right_motor.forward(speed=0.3)
    else:
        left_motor.backward(speed=0.3)
        right_motor.backward(speed=0.3)

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

@app.route('/robot/hello')
def helloworld():
    resp = Response("robot is up", status = 200)
    return resp

#curl -i http://127.0.0.1:5678/robot/move?dir=f
@app.route('/robot/move', methods=['GET'])
def move():
  if 'dir' not in request.args:
    resp = Response('dir not provided')
    return resp
  dir = request.args['dir']
  if dir == 'f':
    front_back(True)
    time.sleep(1)
    stop()
  elif dir == 'r':
    front_back(False)
    time.sleep(1)
    stop()
  return Response('moved')
    
def rest_main():
  try:
    init()
    stop()
    app.run(debug=True, host='0.0.0.0', port=5678)
  except:
    print "exception in rest_main"
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
  rest_main()

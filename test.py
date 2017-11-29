import range_sensor.py

us = Ultrasound()

print us.get_distance()
us.cleanup()

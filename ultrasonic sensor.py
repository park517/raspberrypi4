import RPi.GPIO as gpio
import time

LED = 12
trig = 5
echo = 6
print("start")
gpio.setmode(gpio.BCM)
gpio.setup(trig, gpio.OUT)
gpio.setup(LED, gpio.OUT)
gpio.setup(echo, gpio.IN)
pulse_start = time.time()

try :
    while True :
      gpio.output(trig, False)
      time.sleep(0.1) 
      gpio.output(trig, True)
      time.sleep(0.00002)
      gpio.output(trig, False)
      
      while gpio.input(echo) == 0 :
        pulse_start = time.time()
        
      while gpio.input(echo) == 1 :
        pulse_end = time.time()
        
      pulse_duration = pulse_end - pulse_start
      distance_1 = pulse_duration * 17000
      distance_2 = round(distance_1, 2)
      try:
        if distance_2 <=10:
            gpio.output(LED, gpio.HIGH)
        else:
            gpio.output(LED, gpio.LOW)
      except KeyboardInterrupt:
          print("error")
      print("Distance : ", distance_2, "cm")
except:
    gpio.cleanup()
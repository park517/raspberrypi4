import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
for loop in range(0,3):
        print (loop)
        
        GPIO.output(26, True)
        time.sleep(1)
        GPIO.output(26, False) 
        time.sleep(1)
GPIO.cleanup()
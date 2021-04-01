import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO ports for the 7seg pins
segments = (2,3,4,5,6,7,8,9)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment,0)
    
num = {
    '0':(1,1,1,1,1,1,0,0),
    '1':(0,1,1,0,0,0,0,0),
    '2':(1,1,0,1,1,0,1,0),
    '3':(1,1,1,1,0,0,1,0),
    '4':(0,1,1,0,0,1,1,0),
    '5':(1,0,1,1,0,1,1,0),
    '6':(1,0,1,1,1,1,1,0),
    '7':(1,1,1,0,0,1,0,0),
    '8':(1,1,1,1,1,1,1,0),
    '9':(1,1,1,1,0,1,1,0),
    '10':(1,1,1,0,1,1,1,0), #A
    '11':(0,0,1,1,1,1,1,0), #B
    '12':(1,0,0,1,1,1,0,0), #C
    '13':(0,1,1,1,1,0,1,0), #D
    '14':(1,0,0,1,1,1,1,0), #E
    '15':(1,0,0,0,1,1,1,0), #F
    '16':(1,1,1,1,1,1,1,1) #ALL
    }
while True:
    
    for index in range(0,10):
        s=str(index)
        for loop in range(0,8):
            GPIO.output(segments[loop],num[s][loop])
        time.sleep(1)
        
GPIO.cleanup()
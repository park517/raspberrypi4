

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)




# GPIO ports for the 7seg pins

segments =  (2,3,4,5,6,7,8,9)




for segment in segments:

    GPIO.setup(segment, GPIO.OUT)

    GPIO.output(segment, 0)




num = {                           

    '0':(0,0,0,0,0,0,1,1),

    '1':(1,0,0,1,1,1,1,1),

    '2':(0,0,1,0,0,1,0,1),

    '3':(0,0,0,0,1,1,0,1),

    '4':(1,0,0,1,1,0,0,1),

    '5':(0,1,0,0,1,0,0,1),

    '6':(0,1,0,0,0,0,0,1),

    '7':(0,0,0,1,1,0,1,1),

    '8':(0,0,0,0,0,0,0,1),

    '9':(0,0,0,0,1,0,0,1),

    '10':(0,0,0,1,0,0,0,1), #A

    '11':(1,1,0,0,0,0,0,1), #B

    '12':(0,1,1,0,0,0,1,1), #C

    '13':(1,0,0,0,0,1,0,1), #d

    '14':(0,1,1,0,0,0,0,1), #E

    '15':(0,1,1,1,0,0,0,1), #F

    '16':(0,0,0,0,0,0,0,0)  #X

       }

    

for index in range(0,17):

    s=str(index)

    for loop in range(0,8):

        print (loop)

        GPIO.output(segments[loop],num[s][loop] )

    time.sleep(1)    

GPIO.cleanup()

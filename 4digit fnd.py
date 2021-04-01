import RPi.GPIO as GPIO
import time, datetime
now = datetime.datetime.now()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO ports for the 7seg pins
Digit_1 = 18
Digit_2 = 25
Digit_3 = 8
Digit_4 = 26
segment_a = 23
segment_b = 20
segment_c = 13
segment_d = 27
segment_e = 17
segment_f = 24
segment_g = 19
segment_dp = 22

segment8 = (23,20,13,27,17,24,19,22)

for segment in segment8:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment,0)
    
digits = (18,25,8,26)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit,0) #off

null = [0,0,0,0,0,0,0,0]
zero = [0,0,0,0,0,0,1,1]
one = [1,0,0,1,1,1,1,1]
two = [0,0,1,0,0,1,0,1]
three = [0,0,0,0,1,1,0,1]
four = [1,0,0,1,1,0,0,1]
five = [0,1,0,0,1,0,0,1]
six = [0,1,0,0,0,0,0,1]
seven = [0,0,0,1,1,1,1,1]
eight = [0,0,0,0,0,0,0,1]
nine = [0,0,0,0,1,0,0,1]

def print_segment(charector):
    if charector == 1:
        for i in range(8):
            GPIO.output(segment8[i], one[i])
    if charector == 2:
         for i in range(8):
             GPIO.output(segment8[i], two[i])

    if charector == 3:
         for i in range(8):
             GPIO.output(segment8[i], three[i])

    if charector == 4:
         for i in range(8):
             GPIO.output(segment8[i], four[i])

    if charector == 5:
         for i in range(8):
             GPIO.output(segment8[i], five[i])

    if charector == 6:
         for i in range(8):
             GPIO.output(segment8[i], six[i])

    if charector == 7:
         for i in range(8):
             GPIO.output(segment8[i], seven[i])

    if charector == 8:
         for i in range(8):
             GPIO.output(segment8[i], eight[i])

    if charector == 9:
         for i in range(8):
             GPIO.output(segment8[i], nine[i])

    if charector == 0:
         for i in range(8):
             GPIO.output(segment8[i], zero[i])        
             

while 1:

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    h1 = int(hour/10)
    h2 = int(hour % 10)
    m1 = int(minute /10)
    m2 = int(minute % 10)
    print (h1,h2,m1,m2)  
 
    delay_time = 0.001 #delay to create virtual effect
     
     
    GPIO.output(18, 1) #Turn on Digit One
    print_segment (h1) #Print h1 on segment
    time.sleep(delay_time)
    GPIO.output(18, 0) #Turn off Digit One

    GPIO.output(25, 1) #Turn on Digit One
    print_segment (h2) #Print h1 on segment
    time.sleep(delay_time)
    GPIO.output(25, 0) #Turn off Digit One
    
    GPIO.output(8, 1) #Turn on Digit One
    print_segment (m1) #Print h1 on segment
    time.sleep(delay_time)
    GPIO.output(8, 0) #Turn off Digit One
    
    GPIO.output(26, 1) #Turn on Digit One
    print_segment (m2) #Print h1 on segment
    time.sleep(delay_time)
    GPIO.output(26, 0) #Turn off Digit One
  8
    #time.sleep(1)
    
GPIO.cleanup()
import RPi.GPIO as gpio
import time

touchpin = 21
ledpin = 26
gpio.setmode(gpio.BCM)
gpio.setup(touchpin,gpio.IN)
gpio.setup(ledpin,gpio.OUT)
led = gpio.PWM(ledpin,50)
led.start(0)

try:
    n = 0
    
    while True:
        input_value = gpio.input(touchpin)
        if input_value == True:
            n+=5
            if n>100:
                n=100
        else:
            n-=5
            if n<0:
                n=0
        led.ChangeDutyCycle(n)
        time.sleep(0.1)
        
except KeyboardInterrupt:
        gpio.cleanup()
                
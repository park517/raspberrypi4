import RPi.GPIO as GPIO
import time
FLAME = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME, GPIO.IN)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

try:
    while True:
        if GPIO.input(FLAME) == 1 : # 평소 1을 전송함
            print("안전")
            GPIO.output(19, True)
            GPIO.output(20, False)
        else :                      # 불꽃 감지시 0을 전송함
            print("화재 경보")
            GPIO.output(20, True)
            GPIO.output(19, False)
            
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
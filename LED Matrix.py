import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

row_1 = 21
row_2 = 8
row_3 = 26
row_4 = 12
row_5 = 10
row_6 = 19
row_7 = 9
row_8 = 6
col_1 = 7
col_2 = 11
col_3 = 5
col_4 = 20
col_5 = 13
col_6 = 16
col_7 = 25
col_8 = 24

rows = (row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8)
cols = (col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8)

Heart_col_0=(1,1,1,1,1,1,1,1)
Heart_col_1=(1,0,0,1,1,0,0,1)
Heart_col_2=(0,0,0,0,0,0,0,0)
Heart_col_3=(0,0,0,0,0,0,0,0)
Heart_col_4=(1,0,0,0,0,0,0,1)
Heart_col_5=(1,1,0,0,0,0,1,1)
Heart_col_6=(1,1,1,0,0,1,1,1)
Heart_col_7=(1,1,1,1,1,1,1,1)

square_col_0=(1,1,1,1,1,1,1,1)
square_col_1=(1,0,0,0,0,0,0,1)
square_col_2=(1,0,1,1,1,1,0,1)
square_col_3=(1,0,1,1,1,1,0,1)
square_col_4=(1,0,1,1,1,1,0,1)
square_col_5=(1,0,1,1,1,1,0,1)
square_col_6=(1,0,0,0,0,0,0,1)
square_col_7=(1,1,1,1,1,1,1,1)

triangle_col_0=(1,1,1,1,1,1,1,1)
triangle_col_1=(1,1,1,0,0,1,1,1)
triangle_col_2=(1,1,0,0,0,0,1,1)
triangle_col_3=(1,0,0,0,0,0,0,1)
triangle_col_4=(0,0,0,0,0,0,0,0)
triangle_col_5=(1,1,1,1,1,1,1,1)
triangle_col_6=(1,1,1,1,1,1,1,1)
triangle_col_7=(1,1,1,1,1,1,1,1)


for row in rows:
    GPIO.setup(row, GPIO.OUT)
    GPIO.output(row,0)
for col in cols:
    GPIO.setup(col, GPIO.OUT)
    GPIO.output(col,0)
    
def allOff():
    for row in rows:
        GPIO.output(row, 0)
    for col in cols:
        GPIO.output(col, 1)
        
def allOn():
    for row in rows:
        GPIO.output(row, 1)
    for col in cols:
        GPIO.output(col, 0)

while True:

    for x in range(8):
        allOff()
        GPIO.output(rows[x], 1)
        
        if (x==0):
            for y in range(8):
                GPIO.output(cols[y], triangle_col_0[y])
        elif (x==1):
            for y in range(8):
                GPIO.output(cols[y], triangle_col_1[y])
        elif (x==2):
            for y in range(8):
                GPIO.output(cols[y], triangle_col_2[y])
        elif (x==3):
            for y in range(8):
                GPIO.output(cols[y], triangle_col_3[y])
        elif (x==4):
            for y in range(8):
                GPIO.output(cols[y], triangle_col_4[y])
        elif (x==5):
            for y in range(8):
                GPIO.output(cols[y], triangle_col_5[y])
        elif (x==6):
            for y in range(8):
                GPIO.output(cols[y], triangle_col_6[y])
        elif (x==7):
            for y in range(8):
                GPIO.output(cols[y], triangle_col_7[y])

    
GPIO.cleanup()
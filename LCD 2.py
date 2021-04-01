import RPi_I2C_driver
import time

mylcd = RPi_I2C_driver.lcd()

while True:
    mylcd.lcd_display_string("Temp=25.0C", 1)
    mylcd.lcd_display_string("Humidity=64.0%",2)
# you're using the accelerometer
# with increasing tilt in the y-axis the blue LED turns on


import time
import board
import digitalio
from digitalio import DigitalInOut, Direction
import busio
import adafruit_lis3dh

i2c = busio.I2C(board.SCL, board.SDA)
int1 = digitalio.DigitalInOut(board.D5)  # D5 is connected to the interrupt pin on the accelerometer
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)


lis3dh.range = adafruit_lis3dh.RANGE_2_G #options are 2g,4g,8g,16g

blueLed = DigitalInOut(board.BLUE_LED)
blueLed.direction = Direction.OUTPUT

while True:
    x, y, z = [value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration]
    #print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))
    print((x,y,z))
    time.sleep(.1)
    if y > 0.3:
        blueLed.value = True
    else: blueLed.value = False

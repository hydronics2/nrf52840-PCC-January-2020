# you're using the lis3d_sh accelerometer
# with increasing tilt in the x-axis, more LEDs light up.

# I had to adjust Adafruit's lis3dh driver/library to work with the lis3d_sh accelerometer on your board.
# not all functions are working but it seems to read all axis and changes from 2g,4g,8g,16g!
# https://www.digikey.com/product-detail/en/stmicroelectronics/LIS3DSHTR/497-13244-1-ND/3635108

import time
import board
import digitalio
from digitalio import DigitalInOut, Direction
import busio
import lis3d_sh # this is NOT the lis3dh Adafruit accelerometer so this lis3d_sh library is used instead (i2c ID is different)

i2c = busio.I2C(board.SCL, board.SDA)
int1 = digitalio.DigitalInOut(board.D2)  # Set to correct pin for interrupt!
accelerometer = lis3d_sh.LIS3DH_I2C(i2c, address=0x1D, int1=int1) #i2 address is 0x1D for the lis3d_sh

accelerometer.range = lis3d_sh.RANGE_8_G #options are 2g,4g,8g,16g

blueLed = DigitalInOut(board.BLUE_LED)
blueLed.direction = Direction.OUTPUT


while True:
    x, y, z = [value / lis3d_sh.STANDARD_GRAVITY for value in accelerometer.acceleration]
    #print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))
    print((x,y,z))
    time.sleep(.1)
    if y > 1: blueLed.value = True
    else: blueLed.value = False

import board
import bleio
from bleio import Service
import time
import digitalio
from digitalio import DigitalInOut, Direction
import busio
import lis3d_sh


i2c = busio.I2C(board.SCL, board.SDA)
int1 = digitalio.DigitalInOut(board.D6)  # Set to correct pin for interrupt!
accelerometer = lis3d_sh.LIS3DH_I2C(i2c, address=0x1D, int1=int1)
accelerometer.range = lis3d_sh.RANGE_2_G


redLed = DigitalInOut(board.D13)
redLed.direction = Direction.OUTPUT

# Create a Characteristic.
chara = bleio.Characteristic(bleio.UUID(0x2A37), read=True, notify=True) #heart rate measurement

# Create a Service providing that one Characteristic.
serv = bleio.Service(bleio.UUID(0x180D), [chara])  # Heart Rate Monitor... just for fun could be anything

# Create a peripheral and start it up.
periph = bleio.Peripheral([serv])
periph.start_advertising()

while not periph.connected:
    # Wait for connection.
    redLed.value = False
    periph.start_advertising()
    time.sleep(.5)
    pass

while periph.connected:
    x, y, z = [value / lis3d_sh.STANDARD_GRAVITY for value in accelerometer.acceleration]
    print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))
    redLed.value = True
    xSign = 1
    ySign = 1
    zSign = 1
    if(x < 0): # capture sign but lets ignore for this example
        xSign = 0
        x = x * -1
    if(y < 0):
        ySign = 0
        y = y * -1
    if(z < 0):
        zSign = 0
        z = z * -1

    x = (int)(x * 100) #change from float to int
    y = (int) (y * 100)
    z = (int) (z * 100)
    chara.value = bytearray([x & 0xFF, y & 0xFF, z & 0xFF])

    time.sleep(.2) #delay 200ms
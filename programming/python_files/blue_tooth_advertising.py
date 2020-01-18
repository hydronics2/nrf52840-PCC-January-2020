
#if your phone or laptop has bluetooh. You can connect to the nrf52840 over bluetooth here
# https://storage.googleapis.com/thomashudson.org/ble/index.html

import board
import bleio
from bleio import Service
import time
import digitalio
from digitalio import DigitalInOut, Direction
import busio
import adafruit_lis3dh

i2c = busio.I2C(board.SCL, board.SDA)
int1 = digitalio.DigitalInOut(board.D5)  # D5 is connected to the interrupt pin on the accelerometer
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)


lis3dh.range = adafruit_lis3dh.RANGE_2_G #options are 2g,4g,8g,16g


greenLed = DigitalInOut(board.D3)
greenLed.direction = Direction.OUTPUT

# Create a Characteristic.
chara = bleio.Characteristic(bleio.UUID(0x2A37), read=True, notify=True) #heart rate measurement

# Create a Service providing that one Characteristic.
serv = bleio.Service(bleio.UUID(0x180D), [chara])  # Heart Rate Monitor... just for fun could be anything

# Create a peripheral and start it up.
periph = bleio.Peripheral([serv])
periph.start_advertising()

while not periph.connected:
    # Wait for connection.
    greenLed.value = False
    periph.start_advertising()
    time.sleep(.5)
    pass

while periph.connected:
    x, y, z = [value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration]
    print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))
    greenLed.value = True
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

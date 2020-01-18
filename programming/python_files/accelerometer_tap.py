import time
import board
import busio
import digitalio
import adafruit_lis3dh

i2c = busio.I2C(board.SCL, board.SDA)
int1 = digitalio.DigitalInOut(board.D5)  # D5 is connected to the interrupt pin on the accelerometer
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)


# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_8_G

# Set tap detection to double taps.  The first parameter is a value:
#  - 0 = Disable tap detection.
#  - 1 = Detect single taps.
#  - 2 = Detect double taps.
# The second parameter is the threshold and a higher value means less sensitive
# tap detection.  Note the threshold should be set based on the range above:
#  - 2G = 40-80 threshold
#  - 4G = 20-40 threshold
#  - 8G = 10-20 threshold
#  - 16G = 5-10 threshold
lis3dh.set_tap(1, 40)

tapCount = 0

# Loop forever printing if a double tap is detected.
while True:
    if lis3dh.tapped:
        tapCount = tapCount + 1
        print("Tap number:", tapCount)
        time.sleep(0.01)

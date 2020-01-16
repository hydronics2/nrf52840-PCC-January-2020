# CircuitPython demo #1 - General Purpose I/O

# blink and hello world in one. Press the serial button above to see the serial output

import time
import board
from digitalio import DigitalInOut, Direction, Pull

blueLed = DigitalInOut(board.BLUE_LED)
blueLed.direction = Direction.OUTPUT
yellowLed = DigitalInOut(board.D3)
yellowLed.direction = Direction.OUTPUT
greenLed = DigitalInOut(board.D13)
greenLed.direction = Direction.OUTPUT

button = DigitalInOut(board.D12)
button.direction = Direction.INPUT
button.pull = Pull.UP

while True:
    print("hello world")
    blueLed.value = True
    time.sleep(.2)
    blueLed.value = False
    yellowLed.value = True
    time.sleep(.2)
    yellowLed.value = False
    greenLed.value = True
    time.sleep(.2)
    greenLed.value = False
    while not button.value:
        yellowLed.value = True
        print("button down")
        time.sleep(.5)
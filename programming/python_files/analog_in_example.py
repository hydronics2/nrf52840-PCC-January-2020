# CircuitPython AnalogIn Demo

# use a potentiometer or a light sensor across 3V, A0, and ground (GND)
# turn an LED on when it gets light or dark
# see pictures

# the A0 analog value is printed. I think it has a 12bit ADC but likely configurable as needed
# 10bit outputs 0-1023 between the values of 0V to 3.3V
# 12bit outputs 0-2046 between the values of 0V to 3.3V
# 14bit outputs 0-16383 between the values of 0V to 3.3V
# the below is behaving as if it is 16bit

import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

analog_in = AnalogIn(board.A0)

blueLed = DigitalInOut(board.BLUE_LED)
blueLed.direction = Direction.OUTPUT


def get_voltage(pin):
    return (pin.value * 3.3) / 65536
    #return pin.value

while True:
    analogValue = get_voltage(analog_in)
    print((analogValue,))
    if analogValue < 2.5:
        blueLed.value = True
    else:
        blueLed.value = False
    time.sleep(0.1)

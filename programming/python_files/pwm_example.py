#pwm is pulse width modulation

import time
import board
import pulseio

greenLed = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0)
yellowLed = pulseio.PWMOut(board.D3, frequency=5000, duty_cycle=0)


while True:
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            yellowLed.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            yellowLed.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(0.01)
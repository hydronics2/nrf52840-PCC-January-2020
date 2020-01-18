# CircuitPython
## https://github.com/hydronics2/nrf52840-PCC-January-2020
If you need to flash a bare board... [here are some steps..](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/firmware/README.md)

I uploaded the python scripts onto the 2MB SPI Flash chip before the class. When you plug the unit into your board it appears as a flash drive.

Download and install the [MU editor](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor) if you have not done so already.

Finally, to find more example code, go through Adafruit's [great tutorial](https://learn.adafruit.com/welcome-to-circuitpython?view=all)


## code.py
LOAD the code.py script. Code.py determines which scripts run. Uncomment the files you would like to run.
###
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/code.jpg)

# 
## blink
LOAD the "blink.py" script that's currently running. It blinks the LEDs on pin 13, pin 3, and BLUE_LED pin. Try adjusting the time.sleep(x) to speed up the blinking. 
###
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/blink.jpg)
# 

## Web Ble
LOAD the blue_tooth_advertising.py script.  Next open a chrome browser and connect through the browser using this address: [BLE WEB App](https://storage.googleapis.com/thomashudson.org/ble/index.html). Or this bit.ly/324KFD8. You have to use the https!
###
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/ble.JPG)
# 
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/chrome_ble2.JPG)
# 

## accelerometer
Modify the code.py script and uncomment accelerometer_led.
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/accelerometer.jpg)
###
The script lights up an LED with increasing tilt.
When you use a print statement with double perenthesis it allows the data to the plotter; such as, print((x,y,z)).
###
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/accel_plot.jpg)
# 

## ws2812_example
Modify the code.py script and unomment a4_ws2812_example
###
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/ws2812_1.JPG)
###
solder three leads onto your LED strip on the correct side (start of the arrow). Insert the LEDs into the screw headers.
LOAD the sketch and modify the "num_leds" variable to the number of LEDs in your strip.
The red, green, and blue LEDs can have values from 0 to 255.
###
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/ws2812_2.JPG)
# 

## analog_in_example
Modify the code.py script and unomment analog_in_example.
Try plugging in both the potentiometer and photocell to see how the analog-to-digital converter(ADC) on pin A0 interprets the signals.
###
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/pot1.JPG)
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/pot2.JPG)
###
Make the photocell voltage divder using a photocell and a 10k resistor.
###
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/photocell2.JPG)
You can see the data on the plotter by using the print statement with extra perenthesis and a comma, "print((analogValue,))"
###
![](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/programming/pics/analog_in_data.JPG)
# 








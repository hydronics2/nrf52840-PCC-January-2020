# Flashing a new nrf52840 module

Download [nrfjprog command line utility](https://www.nordicsemi.com/?sc_itemid=%7B56868165-9553-444D-AA57-15BDE1BF6B49%7D) from nordic semiconductor

Grab yourself a $20 SWD programmer from [digikey/mouser](https://www.mouser.com/ProductDetail/943-8.08.91) (j-link segger)
You'll need to populate (solder) the SWD header onto the board and then plug in your programmer, erase the chip, and flash the hex bootloader.

nrfjprog -f nrf52 --eraseall

nrfjprog --program feather_nrf52840_express_bootloader-0.2.11_s140_6.1.1.hex --chiperase -f nrf52 --reset

Once the hex bootloader is flashed, a folder will open (FTHR840BOOT) and you'll see the USB enumerate. If you have the board files loaded into Arduion, the port will show up as a Feather nrf52840.  Try uploading an Arduino blink sketch for fun.

Next you simply pull the latest circuitpython firmware, UF2 file, over into the FTHR840BOOT folder. As of 6/19/19 the uf2 file looks like this:
adafruit-circuitpython-feather_nrf52840_express-en_US-4.0.1.uf2

That's it. If everything goes right, the RTHR840BOOT folder will close and a CIRCUITPY will open. Now when you open Mu, it will recognize your board as an Adafruit circuitpython board.

![](https://github.com/hydronics2/Teardown-2019/blob/master/programming/firmware/CIRCUITPY.JPG)

Adafruit maintains the hex bootloader [here](https://github.com/adafruit/Adafruit_nRF52_Bootloader/releases)

Adafruit maintains the uf2 circuitpython firmware [here](https://github.com/adafruit/circuitpython/releases)

A bundle of circuitpython libraries can be found [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases)

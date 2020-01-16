# Soldering Instructions

## https://github.com/hydronics2/nrf52840-PCC-January-2020
Parts list
- [Nordic Semiconductor nrf52840 bluetooth module](https://www.adafruit.com/product/4078)
- [SPI QUAD FLASH 2MB Memory](https://www.digikey.com/product-detail/en/gigadevice-semiconductor-hk-limited/GD25Q16CTIGR/1970-1010-1-ND/9484760)


Full parts list on [mouser](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=5d5a690db9).


[Link to schematic](https://github.com/hydronics2/nrf52840-PCC-January-2020/blob/master/soldering/eagle_design_files/schematic.pdf)


![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/1_headers.JPG)
## 11 pin header for accelerometer.

![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/2_10k_pullup.JPG)
## 10K pullup resistor for the CS pin to initiate i2c on the accelerometer.

![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/3_3.3Voltage_reg.JPG)
## 3.3volt regulator and 100n(0.1uF) capacitor
![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/4_330ohmResistors.JPG)
## 4 x Current limiting resistors for the LEDs. ~330ohms but anywhere from 220 to 510 is fine.

![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/5_resistors_at_CS.JPG)

## 2 x 22ohm resistors connect the USB lines to the uController

## 1 x 10K pullup for the reset signal.

## 1 x 10uH ferrite inductor that filters high frequency noise per the mfg recommended layout

![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/6_10uf_caps.JPG)
## 10uF caps along side the bluetooth module per the MFG recomended board layout.

![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/7_headers.JPG)
## 5mm pitch screw headers that we'll use for connecting wires and potentiometers.

![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/8_crystal.JPG)
## 1 x 32.768khz crystal

## 2 x caps along side the crystal. these are 20pF!!!! not 10 as show on the silkscreen.

## 1 x 100nF(0.1uF) bypass capacitor that serves the aref signal per the mfg layout.

![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/9_100uF.JPG)
## 1 x 100uF capacitor serving the 3.3v regulator per the mfg layout.

![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/10_leds.JPG)
## LEDs!! pic whatever color you want. They are directional! Ask your neighbor if you don't know.

![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/11_headers.JPG)
## solder the male headers onto the little acclerometer board.

![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/ws2812.JPG)

## Solder 3 lines onto some WS2812 LEDs.

![](https://github.com/hydronics2/Teardown-2019/blob/master/soldering/pics/22.jpg)

## Solder 3 wires onto the potentiometer.
## That's it. We're all finished! We're leaving a few footprints unpopulated for this class.

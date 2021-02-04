# Raspberry Pico Micropython Scripts

This is a collection of my own experimental Raspberry PI Pico Micropython scripts. These have been generated primarily to help me learn Micropython, so you may see other simpler ways of implementing the code!

If you wish me to include your scripts please post in the discussions tab above.

# SHT21/HTU21 script

This script uses the I2C bus to interface with the SHT21/HTU21 temperature and humidity sensor. The readings are printed to the Shell window.
```
Connections:
    sensor VCC/VIN to Pico 3.3V
    sensor GND     to Pico GND
    sensor SCL     to Pico pin 13
    sensor SDA     to Pico pin 12
```
This is a picture of the module I am using, other board designs are available online that have the same functionality:


![SHT21](https://i.imgur.com/2buOhkE.png)


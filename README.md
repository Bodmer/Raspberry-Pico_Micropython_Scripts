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

# stepper_1_rev script

This script drives a geared stepper motor 1 rev clockwise, then powers down the coils and stops for 1 second. The motor is half stepped to achieve a maximum speed of ~1000 steps per second (1 millisecond per step)
```
Connections:
    motor driver board +(5V) to Pico VBUS
    motor driver board -(0V) to Pico GND
    motor driver board   IN1 to Pico pin 0
    motor driver board   IN2 to Pico pin 1
    motor driver board   IN3 to Pico pin 2
    motor driver board   IN4 to Pico pin 3

```
This is a picture of the 28BYJ-48 motor I am using:

![Motor](https://i.imgur.com/rEpvvsX.png?1)

The motor is driven by a board fitted with a ULN2003 device:

This is a picture of the 28BYJ-48 motor driver board I am using:

![Driver](https://i.imgur.com/OdMqjvX.png)

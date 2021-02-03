# Read SHT21/HTU21 temperature and humidity
# Print results to shell

# Device I2C address = 0x40 (hex) = 64 decimal

# Command registers
# Soft reset = 0xFE

# Write user register = 0xE6
# Read user register = 0xE7

# Trigger temperature reading and hold the bus = 0xE3
# Trigger humidity reading and hold the bus = 0xE5

# Trigger temperature reading without holding the bus = 0xF3
# Trigger humidity reading without holding the bus = 0xF5



STATUS_BITS_MASK = 0xFFFC

from machine import Pin,I2C

import utime

sda=machine.Pin(12)
scl=machine.Pin(13)

i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000) # I2C channel 0, pins, 400kHz max

print("I2C Address       : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration : "+str(i2c))                   # Display I2C config

data = []
address = 64

# The status register must be read and then just the valid control bits changed
i2c.writeto(address, b'\xE7')    # Read user register
data = i2c.readfrom(address, 1)  # Get the 1 byte result
##print ("Status register = " '{:08b}'.format(data[0])) # print as a 8 bit binary with leading zeros

if data[0] & (1<<6):
    print ("Supply voltage is under 2.25V")
else:
    print ("Supply voltage is over 2.25V")

reg = bytearray(1)

reg[0] = (data[0] & 0xFB) # Turn off heater
#reg[0] = (data[0] | 0x04) # Turn on heater

i2c.writeto_mem(address, 0xE6, reg)

# Read the register back to check it has been changed
i2c.writeto(address, b'\xE7')    # Read user register
data = i2c.readfrom(address, 1)  # Get the 1 byte result
#print ("Status register = " '{:08b}'.format(data[0])) # print as a 8 bit binary with leading zeros

if data[0] & (1<<2):
    print ("On-chip heater is ON")
else:
    print ("On-chip heater is OFF")
    
print("Measurement resolution: ",sep=' ', end='') # print with no linefeed

if data[0] & (1<<7):
    if data[0] & (1<<0):
        print ("11 bit humidity, 11 bit temperature")
    else:
        print ("10 bit humidity, 13 bit temperature")
else:
    if data[0] & (1<<0):
        print ("8 bit humidity, 12 bit temperature")
    else:
        print ("12 bit humidity, 14 bit temperature")


# Read humidity
i2c.writeto(address, b'\xF5')   # Trigger humidity measurement
utime.sleep_ms(29)              # Wait for it to finish (29ms max)
data = i2c.readfrom(address, 2) # Get the 2 byte result

adjusted = (data[0] << 8) + data[1]   # convert to 16 bit value
adjusted &= STATUS_BITS_MASK          # zero the status bits
adjusted *= 125                       # scale
adjusted /= 1 << 16                   # divide by 2^16
adjusted -= 6                         # subtract 6

print ("Humidity    = %.1f" % adjusted)


# Read temperature
i2c.writeto(address, b'\xF3')   # Trigger temperature measurement
utime.sleep_ms(85)              # Wait for it to finish (85ms max)
data = i2c.readfrom(address, 2) # Get the 2 byte result

#print (data[0]) # Debug only print byte 0
#print (data[1]) # Debug only print byte 1

## Compute temperature
adjusted = (data[0] << 8) + data[1]   # convert to 16 bit value
adjusted &= STATUS_BITS_MASK          # zero the status bits
adjusted *= 175.72                    # scale
adjusted /= 1 << 16                   # divide by 2^16
adjusted -= 46.85                     # subtract offset

print ("Temperature = %.1f" % adjusted)

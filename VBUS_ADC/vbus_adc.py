# Read the VBUS voltage
import machine
import utime

sensor_v = machine.ADC(3)

# Conversion factor uses a fudge factor of 5.0/3.11 to give the measured value
#                         resistor divider           fudge value    12 bit ADC maximum
conversion_factor = ( ((5600.0 + 10000.0)/10000.0) * (5.0/3.11) ) / 4095.0

while True:
    voltage = sensor_v.read_u16() * conversion_factor
    print("VBUS = %.2f" % voltage)
    utime.sleep(2)
    
## Simple stepper driver code for 5V, 32 step, 64:1 geared motor (2048 steps per rev.)
import machine
import utime

# Stepper driver pins 
led_external1 = machine.Pin(0, machine.Pin.OUT) # IN1
led_external2 = machine.Pin(1, machine.Pin.OUT) # IN2
led_external3 = machine.Pin(2, machine.Pin.OUT) # IN3
led_external4 = machine.Pin(3, machine.Pin.OUT) # IN4

print ("Running")

delay = 1 # number of milliseconds per step (minimum of 1 = 1000 steps/sec)

steps = 1*32*64/4 # 1 rev, 32 steps per rev, 64:1 gear ration, 4 steps in full phase cycle

while True:
    # 1 revolution clockwise (using half-steps allows higher motor speeds to be attained)
    for i in range(steps):
        led_external1.value(0)
        led_external2.value(0)
        led_external3.value(0)
        led_external4.value(1) # Step 0
        utime.sleep_ms(delay)
        led_external1.value(0)
        led_external2.value(0)
        led_external3.value(1) # Half step
        led_external4.value(1)
        utime.sleep_ms(delay)
        led_external1.value(0)
        led_external2.value(0)
        led_external3.value(1) # step 1
        led_external4.value(0)
        utime.sleep_ms(delay)
        led_external1.value(0)
        led_external2.value(1)
        led_external3.value(1) # Half step
        led_external4.value(0)
        utime.sleep_ms(delay)
        led_external1.value(0)
        led_external2.value(1) # Step 2
        led_external3.value(0)
        led_external4.value(0)
        utime.sleep_ms(delay)
        led_external1.value(1) # Half step
        led_external2.value(1)
        led_external3.value(0)
        led_external4.value(0)
        utime.sleep_ms(delay)
        led_external1.value(1) # Step 3
        led_external2.value(0)
        led_external3.value(0)
        led_external4.value(0)
        utime.sleep_ms(delay)
        led_external1.value(1)
        led_external2.value(0)
        led_external3.value(0)
        led_external4.value(1) # Half step
        utime.sleep_ms(delay)

    # Stop phase and next start phase should be the same to avoid loss of steps
    led_external1.value(0)
    led_external2.value(0)
    led_external3.value(0)
    led_external4.value(1)
    utime.sleep_ms(delay) # Wait for last step to complete before removing power

    led_external1.value(0) # Turn off all coils to save power
    led_external2.value(0) # Now relying on motor gearing x detent torque and friction to hold position
    led_external3.value(0)
    led_external4.value(0)

    utime.sleep_ms(2000) # Wait for 2 sec

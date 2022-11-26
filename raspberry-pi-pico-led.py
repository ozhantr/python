import machine
import utime

"""
# Raspberry Pi Pico Internal Led Blink
# Onboard LED Test (GPIO25)
"""

led_onboard = machine.Pin(25, machine.Pin.OUT)
 
while True:
    led_onboard.value(1)
    utime.sleep(1)
    led_onboard.value(0)
    utime.sleep(1)
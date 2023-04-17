from gpiozero import LED
from time import sleep

# PINS
red = LED(18)
green = LED(17)
blue = LED(15)
red.off()
green.off()
blue.off()

# Blink red, green, blue respectively
while True:
    # RED
    red.on()
    green.off()
    blue.off()
    sleep(0.5)
    # GREEN
    red.off()
    green.on()
    blue.off()
    sleep(0.5)
    # BLUE
    red.off()
    green.off()
    blue.on()
    sleep(0.5)



from gpiozero import LED
from time import sleep
import warnings
warnings.filterwarnings('ignore')

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
    red.off()
    green.on()
    blue.on()
    sleep(1)
    # GREEN
    red.on()
    green.off()
    blue.on()
    sleep(1)
    # BLUE
    red.on()
    green.on()
    blue.off()
    sleep(1)



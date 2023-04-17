from gpiozero import Button
from time import sleep

# PINS
# LmSwitch 1: top
# LmSwitch 2: bottom
lmsw1 = Button(5)
lmsw2 = Button(7)

while True:
    if lmsw1.is_pressed:
        print("LmSwitch 1 is pressed!")
    if lmsw2.is_pressed:
        print("LmSwitch 2 is pressed!")
    sleep(0.1)
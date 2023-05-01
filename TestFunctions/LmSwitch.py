from gpiozero import Button
from time import sleep

# PINS
# LmSwitch 1: top
# LmSwitch 2: bottom
lmsw1 = Button(5)
lmsw2 = Button(7)

print(f'First status: LM1 {lmsw1.is_pressed}, LM2 {lmsw2.is_pressed}')

while True:
    # print(f'First status: LM1 {lmsw1.is_pressed}, LM2 {lmsw2.is_pressed}')
    if lmsw1.is_pressed:
        print("LmSwitch 1 is pressed!")
    if lmsw2.is_pressed:
        print("LmSwitch 2 is pressed!")
    sleep(0.01)
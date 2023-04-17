from gpiozero import Button
from time import sleep

# PINS
# Button 1: up
# Button 2: down
# Button 3: Drill and Stop
button1 = Button(8)
button2 = Button(11)
button3 = Button(25)
counter = 0
while True:
    if button1.is_pressed:
        print("Move up!")
    if button2.is_pressed:
        print("Move down!")
    if button3.is_pressed:
        counter += 1
    if counter == 1:
        print("Drill!")
    if counter == 2:
        print("Stop!")
        counter = 0
    sleep(0.1)    

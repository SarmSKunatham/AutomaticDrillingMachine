from gpiozero import LED, PWMLED, Button
from time import sleep
import threading
import os
import warnings
import playsound as ps
warnings.filterwarnings("ignore")

# =====Define the pins=====
# RGB LED
red = LED(18)
green = LED(17)
blue = LED(15)

# Button 1: up
# Button 2: down
# Button 3: Drill and Stop
button1 = Button(8)
button2 = Button(11)
button3 = Button(25)
counter = 0

# LmSwitch 1: top
# LmSwitch 2: bottom
lmsw1 = Button(5)
lmsw2 = Button(7)

# DC Motor controlled with driver
dc_dir = LED(6)
dc_pwm = PWMLED(12, frequency=1000)

# Stepper Motor controlled with driver
dir1 = LED(13)
step1 = PWMLED(19, frequency=800)
en1 = LED(16)
# =====Define the pins=====

# =====Define the functions=====
def move_up():
    step1.blink(on_time=0.001, off_time=0.001, fade_in_time=0, fade_out_time=0, n=None, background=True)
    dir1.off()
    print("Moving up")
    speak("Audios/1. Moving up.wav")

def move_down():
    step1.blink(on_time=0.001, off_time=0.001, fade_in_time=0, fade_out_time=0, n=None, background=True)
    dir1.on()
    print("Moving down")
    speak("Audios/2. Moving down.wav")

def stop_moving():
    step1.off()
    print("Stopped Moving")
    speak("Audios/3. Stopped.wav")

def drill():
    dc_pwm.blink(on_time=0.001, off_time=0.001, fade_in_time=0, fade_out_time=0, n=None, background=True)
    dc_dir.off()
    print("Drilling")
    speak("Audios/4. Start Drilling.wav")

def stop_drilling():
    dc_pwm.off()
    print("Stopped Drilling")
    speak("Audios/7. Stop Drilling.wav")

def speak(audio):
    ps.playsound(audio)

def red_on():
    red.on()
    green.off()
    blue.off()

def green_on():
    red.off()
    green.on()
    blue.off()

def blue_on():
    red.off()
    green.off()
    blue.on()

# =====Define the functions=====

print("Setup complete!!!")
green_on()
speak("Audios/6. Ready to start.wav")

while True:
    # Move up
    if button1.is_pressed:
        move_up()
        red_on()
    # Move down
    if button2.is_pressed:
        move_down()
        red_on()
    
    # Top limit switch
    if lmsw1.is_pressed:
        print("LmSwitch 1 is pressed!")
        stop_moving()
        green_on()
    # Bottom limit switch
    if lmsw2.is_pressed:
        print("LmSwitch 2 is pressed!")
        stop_moving()
        green_on()

    # Controll the drill
    if button3.is_pressed:
        counter += 1
    if counter == 1:
        drill()
        blue_on()
    if counter == 2:
        stop_drilling()
        counter = 0
        green_on()
    
    # Stop moving
    else:
        stop_moving()
        green_on()

    
    

    sleep(0.1)
from gpiozero import LED, PWMLED
from time import sleep

# PINS
# Stepper Motor controlled with driver
dir1 = LED(13)
step1 = PWMLED(19, frequency=800)
en1 = LED(16)

def move_up():
    step1.blink(on_time=0.001, off_time=0.001, fade_in_time=0, fade_out_time=0, n=None, background=True)
    dir1.off()
    print("Moving up")

def move_down():
    step1.blink(on_time=0.001, off_time=0.001, fade_in_time=0, fade_out_time=0, n=None, background=True)
    dir1.on()
    print("Moving down")

def stop():
    step1.off()
    print("Stopped")


while True:
    move_up()
    sleep(1)
    stop()
    sleep(1)
    move_down()
    sleep(1)
    stop()
    sleep(1)


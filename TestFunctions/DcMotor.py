from gpiozero import PWMLED, LED
from time import sleep

# PINS
dc_dir = LED(6)
dc_pwm = PWMLED(12, frequency=1000)

def drill():
    dc_pwm.blink(on_time=0.001, off_time=0.001, fade_in_time=0, fade_out_time=0, n=None, background=True)
    dc_dir.off()
    print("Drilling")

def stop():
    dc_pwm.off()
    print("Stopped")

while True:
    drill()
    sleep(1)
    stop()
    sleep(1)


from gpiozero import PWMLED, LED
from time import sleep

# PINS
# DC Motor controlled with driver
# Swap pin 12, 6 from wiring
dc_dir = LED(12)
dc_pwm = PWMLED(6, frequency=10000)

def drill():
    dc_pwm.blink(on_time=0.001, off_time=0.001, fade_in_time=0, fade_out_time=0, n=None, background=True)
    dc_dir.on()
    print("Drilling")

def stop():
    dc_pwm.off()
    print("Stopped")

stop() 
while True:
    drill()
    sleep(1)
    stop()
    sleep(1)


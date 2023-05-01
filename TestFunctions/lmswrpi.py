import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

pushpin = 5 # set input push button pin
GPIO.setup(pushpin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # with pull up resistor
pushpin2 = 7 # set input push button pin
GPIO.setup(pushpin2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # with pull up resistor

print(f'lm1 {GPIO.input(pushpin)}')
print(f'lm2 {GPIO.input(pushpin2)}')
while True:
    # GPIO.output(ledpin, GPIO.input(pushpin))
    if not GPIO.input(pushpin):
        print('lm1 pressed')
    if not GPIO.input(pushpin2):
        print('lm2 pressed')    
  
    # sleep(1)
from gpiozero import LED, PWMLED, Button
from time import sleep
import threading
import os
import warnings
import speech_recognition as sr
import time
from TestFunctions.playwavfile import playWavFile, audioFiles, audioDir
import os
from threading import Thread
warnings.filterwarnings("ignore")

# =====Define the pins=====
# RGB LED
red = LED(15)
green = LED(17)
blue = LED(18)
red.on()
green.on()
blue.on()

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
dc_dir = LED(12)
dc_pwm = PWMLED(6, frequency=1000)

# Stepper Motor controlled with driver
dir1 = LED(13)
step1 = PWMLED(19, frequency=1000)
en1 = LED(16)
# =====Define the pins=====

# =====Define the functions=====
def move_up():
    # step1.blink(on_time=0.01, off_time=0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    step1.pulse(fade_in_time=5, fade_out_time=0.001, n=None, background=True)
    dir1.off()
    print("Moving up")
    playWavFile("Audios/1. Moving up.wav")

def move_down():
    # step1.blink(on_time=0.01, off_time=0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    step1.pulse(fade_in_time=5, fade_out_time=0.001, n=None, background=True)
    dir1.on()
    print("Moving down")
    playWavFile("Audios/2. Moving down.wav")

def stop_moving():
    step1.off()
    print("Stopped Moving")
    playWavFile("Audios/3. Stopped.wav")

def drill():
    dc_pwm.blink(on_time=10, off_time=0, fade_in_time=0, fade_out_time=0, n=None, background=True)
    # dc_pwm.pulse(fade_in_time=10, fade_out_time=10, n=None, background=True)
    dc_dir.on()
    print("Drilling")
    playWavFile("Audios/4. Start Drilling.wav")

def stop_drilling():
    dc_pwm.off()
    print("Stopped Drilling")
    playWavFile("Audios/7. Stop Drilling.wav")

def red_on():
    red.off()
    green.on()
    blue.on()

def green_on():
    red.on()
    green.off()
    blue.on()

def blue_on():
    red.on()
    green.on()
    blue.off()

# Thread for speech recognition
def speech_recognition():
    global text
    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print('Command should be move up/ move down/ start drilling/ stop drilling.')
            print('Tell your command: ')
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text = text.lower()
            print(f"text: {text}")
            # command 1
            if str(text) in spellLists["move up"]:
                print(f"=====================================")
                print(f"Your command is moving up")
                print(f"=====================================")
                speechFile = os.path.join(audioDir, audioFiles[0])
            # command 2
            elif str(text) in spellLists["move down"]:
                print(f"=====================================")
                print(f"Your command is marking position : move down")
                print(f"=====================================")
                speechFile = os.path.join(audioDir, audioFiles[1])
            # command 3
            elif str(text) in spellLists["start drilling"]:
                print(f"=====================================")
                print(f"Your command is marking position : start drilling")
                print(f"=====================================")
                speechFile = os.path.join(audioDir, audioFiles[3])
            # command 4
            elif str(text) in spellLists["stop drilling"]:
                print(f"=====================================")
                print(f"Your command is marking position : stop drilling")
                print(f"=====================================")
                speechFile = os.path.join(audioDir, audioFiles[6])
            # command 5
            elif str(text) in spellLists["stop"]:
                print(f"=====================================")
                print(f"Your command is marking position : stop")
                print(f"=====================================")
                speechFile = os.path.join(audioDir, audioFiles[2])
            else:
                print('Please give a right command.')
                speechFile = os.path.join(audioDir, audioFiles[4])
                playWavFile(speechFile)
                text = ""
                continue
        except:
            print('Sorry could not recogonize your voice.')
            speechFile = os.path.join(audioDir, audioFiles[4])
            playWavFile(speechFile)
            text = ""
            continue
        playWavFile(speechFile)
        text = ""

# Main Thread
def main():
    # global text
    counter = 0
    counterDrill = 0
    prevDrill = 0
    prev = 0
    while True:
          # Controll the up down
        if not button3.is_pressed:
            counter += 1
    #     # Move up
        if (counter == 1 and prev != counter) or (str(text) in spellLists["move up"]):
            move_up()
            red_on()
            prev = counter
    #     # Move down
        if (counter == 2 and prev != counter) or (str(text) in spellLists["move down"]):
            move_down()
            red_on()
            counter = 0
            prev = counter
        
    #     # # Top limit switch
    #     # if lmsw1.is_pressed:
    #     #     print("LmSwitch 1 is pressed!")
    #     #     stop_moving()
    #     #     green_on()
    #     # # Bottom limit switch
    #     # if lmsw2.is_pressed:
    #     #     print("LmSwitch 2 is pressed!")
    #     #     stop_moving()
    #     #     green_on()

    #   
    #     # Start drilling
        if not button1.is_pressed:
            counterDrill += 1
        if (counterDrill == 1 and prevDrill != counterDrill) or str(text) in spellLists["start drilling"]:
            drill()
            blue_on()
            prevDrill = counterDrill
            
        # Stop drilling   
        if (counterDrill == 2 and prevDrill != counterDrill) or str(text) in spellLists["stop drilling"]:
            stop_drilling()
            green_on()
            counterDrill = 0
            prevDrill = counterDrill
            
        
    #     # Stop moving
        if not button2.is_pressed or str(text) in spellLists["stop"]:
            stop_moving()
            green_on()
        # else:
        #     stop_moving()
        #     green_on()


# =====Define the functions=====

# =====Setup=====
# Microphone
mic = sr.Microphone(2)
# Recognizer
r = sr.Recognizer()


spellLists = {
    "move up": ["move up","couldn't", "moving up", 'coon', "go up", "going up", "move app", "moving app"],
    "move down": ["move down", "move doll", 'long', "moving down", "moving doll", "go down", "going down", "go doll", "going doll", "mcdowell"],
    "start drilling": ["start", 'moon', "start drilling", "start drooling", "drooling", 'start doin', 'start doing', "drilling", "dooling", "drill", "dealing", "start dealing", "spot juuling", "start tingling", "spiderling", "bad drooling", "juuling", "spot drilling", "bad ruling", "start giggling", "todd dewey", "sparkling", "spot"],
    "stop drilling": ["stop juuling", "stop giggling", 'stop doing', 'stop doin', "stop vierling", 'stop dueling', "stop their drill", "stop dead through", "stop drooling", "stop drilling", "stop the drill", "stop the deal", "stop dealing", "set up dealing", "stop doing"],
    "stop": ["stop", "stop moving", "stop movie", 'use', 'paul'],
}
speechFile = os.path.join(audioDir, audioFiles[5])
playWavFile(speechFile)
green_on()
text = ""
print("Setup complete!!!")

# =====Setup=====

# =====Main Thread=====
if __name__ == "__main__":
    # Thread for speech recognition
    t1 = threading.Thread(target=speech_recognition)
    t1.start()
    t2 = threading.Thread(target=main)
    t2.start()



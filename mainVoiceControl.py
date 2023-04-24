from gpiozero import LED, PWMLED, Button
from time import sleep
import threading
import os
import warnings
import playsound as ps
import speech_recognition as sr
import time
from TestFunctions.SpeechSynthesisFunction import speechSynthesis, audioFiles, audioDir
import os
from threading import Thread
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

# Thread for speech recognition
def speech_recognition():
    global text
    while True:
        with mic as source:
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
                speechSynthesis(speechFile)
                text = ""
                continue
        except:
            print('Sorry could not recogonize your voice.')
            speechFile = os.path.join(audioDir, audioFiles[4])
            speechSynthesis(speechFile)
            text = ""
            continue
        speechSynthesis(speechFile)
        text = ""

# Main Thread
def main():
    while True:
        # Move up
        if button1.is_pressed or str(text) in spellLists["move up"]:
            move_up()
            red_on()
        # Move down
        if button2.is_pressed or str(text) in spellLists["move down"]:
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
        # Start drilling
        if counter == 1 or str(text) in spellLists["start drilling"]:
            drill()
            blue_on()
        if counter == 2 or str(text) in spellLists["stop drilling"]:
            stop_drilling()
            counter = 0
            green_on()
        
        # Stop moving
        if str(text) in spellLists["stop"]:
            stop_moving()
            green_on()
        else:
            stop_moving()
            green_on()

        sleep(0.1)

# =====Define the functions=====

# =====Setup=====
# Microphone
mic = sr.Microphone(2)
# Recognizer
r = sr.Recognizer()

spellLists = {
    "move up": ["move up", "moving up", "go up", "going up", "move app", "moving app"],
    "move down": ["move down", "move doll", "moving down", "moving doll", "go down", "going down", "go doll", "going doll", "mcdowell"],
    "start drilling": ["start", "start drilling", "start drooling", "drooling", "drilling", "dooling", "drill", "dealing", "start dealing", "spot juuling", "start tingling", "spiderling", "bad drooling", "juuling", "spot drilling", "bad ruling", "start giggling", "todd dewey", "sparkling", "spot"],
    "stop drilling": ["stop juuling", "stop giggling", "stop vierling", "stop their drill", "stop dead through", "stop drooling", "stop drilling", "stop the drill", "stop the deal", "stop dealing", "set up dealing", "stop doing"],
    "stop": ["stop", "stop moving", "stop movie"],
}
speechFile = os.path.join(audioDir, audioFiles[5])
speechSynthesis(speechFile)
green_on()
text = ""
print("Setup complete!!!")

# =====Setup=====

# =====Main Thread=====
if __name__ == "__main__":
    # Thread for speech recognition
    t1 = threading.Thread(target=speech_recognition)
    t1.start()
    main()



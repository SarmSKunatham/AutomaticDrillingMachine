import speech_recognition as sr
import time
from SpeechSynthesisFunction import speechSynthesis, audioFiles, audioDir
import os

# To check the microphone index
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
# Microphone
mic = sr.Microphone(2)
# Recognizer
r = sr.Recognizer()

spellLists = {
    "move up": ["move up", "moving up", "go up", "going up"],
    "move down": ["move down", "move doll", "moving down", "moving doll", "go down", "going down", "go doll", "going doll", "mcdowell"],
    "start drilling": ["start", "start drilling", "start drooling", "drooling", "drilling", "dooling", "drill", "dealing", "start dealing", "spot juuling", "start tingling", "spiderling", "bad drooling", "juuling", "spot drilling", "bad ruling", "start giggling", "todd dewey", "sparkling", "spot"],
    "stop drilling": ["stop juuling", "stop giggling", "stop vierling", "stop their drill", "stop dead through", "stop drooling", "stop drilling", "stop the drill", "stop the deal", "stop dealing", "set up dealing", "stop doing"],
    "stop": ["stop", "stop moving", "stop movie"],
}
speechFile = os.path.join(audioDir, audioFiles[5])
speechSynthesis(speechFile)
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
            continue
    except:
        print('Sorry could not recogonize your voice.')
        speechFile = os.path.join(audioDir, audioFiles[4])
        speechSynthesis(speechFile)
        continue
    speechSynthesis(speechFile)
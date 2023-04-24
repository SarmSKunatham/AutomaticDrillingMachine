# Test synthesis sound from .wav file
import playsound as ps
import os

audioDir = os.getcwd() + "/Audios/"
audioFiles = os.listdir("Audios")
audioFiles.sort()

def speechSynthesis(audio):
    print(audio)
    ps.playsound(audio)





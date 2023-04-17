# Test synthesis sound from .wav file
import playsound as ps
import os

def speechSynthesis(audio):
    print(audio)
    ps.playsound(audio)

audioDir = os.getcwd() + "/Audios/"
audioFiles = os.listdir("Audios")

while True:
    try:
        fileIndex = int(input("Enter file index: "))
        if fileIndex >= len(audioFiles) or fileIndex < 0:
            print("File index out of range")
            break
        audio = os.path.join(audioDir, audioFiles[fileIndex])
        speechSynthesis(audio)
    except:
        print("Done")


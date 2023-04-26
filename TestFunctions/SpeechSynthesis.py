# Test synthesis sound from .wav file
import playwavfile as pwf
import os

def speechSynthesis(audio):
    print(audio)
    pwf(audio)

audioDir = os.getcwd() + "/Audios/"
audioFiles = os.listdir("Audios")
audioFiles.sort()
print(audioFiles)

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


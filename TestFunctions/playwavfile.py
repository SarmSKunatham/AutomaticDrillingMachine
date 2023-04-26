
# import required module
import simpleaudio as sa
import os

audioDir = os.getcwd() + "/Audios/"
audioFiles = os.listdir("Audios")
audioFiles.sort()

def playWavFile(audiofile):

    # define an object to play
    wave_object = sa.WaveObject.from_wave_file(audiofile)
    print('play ', audiofile)
    
 
    # define an object to control the play
    play_object = wave_object.play()
    play_object.wait_done()

# playWavFile('/home/pi/Desktop/AutomaticDrillingMachine/Audios/1. Moving up.wav')
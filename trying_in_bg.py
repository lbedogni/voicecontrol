import speech_recognition as sr
import subprocess
import urllib
import os

# obtain audio from the microphone
r = sr.Recognizer()
r.energy_threshold = 4000
r.pause_threshold = 0.2
r.timeout = 2
r.non_speaking_duration = 0.2
r.dynamic_energy_threshold = True

def callbackAudio(myAudio, myOther):
    print("HERE I AM")
    command = "nothing"
    entity = ""
    try:
        phrase = r.recognize_google(myOther, language = "it-IT").lower()
        print(phrase)
        if "accend" in phrase:
            command = "on"
        elif "spegn" in phrase:
            command = "off"

        if "sala" in phrase:
            entity = 3
        elif "bagno" in phrase:
            entity = 2
        elif "camera" in phrase:
            entity = 1
        elif "tutto" in phrase:
            entity = 0
       
        if command != "nothing":
            print("php switch.php " + str(command) + " " + str(entity))
            os.system("php switch.php " + str(command) + " " + str(entity))

    except sr.UnknownValueError:
        print("Unknown")
    except:
        print("Other Error")

source = sr.Microphone()
r.listen_in_background(source, callbackAudio)

while True:
    pass

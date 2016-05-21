import speech_recognition as sr
import subprocess
import urllib
import sys
import pyaudio

# obtain audio from the microphone
r = sr.Recognizer()
r.energy_threshold = 4000
r.pause_threshold = 0.2
r.non_speaking_duration = 0.2
r.dynamic_energy_threshold = True

import wave
wf = wave.open('bark.wav','r')
pau = pyaudio.PyAudio()
stream = pau.open(format=pau.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True)
data = wf.readframes(1024)
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(1024)
stream.stop_stream()
stream.close()

# close PyAudio (5)
pau.terminate()

while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print("Acquired, now we recognize.")
        try:
            phrase = r.recognize_google(audio, language = "it-IT").lower()
        except (sr.UnknownValueError):
            phrase = ""
        except (urllib.HTTPError):
            phrase = ""
        print(phrase)
        location = 0
        if "sala" in phrase:
            location = 3
        elif "bagno" in phrase:
            location = 2
        elif "camera" in phrase:
            location = 1
        elif "tutto" in phrase:
            location = 0

        import os
        if "accendi" in phrase.lower():
            print("Switching on")
            #subprocess.call(["php", "switch.php", "on", str(location)])
            print("php switch.php on " + str(location))
            os.system("php switch.php on " + str(location))
        else:
            print("Switching off")
            #subprocess.call(["php", "switch.php", "off", str(location)])
            print("php switch.php off " + str(location))
            os.system("php switch.php off " + str(location))

    sys.exit(1)

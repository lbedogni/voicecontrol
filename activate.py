import sys, os, pyaudio
from pocketsphinx import *

modeldir = "/usr/local/share/pocketsphinx/model"
modeldir = "../../pocketsphinx-5prealpha/model/en-us/"
modeldir = "model/"
# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', os.path.join(modeldir, 'hmm/en_US/hub4wsj_sc_8k'))
config.set_string('-dict', os.path.join(modeldir, 'lm/en_US/cmu07a.dic'))
config.set_string('-keyphrase', 'leopoldo')
config.set_float('-kws_threshold', 1e-30)

decoder = Decoder(config)
decoder.start_utt()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()        

while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
    else:
         break
    if decoder.hyp() != None:
        print ([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()])
        print ("Detected keyword, restarting search")
        decoder.end_utt()
        stream.stop_stream()
        import subprocess
        #subprocess.call(["python3","trying.py"])
        subprocess.call(["python3","recognize_background.py"])
        stream.start_stream()
        decoder.start_utt()

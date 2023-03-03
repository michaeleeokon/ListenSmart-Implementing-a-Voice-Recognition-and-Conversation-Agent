#!/usr/bin/python3

import pyaudio
import wave
from datetime import datetime as dt
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input= True, frames_per_buffer= FRAMES_PER_BUFFER)
print("Start recording\n"+"*"*12)
seconds = 10
frames = []
for i in range(0,int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)
stream.stop_stream()
stream.close 
p.terminate 


obj = wave.open(dt.now(),"wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames)) 
obj.close()

print("Recording finish")

import sounddevice as sd
import numpy

fs = 44100
seconds = 3

def callback(indata, outdata, frames, time, status):
  if status:
    print(status)
  outdata[:] = indata

with sd.Stream(channels=2, callback=callback):
  sd.sleep(int(seconds * 1000))


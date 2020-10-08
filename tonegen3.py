import numpy
import pyaudio
import math
from time import sleep
#from sprit1 import stop
#from sprit1 import xx
 
 
class ToneGenerator(object):
 
    def __init__(self, samplerate=44100, frames_per_buffer=4410):
        self.p = pyaudio.PyAudio()
        self.samplerate = samplerate
        self.frames_per_buffer = frames_per_buffer
        self.streamOpen = False
 
    def sinewave(self):
        if self.buffer_offset + self.frames_per_buffer - 1 > self.x_max:
            # We don't need a full buffer or audio so pad the end with 0's
            xs = numpy.arange(self.buffer_offset,
                              self.x_max)
            tmp = self.amplitude * numpy.sin(xs * self.omega)
            out = numpy.append(tmp,
                               numpy.zeros(self.frames_per_buffer - len(tmp)))
        else:
            xs = numpy.arange(self.buffer_offset,
                              self.buffer_offset + self.frames_per_buffer)
            out = self.amplitude * numpy.sin(xs * self.omega)
        self.buffer_offset += self.frames_per_buffer
        return out
 
    def callback(self, in_data, frame_count, time_info, status):
        if self.buffer_offset < self.x_max:
            data = self.sinewave().astype(numpy.float32)
            return (data.tostring(), pyaudio.paContinue)
        else:
            return (None, pyaudio.paComplete)
 
    def is_playing(self):
        if self.stream.is_active():
            return True
        else:
            if self.streamOpen:
                self.stream.stop_stream()
                self.stream.close()
                self.streamOpen = False
            return False
 
    def play(self, frequency, duration, amplitude):
        self.omega = float(frequency) * (math.pi * 2) / self.samplerate
        self.amplitude = amplitude
        self.buffer_offset = 0
        self.streamOpen = True
        self.x_max = math.ceil(self.samplerate * duration) - 1
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=self.samplerate,
                                  output=True,
                                  frames_per_buffer=self.frames_per_buffer,
                                  stream_callback=self.callback)
 
 
###############################################################################
#                                 Usage Example                               #
###############################################################################
 
generator = ToneGenerator()
counter = 0
#stop = 0
xx = "1"
#if (stop == 1):
#    for x in range(15):
#        
#        if (xx == "0"):
#            break

xn = 1
frequency = 50 
frequency_start = 50        # Frequency to start the sweep from
frequency_end = 50       # Frequency to end the sweep at
num_frequencies = 1       # Number of frequencies in the sweep
amplitude = 0.50            # Amplitude of the waveform
        # Time (seconds) to play at each step
 
#for frequency in numpy.logspace(math.log(frequency_start, 10),
                                #math.log(frequency_end, 10),
                                #num_frequencies):
 
while True: 
    cmd1 = input("do you want to start?")
    if (cmd1 == 'yes'):
        print("Playing tone at {0:0.2f} Hz".format(frequency))
        for x in range(10000): 
            counter = 1000
            step_duration = counter
            generator.play(frequency, step_duration, amplitude)
            cmd = input("do you want to stop?")
            if (cmd == 'yes'):
                break
        break
    while generator.is_playing():
        #xx = input("do you want to stop?")
        #print(xx)
        if (xx == "0"):
            exit()
        pass                # Do something useful in here (e.g. recording)
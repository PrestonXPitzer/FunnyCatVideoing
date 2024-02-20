import pyaudio
import wave

# Open a new audio stream object
def openAudioStream() -> pyaudio.Stream:
    pa = pyaudio.PyAudio()
    stream_in = pa.open(format=pyaudio.paInt32, channels=1, rate=48000, input=True, frames_per_buffer=1024)

    return stream_in

"""
Read the audio stream and return an intensity value as 
an integer between 1 and 24 (inclusive).  
"""
def getCurrrentAudioIntensity(stream: pyaudio.Stream) -> int:
    stream_data = stream.read(1024)
    intensity = 0
    for i in range(0, len(stream_data), 4):
        intensity += abs(int.from_bytes(stream_data[i:i+4], byteorder='little', signed=True))
    return intensity

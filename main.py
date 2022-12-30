import speech_recognition as r
from speech_recognition.__main__ import source

r.adjust_for_ambient_noise(source)
with r.Microphone(device_index=2) as source:

    print("Speak Anything :")
    audio = r.listen(source)

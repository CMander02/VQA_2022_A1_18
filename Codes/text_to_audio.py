from gtts import gTTS
from playsound import playsound
import os


def text_to_audio(input_text,filename):
    language = 'en'
    myobj = gTTS(text=input_text, lang=language, slow=False)
    myobj.save(filename)
    playsound(filename)
    os.remove(filename)
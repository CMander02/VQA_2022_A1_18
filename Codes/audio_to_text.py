import speech_recognition as sr

def audio_to_text():
    r = sr.Recognizer()
    # Microphone
    mic = sr.Microphone()
    print("Listening")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print("Translating")
    test = r.recognize_google(audio, language='en-US', show_all=True)
    try:
        return_text=test['alternative'][0]
        print(return_text)
    except:
        print("Audio to text error")
    return test['alternative'][0]

# audio_to_text()

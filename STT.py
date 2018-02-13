import speech_recognition as sr
# obtain audio from the microphone
r = sr.Recognizer()
def say_something():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source) # adapt to the noise
        print("Say Something")
        audio =  r.listen(source)
    try:
        print("MJ thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("MJ could not understand what you said")
    except sr.RequestError as e:
        print("MJ error; {0}".format(e))
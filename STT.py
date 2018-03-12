import speech_recognition as sr
import TTS_Google

def talk():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        mjAudio = r.recognize_google(audio)
        try:
            print ("You said: " + mjAudio)
        except sr.UnknownValueError:
            TTS_Google.speak('I could not understand what you said','en')
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return r.recognize_google(audio)


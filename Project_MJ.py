import TTS_Google
import random
#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
 
hellos = ["hey", "hi", "hello", "how is it going"]
def say_hello(hellos):
    return random.choice(hellos)

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    mjAudio = r.recognize_google(audio)
 
# Speech recognition using Google Speech Recognition
try:
    #here goes everything MJ will do if she understand you
    print ("You said: " + mjAudio)

    #Profile set
    #Process
    #Math/Google Search/Reading of a file or web page
    #Do It
    #Get answer of what was asked for and what was asked for
    #Interpretate Answer

    #Return Spoken Answer
    if mjAudio in hellos:
        text = say_hello(hellos)
    elif mjAudio == "hello there":
        text = "general kenobi"
    else:
        text = "I am not self conscious, yet"

    TTS_Google.speak(text,'en')
    
except sr.UnknownValueError:
    TTS_Google.speak('I could not understand what you said','en')
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
#Profile set
#Process
#Math/Google Search/Reading of a file or web page
#Do It
#Get answer of what was asked for and what was asked for
#Interpretate Answer
#Return Spoken Answer

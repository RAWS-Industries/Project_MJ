import TTS_Google
#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
 
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print ("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
#Profile set
#class God (object):

#    species = "Devine"

#    def __init__ (self, user_Name, user):
       
 #       self.user_Name = user_Name
  #      self.user = user

#WS = God ("WS","Sebastián")
    
#def setuser (WS):
 #       if WS.__class__ == God:
  #          print (WS.user + " has full access.")

#class CPU (object):



#Process
#Math/Google Search/Reading of a file or web page
#Do It
#Get answer of what was asked for and what was asked for
#Interpretate Answer
#Return Spoken Answer
text = r.recognize_google(audio)
TTS_Google.speak(text,'en')
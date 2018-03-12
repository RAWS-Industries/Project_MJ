import TTS_Google
import random
import Google_Search
import STT
import MJ_CPU

#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
search = ("search", "google", "investigate", "research")
hello = ("hello", "hey", "hi", "hello there")

#Recognize voice
mjAudio = STT.talk()
#Separate by words
mj = mjAudio.split() 
#command to run
mjAudio0 = mj[0]
#After de first word are the commands
mjAudio1 = mj[1:]
#keywords and commands

#    else:
 #       return "I do not know how to do that yet"


MJ_CPU.select_command(mjAudio0,mjAudio1)
text = MJ_CPU.select_command(mjAudio0,mjAudio1)


#Math/Google Search/Reading of a file or web page
#Do It
#Get answer of what was asked for and what was asked for
#Interpretate Answer

    #Return Spoken Answer
#    if mjAudio in hello:
 #       text = say_hello(hellos)
  #  elif mjAudio == "hello there":
   #     text = "general kenobi"
    #else:
     #   text = "I am not self conscious, yet"



# Speech recognition using Google Speech Recognition
TTS_Google.speak(text,'en')
    


#here goes everything MJ will do if she understand you
#Profile set
#Process
#Math/Google Search/Reading of a file or web page
#Do It
#Get answer of what was asked for and what was asked for
#Interpretate Answer
#Return Spoken Answer

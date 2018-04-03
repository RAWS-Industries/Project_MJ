import TTS_Google
import random
import Google_Search
import STT
import MJ_CPU

#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

#Recognize voice
mjAudio = STT.talk()
#Separate by words
mj = mjAudio.split() 
#command to run
mjAudio0 = mj[0]
#Parameters for the command
mjAudio1 = mj[1:]

#Run command selector
text = MJ_CPU.select_command(mjAudio0,mjAudio1)

# Speech recognition using Google Speech Recognition
TTS_Google.speak(text,'en')
    

import TTS_Google
import random
import Google_Search
import STT
import MJ_CPU

#MJ will do any number of things until you say thank you (be polite)
mjAudio = ""
terminator = ["thank you MJ", "thanks MJ","that's it", "that's it MJ", "no", "no thanks", "no thank you","thank you", "no thanks MJ", "no thank you MJ"]
TTS_Google.speak('what can I help you with today','en')
while mjAudio not in terminator:
    #recognize audio
    mjAudio = STT.talk()
    mjAudio.lower()
    if mjAudio not in terminator: #Avoids another repetition when "thank you MJ is said"
        #Separate the command and the specifications
        mj = mjAudio.split() 
        mjAudio0 = mj[0]
        mj.pop(0)
        mjAudio1 = " ".join (mj)
        #Run command selector
        text = MJ_CPU.select_command(mjAudio0,mjAudio1)
        # Speech recognition using Google Speech Recognition
        TTS_Google.speak(text,'en')
        #Ask for another command
        TTS_Google.speak('do you need me to do something else?','en')
else:
    TTS_Google.speak("You are welcome",'en')    

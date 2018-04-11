import TTS_Google
import random
import Google_Search
import STT
import MJ_CPU

#MJ will do any number of things until you say thank you (be polite)
mjAudio = ""
terminator = ["thank you MJ", "thanks MJ","that's it", "that's it MJ", "no", "no thaks", "no thank you"]
while mjAudio not in terminator:
    #recognize audio
    mjAudio = STT.talk()
    if mjAudio not in terminator: #Avoids another repetition when "thank you MJ is said"
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
        #Ask for another command
        TTS_Google.speak('do you need me to do something else?','en')
else:
    TTS_Google.speak("You are welcome",'en')    

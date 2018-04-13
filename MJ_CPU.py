import random
import Google_Search
import MJ_Math

search = ["search","google","look"]
hello = ["hello", "hey", "hi", "hello there"]
operate = ["what's", "how much is", "solve","what is"]
say = ["repeat", "say"]

def say_hello(mjAudio):
    hi = ("hello", "hey", "hi", "hello there")
    if mjAudio in hi:
        hellos = ["hey", "hi", "hello", "how is it going"]
        return random.choice(hellos)
    elif mjAudio == 'hello there':
        return "general kenobi"

def search_for (searchfor):
    Google_Search.google_search(searchfor)
    return "This is what you searched for"

def solve (num1, num2, operator):
    return str (MJ_Math.select_Math(num1, num2, operator))

def repeat(mjAudio1):
    return mjAudio1

def select_command (mjAudio0,mjAudio1):
    if mjAudio0 in search:
        return search_for(mjAudio1)
    elif mjAudio0 in hello:
        return say_hello(mjAudio0)
    elif mjAudio0 in operate:
        mA = mjAudio1.split()
        num1 = int (mA [0])
        operand = mA [1]
        num2 = int (mA [2])
        return solve (num1,num2,operand)
    elif mjAudio0 in say:
        return repeat(mjAudio1)
    else:
        return "I do not know how to do that yet"



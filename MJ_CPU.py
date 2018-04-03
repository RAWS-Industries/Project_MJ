import random
import Google_Search
search = ["search","google","look"]
hello = ["hello", "hey", "hi", "hello there"]


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

def select_command (mjAudio0,mjAudio1):
    if mjAudio0 in search:
        return search_for(mjAudio1)
    elif mjAudio0 in hello:
        return say_hello(mjAudio0)
    else:
        return "I do not know how to do that yet"


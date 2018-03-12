import random
import Google_Search



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

#search = ("search", "google", "investigate", "research")
#hello = ("hello", "hey", "hi", "hello there")
#search = ("search", "google", "investigate", "research")
#hello = ("hello", "hey", "hi", "hello there")
mjCommands = {('search','look'):search_for}
#mjCommands['search'] = search_for,
#hello:say_hello

#Profile set
#Process


def select_command (mjAudio0,mjAudio1):
#    if mjAudio0 in mjCommands.keys():
       return mjCommands[mjAudio0](mjAudio1)

select_command ('search','dragon')

#    def think ():
#        while mjAudio != "that would be all":
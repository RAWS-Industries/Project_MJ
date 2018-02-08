"This module will set the user and it's type from the user's input"

class User(object):
    "This class is the base class for all users"
    def __init__(self, user_Name, user):
        self.user_Name = user_Name
        self.user = user

    def get_user (self):
        "This function returns who's profile it's signed in"
        return self.user_Name + " " + self.user

class God(object):
    "This class is the default class for the creators of the programm"

    species = "Devine"

    def __init__(self, user_Name, user, clearance):
        User.__init__(self, user_Name, user)
        self.clearance = clearance


users = {}

users['S'] = WS = God("WS", "Sebastián", "1113")
users['JL'] = JL = God("JL", "Chepe", "with clearance code: 1113")
users['A'] = AR = God("AR", "Annie", "with clearance code: 1113")
users['MPH'] = MP = God("MP", "Marco", "with clearance code: 1113")
users['MX'] = MX = God("MX", "Max", "with clearance code: 1113")
users['SF'] = SF = God("SF", "Sofi", "with clearance code: 1113")

#Voice input
userInput = God("S", "Sebastián", "1113")
user2 = User("S", "Sebastián")

def set_user(God):
    "This function determines the type of user, and checks the password"
    if userInput.user_Name in users:
        if userInput.clearance == users[userInput.user_Name].clearance:
            return users[user2.user_Name]
        else:
            print("Wrong password")
    else:
        print("No such user found")



#class Cyborg (object):


#class Mortal (object):



#def pass_check (theUser):
 #       if theUser.__class__ == God:
 #           print (theUser.user + " " + theUser.clearance + " " + " has full access.")
 #       elif the_User.__class__ == Cyborg:
 #           print (the_User.user + " " + the_User.clearance + " " + " has developer access.")
 #       elif the_User.__class__ == Mortal:
 #           print (the_User.user + " " + the_User.clearance + " " + " has basic access.")
             

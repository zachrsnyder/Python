import random

class Animal:
    mood_switch = {
        1: "happy",
        2: "hungry",
        3: "sleepy",
    }
    def decide_mood(self):
        x = random.randrange(1,4)
        self.__mood = Animal.mood_switch.get(x)
    
    def __init__(self, _type, name):
        self.__animal_type = _type
        self.__name = name
        self.decide_mood()

    def get_animal_type(self):
        return self.__animal_type
    
    def get_name(self):
        return self.__name
    
    def check_mood(self):
        return self.__mood


        

        
        

        
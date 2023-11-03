from Animal import Animal
from Animal import Mammal
from Animal import Bird

def main():
    animal_list = []
    print("Welcome to the animal generator!\nThis program creates Animal Objects.\n")
    while True:    
        while True:
            try:
                decision = int(input("Would you like to create a mammal or bird?\n1. Mammal\n2. Bird\nWhich would you like to create? "))
                if(decision == 1):
                    species = input("What type of mammal would you like to create? ")
                    name = input("What is the mammal's name? ")
                    hair = input("What color is the mammal's hair? ")
                    animal_list.append(Mammal(species, name, hair))
                elif(decision == 2):
                    species_bird = input("What type of bird would you like to create? ")
                    name_bird = input("What would you like to name the bird? ")
                    fly = input("Can this bird fly? ")
                    animal_list.append(Bird(species_bird, name_bird, fly))
                else:
                    print("Invalid number please try again\n")
                    continue
            except Exception as e:
                print(f"An {e} error occurred\n")
            else:
                break
        new = input("Would you like to add more animals (y/n)? ")
        if(new != "y"):
            print("Animal List:\n")
            for x in animal_list:
                print(f"{Animal.get_name(x)} the {Animal.get_animal_type(x)} is {Animal.check_mood(x)}\n")
            break

main()
        


    
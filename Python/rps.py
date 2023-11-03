import random
import pickle

rps_dict = {
    0: "Rock",
    1: "Paper",
    2: "Scissors",
}

def game_menu():
    while True:
        try:
            print("1. Play Again\n2. View Statistics\n3. Quit\n\n")
            choice = int(input("Enter choice: "))
            if(choice > 3 or choice < 0):
                print("Please enter a number 1-3\n")
                continue
        except ValueError:
            print("Please enter a number 1-3\n")
        else:
            return choice


def newGame():
    name = input("What is your name? ")
    curr_round = 1
    print(f"Hello {name}. Lets play!\n\n")
    wins = 0
    losses = 0
    ties = 0
    while True:
        print(f"Round {curr_round}\n\n")
        try:
            print("1. Rock\n2. Paper\n3. Scissors\n\n")
            A = int(input("What will it be? ")) - 1
            if(A > 2 or A < 0):
                print("Please enter a number between 1 and 3\n\n")
                continue
            B = random.randrange(0,3)
            winner = (3 + A - B) % 3
            if(winner == 0):
                ties += 1
                print(f"You chose {rps_dict.get(A)}. The computer chose {rps_dict.get(B)}. You tied!\n\n")
            elif(winner == 1):
                wins += 1
                print(f"You chose {rps_dict.get(A)}. The computer chose {rps_dict.get(B)}. You win!\n\n")
            elif(winner == 2):
                losses += 1
                print(f"You chose {rps_dict.get(A)}. The computer chose {rps_dict.get(B)}. You lose!\n\n")
        except ValueError:
            print("Please enter your answer as a number between one and 3\n\n")
        else:
            print("What would you like to do?\n\n")
            choice = game_menu()
            while True:
                if(choice == 1):
                    curr_round += 1
                    break
                elif(choice == 2):
                    print(f"{name}, here are your game play statistics...\n")
                    if(losses == 0):
                        ratio = float(wins)
                    else:
                        ratio = wins/losses
                    print(f"Wins: {wins}\nLosses: {losses}\nTies: {ties}\nWin\Loss Ratio: {ratio}")
                    choice = game_menu()
                elif(choice == 3):
                    with open(f"{name}.rps", "wb") as outfile:
                        pickle.dump(f"User: {name}\n", outfile)
                        pickle.dump(f"Wins: {wins}\n", outfile)
                        pickle.dump(f"Losses: {losses}\n", outfile)
                        pickle.dump(f"Ties: {ties}\n", outfile)
                    print(f"\n{name}, your game has been saved\n")
                    return
                
def loadGame():
    name = input("What is your name? ")
    print(f"Welcome back {name}. Let's play\n\n")
    with open(f"{name}.rps", "rb") as b:
        name = pickle.load(b)
        wins = pickle.load(b)
        losses = pickle.load(b)
        ties = pickle.load(b)
        name = name.strip(' \n')[6:]
        wins = int(wins.strip(' ')[6:])
        losses = int(losses.strip(' ')[8:])
        ties = int(ties.strip(' ')[6:])
    curr_round = wins + losses + ties + 1
    while True:
        print(f"Round {curr_round}\n\n")
        try:
            print("1. Rock\n2. Paper\n3. Scissors\n\n")
            A = int(input("What will it be? ")) - 1
            if(A > 2 or A < 0):
                print("Please enter a number between 1 and 3\n\n")
                continue
            B = random.randrange(0,3)
            winner = (3 + A - B) % 3
            if(winner == 0):
                ties += 1
                print(f"You chose {rps_dict.get(A)}. The computer chose {rps_dict.get(B)}. You tied!\n\n")
            elif(winner == 1):
                wins += 1
                print(f"You chose {rps_dict.get(A)}. The computer chose {rps_dict.get(B)}. You win!\n\n")
            elif(winner == 2):
                losses += 1
                print(f"You chose {rps_dict.get(A)}. The computer chose {rps_dict.get(B)}. You lose!\n\n")
        except ValueError:
            print("Please enter your answer as a number between one and 3\n\n")
        else:
            print("What would you like to do?\n\n")
            choice = game_menu()
            while True:
                if(choice == 1):
                    curr_round += 1
                    break
                elif(choice == 2):
                    print(f"{name}, here are your game play statistics...\n")
                    if(losses == 0):
                        ratio = float(wins)
                    else:
                        ratio = wins/losses
                    print(f"Wins: {wins}\nLosses: {losses}\nTies: {ties}\nWin\Loss Ratio: {ratio}")
                    choice = game_menu()
                elif(choice == 3):
                    with open(f"{name}.rps", "wb") as outfile:
                        pickle.dump(f"User: {name}\n", outfile)
                        pickle.dump(f"Wins: {wins}\n", outfile)
                        pickle.dump(f"Losses: {losses}\n", outfile)
                        pickle.dump(f"Ties: {ties}\n", outfile)
                    print(f"\n{name}, your game has been saved\n")
                    return
    
    


def main():
    print("Welcome to Rock, Paper, Scissors!\n\n")
    while True:
        try:
            print("1. Start New Game\n2. Load Game\n3. Quit\n\n")
            choice = int(input("Enter Choice: "))
            if(choice != 1 and choice != 2 and choice != 3):
                print("Please enter a number 1-3\n")
                continue
        except ValueError:
            print("Please enter a number 1-3\n")
        else: 
            break
    if(choice == 1):
        newGame()
    elif(choice == 2):
        loadGame()
    elif(choice == 3):
        return


main()

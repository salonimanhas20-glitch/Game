import random
from stone import stone_paper_scissors
from dice_roll_game import dice_roll_game
def main():
    while True:
        print("\n1. Stone-Paper-Scissors\n2. Dice Roll\n3. Exit")
        choice = input("what you want to play: ")
        
        if (choice == "1"):
            stone_paper_scissors()
        elif (choice == "2"):
            dice_roll_game()
        elif (choice == "3"):
            print("Thank you for playing the game...")
            break
            
        else:
            print("Try again...")
main()
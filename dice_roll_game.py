import random

def dice_roll_game():
    print("\n--- Dice Roll Game ---")
    user = random.randint(1, 6)
    comp = random.randint(1, 6)
    
    print(f"You: {user} | Computer: {comp}")
    
    if user > comp:
        print("Result: Amazing You Won the game!")
    elif comp > user:
        print("Result: Oooo Computer Won the game!")
    else:
        print("Result: DRAWW!")
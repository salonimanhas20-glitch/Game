import random 
def stone_paper_scissors():
    options = ["stone", "paper", "scissors"]
    print("\n--- Stone, Paper, Scissors ---")
    user = input("Choose Stone, Paper, or Scissors: ").lower()
    
    if user not in options:
        print("Invalid choice!")
        return

    comp = random.choice(options)
    print(f"Computer: {comp}")

    if user == comp:
        print("Result: DRAWWW!")
    elif (user == "stone" and comp == "scissors") or \
         (user == "paper" and comp == "stone") or \
         (user == "scissors" and comp == "paper"):
        print("Result: YOU WON THE GAME!")
    else:
        print("Result: Computer Wins!!")
from ast import Continue
import random
from telnetlib import DO

gamelistoption = ["R", "P", "S"]

user_option = input('Enter a choice (R for Rock, P for paper, S for scissors):')
    
computer_option = random.choice(gamelistoption)

print(f"Player ({user_option}) : CPU ({computer_option}). \n")

while user_option not in gamelistoption:
    print("error")
    user_option = input('Enter a choice (R for Rock, P for paper, S for scissors):')
    Continue

if user_option == computer_option:
    print(f"Both players selected {user_option}. It's a tie!")
    user_option = input('Enter a choice (R for Rock, P for paper, S for scissors):')
    Continue

elif user_option == "R":
        if computer_option == "P":
            print("Computer Win!", computer_option, "covers", user_option)
        else:
            print("You win!", user_option, "smashes", computer_option)
elif user_option == "P":
        if computer_option == "S":
            print("Computer Win!", computer_option, "cut", user_option)
        else:
            print("You win!", user_option, "covers", computer_option)
elif user_option == "S":
        if computer_option == "R":
            print("Computer Win!...", computer_option, "smashes", user_option)
        else:
            print("You win!", user_option, "cut", computer_option)
        



    






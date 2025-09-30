# Write a dice rolling game program
# Write a python program that keeps asking the user if they want to roll the dice,
# It should ask them to choose a yes/no or y/n as answer
# If the user inputs 'yes' or 'y', generate 2 random dice numbers,
# If the user enters another value rather than 'yes' or 'y' or 'no' or 'n',
# tell them 'Invalid choice!' and continue the game
# If the user inputs 'no' or 'n', tell them 'Thanks for playing!', then terminate the game.


# code:

import random
while True:
    user_input = input(
        "Do you want to roll the dice? (yes/no or y/n):").lower().strip()
    if user_input == 'yes' or user_input == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled a {dice1} and a {dice2}.")
    elif user_input == 'no' or user_input == 'n':
        print("Try again next time!")
        break
    else:
        print("Invalid choice!")

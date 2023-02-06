import random
import os
from art import rock, paper, scissors, win, draw, lose, logo

# game function
def game():
    print(logo)
    game_images = [rock, paper, scissors]

    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if user_choice >= 3 or user_choice < 0: 
        print("You typed an invalid number, you lose!") 
    else:
        print(f" You Chose:\n {game_images[user_choice]}\n")

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])


        if user_choice == 0 and computer_choice == 2:
            print(win)
            should_play = input("Do you want play again?: Type 'y' or 'n'")
            if should_play == 'y':
                os.system('cls')
                game()
        elif computer_choice == 0 and user_choice == 2:
            print(lose)
            should_play = input("Do you want play again?: Type 'y' or 'n'")
            if should_play == 'y':
                os.system('cls')
                game()
        elif computer_choice > user_choice:
            print(lose)
            should_play = input("Do you want play again?: Type 'y' or 'n'")
            if should_play == 'y':
                os.system('cls')
                game()
        elif user_choice > computer_choice:
            
            print(win)
            should_play = input("Do you want play again?: Type 'y' or 'n'")
            if should_play == 'y':
                os.system('cls')
                game()
        elif computer_choice == user_choice:
            print(draw)
            should_play = input("Do you want play again?: Type 'y' or 'n'")
            if should_play == 'y':
                os.system('cls')
                game()

# game strting point
game()

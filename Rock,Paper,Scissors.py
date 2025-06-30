import random
import time

def play_game():


    while True:

        ch = input("Enter your choice (rock, paper, scissor) : ").strip().lower()

        choices = ['rock', 'paper', 'scissor']
        a = random.choice(choices)

        time.sleep(0.5)

        print("Computer's choice is: ", a)

        time.sleep(0.8)

        if a == ch:
            print("Tie")
        else:
            if a == 'rock' and ch == 'paper':
                print("You win")

            elif a == 'rock' and ch == 'scissor':
                print("Computer wins")

            if a == 'paper' and ch == 'scissor':
                print("You win")
            elif a == 'paper' and ch == 'rock':
                print("Computer wins")

            if a == 'scissor' and ch == 'rock':
                print("You win")
            elif a == 'scissor' and ch == 'paper':
                print("Computer wins")

        time.sleep(0.7)

        ask = input("Do you want to continue playing? (y/n) ")
        if ask == 'n':
            print("Ending game")
            break


play_game()
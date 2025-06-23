import random
print("Guess the random number in 10 tries (integers only!)")
while True:
    random_number = random.randint(0, 100)
    max_guesses = 10
    guess_count = 0

    while guess_count < max_guesses:
        guess_count += 1
        try:
            guess = int(input(f"Guess #{guess_count}: Enter your next guess: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")
            guess_count -= 1
            continue

        if guess == random_number:
            print("Congratulations! You guessed the random number that was generated!")
            break
        elif guess < random_number:
            print("Sorry that is incorrect, try a higher number.\n")
        else:
            print("Sorry that is incorrect, try a lower number.\n")

        if guess_count == max_guesses:
            print(f"Sorry, you have ran out of tries and you have lost! The number was {random_number}.")

    while True:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == 'y' or play_again == 'Y':
            break
        elif play_again == 'n' or play_again == 'N':
            print("\nCompleted by, Jonathan Jewell")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

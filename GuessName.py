import random

def play_game():
    # Generate a random number between 1 and 25
    number_to_guess = random.randint(1, 25)
    guess_count = 0
    guessed_correctly = False

    print("\nWelcome to the Guess the Number game!")
    print("Try to guess the number between 1 and 25.")

    # Loop until the player guesses correctly
    while not guessed_correctly:
        try:
            player_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        guess_count += 1

        # Check if the guess is too high, too low, or correct
        if player_guess < number_to_guess:
            print("Your guess is too low. Try again!")
        elif player_guess > number_to_guess:
            print("Your guess is too high. Try again!")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the correct number in {guess_count} guesses.")

def main():
    # Ask user how many games they want to play
    try:
        num_games = int(input("How many games would you like to play? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Play the number of games specified
    for game in range(num_games):
        print(f"\nGame {game + 1}:")
        play_game()

if __name__ == "__main__":
    main()

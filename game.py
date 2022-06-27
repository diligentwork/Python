import random

while True:
    user_input = input("Please enter your choice: rock or paper or scissors: ")
    possible_inputs = ["rock", "paper", "scissors"]
    computer_input = random.choice(possible_inputs)
    print("\nYour input was:", (user_input), "\ncomputer input was:", (computer_input))

    if user_input == computer_input:
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "rock":
        if computer_input == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_input == "paper":
        if computer_input == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_input == "scissors":
        if computer_input == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

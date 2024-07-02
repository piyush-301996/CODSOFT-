import random

# Initialize scores
user_score = 0
computer_score = 0

while True:
    # Prompt user for their choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue

    # Generate computer's choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    # Display result
    print(result)
    print(f"Score - You: {user_score}, Computer: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

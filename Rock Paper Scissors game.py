import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_result(user, computer, result):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if result == 'win':
        print("🎉 You win!")
    elif result == 'lose':
        print("😢 You lose!")
    else:
        print("😐 It's a tie!")

def play_game():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        user = input("Choose rock, paper, or scissors: ").lower()
        if user not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer = get_computer_choice()
        result = determine_winner(user, computer)

        display_result(user, computer, result)

        # Update scores
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer")

        # Ask to play again
        again = input("\nDo you want to play another round? (yes/no): ").lower()
        if again != 'yes':
            print("\nThanks for playing!")
            break

        round_number += 1

# Run the game
play_game()

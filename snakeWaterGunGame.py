import random

def get_user_choice():
    user_choice = input("Enter your choice (snake, water, gun): ").strip().lower()
    while user_choice not in ['snake', 'water', 'gun']:
        print("Invalid choice! Please enter snake, water, or gun.")
        user_choice = input("Enter your choice (snake, water, gun): ").strip().lower()
    return user_choice

def get_computer_choice():
    choices = ['snake', 'water', 'gun']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'snake':
        if computer_choice == 'water':
            return "You win! Snake drank water."
        else:  # computer_choice == 'gun'
            return "You lose! Gun killed snake."
    elif user_choice == 'water':
        if computer_choice == 'snake':
            return "You lose! Snake drank water."
        else:  # computer_choice == 'gun'
            return "You win! Gun got soaked in water."
    elif user_choice == 'gun':
        if computer_choice == 'snake':
            return "You win! Gun killed snake."
        else:  # computer_choice == 'water'
            return "You lose! Gun got soaked in water."

def play_game():
    print("Welcome to Snake Water Gun Game!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("Thanks for playing Snake Water Gun Game!")

# Start the game
play_game()

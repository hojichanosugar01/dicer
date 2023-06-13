import random

def roll_dice():
    # Generate a random number between 1 and 6
    return random.randint(1, 6)

def main():
    play_again = True

    while play_again:
        input("Press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"You rolled a {dice_value}!")

        play_again = input("Do you want to roll again? (y/n): ").lower() == 'y'

    print("Thanks for playing!")

# Start the program
main()

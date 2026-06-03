import random

print("🎮 Welcome to the Smart Guessing Game!")

play_again = "yes"

while play_again == "yes":

    # Difficulty selection
    print("\nChoose difficulty:")
    print("1 = Easy (1-10)")
    print("2 = Medium (1-20)")
    print("3 = Hard (1-50)")

    difficulty = input("Enter difficulty: ")

    if difficulty == "1":
        max_number = 10
        max_attempts = 5
    elif difficulty == "2":
        max_number = 20
        max_attempts = 6
    else:
        max_number = 50
        max_attempts = 8

    # Random number
    secret_number = random.randint(1, max_number)

    attempts = 0
    guess = None

    print(f"\nI picked a number between 1 and {max_number}")
    print(f"You have {max_attempts} attempts!\n")

    # Game loop
    while guess != secret_number and attempts < max_attempts:

        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print("\n🎉 Correct! You guessed the number!")
            print("Attempts used:", attempts)

        elif guess < secret_number:
            print("📉 Too low! Try higher.")

        else:
            print("📈 Too high! Try lower.")

        print("Attempts:", attempts, "/", max_attempts)
        print()

    # Lose condition
    if guess != secret_number:
        print("❌ Game Over!")
        print("The correct number was:", secret_number)

    # Replay option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

print("\n👋 Thanks for playing!")
import random

number = random.randint(1, 100)
attempts = 0

print("=== Number Guessing Game ===")

while True:
    try:
        guess = int(input("Guess a number (1-100): "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < number:
            print("Too low! Guess higher.")
        elif guess > number:
            print("Too high! Guess lower.")
        else:
            print("Correct! You won!")
            print("Attempts:", attempts)
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")

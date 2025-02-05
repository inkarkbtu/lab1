import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    attempts = 0
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1
        if guess < number:
            print("Your guess number is too low.")
        elif guess > number:
            print("Your guess number is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break
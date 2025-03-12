import random

# List of possible secret words
words = ["apple", "banana", "cherry", "grapes", "orange", "peach", "strawberry"]

# Step 1: Choose a random word
secret_word = random.choice(words)

# Step 2: Initialize dashes
dashes = "-" * len(secret_word)


# Step 3: Function to get a valid guess
def get_guess(previous_guesses):
    while True:
        guess = input("Guess: ")
        if len(guess) != 1:
            print("Your guess must have exactly one character!")
        elif not guess.islower():
            print("Your guess must be a lowercase letter!")
        elif guess in previous_guesses:
            print("You already guessed that letter!")
        else:
            return guess


# Step 4: Function to update dashes
def update_dashes(secret_word, dashes, guess):
    return "".join(guess if secret_word[i] == guess else dashes[i] for i in range(len(secret_word)))


# Step 5: Game loop
guesses_left = 10
correct_guesses = set()  # Track correct guesses
incorrect_guesses = set()  # Track incorrect guesses

while dashes != secret_word and guesses_left > 0:
    print(dashes)
    print(f"{guesses_left} incorrect guesses left.")

    guess = get_guess(correct_guesses | incorrect_guesses)  # Check both sets

    if guess in secret_word:
        print("That letter is in the word!")
        correct_guesses.add(guess)  # Add to correct guesses
        dashes = update_dashes(secret_word, dashes, guess)
    else:
        if guess not in incorrect_guesses:  # Deduct only for unique incorrect guesses
            print("That letter is not in the word.")
            incorrect_guesses.add(guess)
            guesses_left -= 1

# Step 6: Check win or lose condition
if dashes == secret_word:
    print(f"Congrats! You win. The word was: {secret_word}")
else:
    print(f"You lose. The word was: {secret_word}")
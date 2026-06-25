import random

words = ["python", "apple", "computer", "gaming", "school"]

secret_word = random.choice(words)

guessed_word = ["_"] * len(secret_word)

attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Remaining Attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

    else:
        attempts -= 1
        print("Wrong Guess!")

if "_" not in guessed_word:
    print("\nCongratulations!")
    print("You guessed the word:", secret_word)
else:
    print("\nGame Over!")
    print("The word was:", secret_word)
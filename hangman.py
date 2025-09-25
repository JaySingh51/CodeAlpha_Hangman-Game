import random

# Step 1: Define word list and choose one randomly
words = ["UMBRELLA", "COMPUTER", "TELEPHONE", "STARTPHONE"]
word = random.choice(words)

# Step 2: Initialize game variables
total_chances = 7
guessed_word = "_" * len(word)

print(" Welcome to Hangman!")
print("Guess the word letter by letter.")

# Step 3: Game loop
while total_chances != 0:
    print("\nCurrent word:", guessed_word)
    print("Remaining chances:", total_chances)

    letter = input("Guess a letter: ").upper()

    if letter in word:
        print(" Correct guess!")
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
        if guessed_word == word:
            print("\n Congratulations, you won!")
            print("The word was:", word)
            break
    else:
        total_chances -= 1
        print(" Incorrect guess.")
        print("Remaining chances:", total_chances)

# Step 4: Game over condition
if guessed_word != word:
    print("\nGame Over")
    print("You lose. All chances exhausted.")
    print("The correct word was:", word)
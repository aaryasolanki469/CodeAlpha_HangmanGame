import random

# Words and their hints
words = {
    "PYTHON": "A popular programming language",
    "GARDEN": "A place where flowers grow",
    "RAINBOW": "It appears in the sky after rain",
    "PUZZLE": "Something you solve using your brain",
    "PLANET": "Earth is one of these"
}

# Select a random word
word = random.choice(list(words.keys()))
hint = words[word]

guessed_letters = []
attempts = 6

print("\n🎮 WELCOME TO HANGMAN GAME 🎮")
print("Guess the hidden word one letter at a time!")
print("You have 6 incorrect guesses.")

print("\n💡 Hint:", hint)

while attempts > 0:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Attempts left:", attempts)

    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the correct word!")
        print("🏆 You are a Hangman champion!")
        break

    guess = input("\nEnter a letter: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one alphabet letter!")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess! Keep going!")
    else:
        attempts -= 1
        print("❌ Wrong guess! Try again!")

if attempts == 0:
    print("\n😢 GAME OVER!")
    print("The correct word was:", word)

print("\n💜 Thanks for playing Hangman!")
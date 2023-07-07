import random

def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return random.choice(words)

def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_ "
        
        print("Word:", display_word)
        print("Attempts left:", attempts)
        
        if display_word == word:
            print("Congratulations! You guessed the word correctly.")
            return
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct guess!")
        else:
            attempts -= 1
            print("Incorrect guess.")
        
        print()
    
    print("Game over! You ran out of attempts.")
    print("The word was:", word)

play_hangman()

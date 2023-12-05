import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = self.pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def pick_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess = guess.lower()  # Convert the guessed letter to lower case
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess  # Replace the corresponding "_" in word_guessed

            self.num_letters -= 1  # Reduce the variable num_letters by 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print("you have ", self.num_lives, " lives left")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

game1 = Hangman(["apples", "oranges"])
game1.ask_for_input()

    

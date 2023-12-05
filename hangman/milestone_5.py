import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = self.pick_random_word()
        self.word_guessed = ['_' if letter.isalpha() else ' ' for letter in self.word]
        self.num_letters = len(set([letter.lower() for letter in self.word if letter.isalpha()]))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def pick_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess! '{guess}' is in the word.")

            for i, letter in enumerate(self.word):
                if letter.lower() == guess:
                    self.word_guessed[i] = letter  # Replace the corresponding letter in word_guessed

            self.num_letters -= 1  # Reduce the variable num_letters by 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

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
                print("Word to guess:", ''.join(self.word_guessed))
                if self.num_letters == 0:
                    print(f"Congratulations! You guessed the word: '{self.word}'.")
                    break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost! The word was: '{game.word}'.")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You won the game!")
            break

# Example usage
play_game(["apple", "banana", "orange"])
import random
import milestone_3

def invalid_input():
    print("Invalid letter. Please, enter a single alphabetical character.")

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = self.pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        
        self.num_letters = len(set(self.word))

    def pick_random_word(self):
        return random.choice(self.word_list)
    
    def check_guess(self, guess):
        guess = str(guess).lower()
        if(guess in self.word):
            print("Good guess! ", guess, " is in the word.")
        else:
            print("Sorry, ", guess, " is not in the word. Try again.")

    def ask_for_input(self):
        while(True):
            guess = input("please guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                invalid_input()
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

              
game1 = Hangman(["apples, oranges"])
game1.ask_for_input()

    

import random
import milestone_3

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        
        self.word_guessed = ['_' for _ in self.word]
        self.word = random.choice(self.word_list)
        self.num_letters = len(set(self.word))



    

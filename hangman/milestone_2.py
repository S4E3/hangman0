import random
word_list = ["blackberry", "strawberry", "apple", "banana", "orange"]
print(word_list)
 
word = random.choice(word_list)
print(word)

guess = input("please enter a single character: ")
print(guess)
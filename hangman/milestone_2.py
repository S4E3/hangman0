import random
word_list = ["blackberry", "strawberry", "apple", "banana", "orange"]
print(word_list)
 
word = random.choice(word_list)
print(word)

guess = input("please enter a single character: ")
print("your character is ", guess)
if(len(guess) == 1):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
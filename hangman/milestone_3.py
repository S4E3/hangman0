import random
condition = True

favourite_fruit_list = ["blackberry", "strawberry", "apple", "banana", "orange"]
print(favourite_fruit_list)

random_fruit = random.choice(favourite_fruit_list)
print(random_fruit)

fruit = "apple"

while(condition == True):
    guess = input("please guess a letter: ")
    if(len(guess) == 1):
        if(guess.isalpha() == True):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    
print("while loop exited")
if(guess in fruit):
    print("Good guess! ", guess, " is in the word.")
else:
    print("Sorry, ", guess, " is not in the word. Try again.")
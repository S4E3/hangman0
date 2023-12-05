import random
condition = True

while(condition == True):
    guess = input("please guess a letter: ")
    if(len(guess) == 1):
        if(guess.isalpha() == True):
            print("this is a single alphabetical character")
            print("Good user_character_input!")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    
print("while loop exited")
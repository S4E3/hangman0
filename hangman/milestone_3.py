import random
condition = True

favourite_fruit_list = ["blackberry", "strawberry", "apple", "banana", "orange"]
print(favourite_fruit_list)

random_fruit = random.choice(favourite_fruit_list)
print(random_fruit)


def check_guess(guess):
    guess_lower = str(guess).lower()
    if(guess_lower in random_fruit):
        print("Good guess! ", guess, " is in the word.")
    else:
        print("Sorry, ", guess, " is not in the word. Try again.")
    
def ask_for_input():
    while(condition == True):
        guess = input("please guess a letter: ")
        if(len(guess) == 1):
            if(guess.isalpha() == True):
                break
            else:
                invalid_input()   
        else:
            invalid_input()
    check_guess(guess)

def invalid_input():
    print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()
 


    
    

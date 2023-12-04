import random
favourite_fruit_list = ["blackberry", "strawberry", "apple", "banana", "orange"]
print(favourite_fruit_list)
 
random_fruit = random.choice(favourite_fruit_list)
print(random_fruit)

user_character_input = input("please enter a single character: ")
print("your character is ", user_character_input)
if(len(user_character_input) == 1):
    print("Good user_character_input!")
else:
    print("Oops! That is not a valid input.")
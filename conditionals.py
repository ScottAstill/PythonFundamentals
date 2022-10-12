# conditional
# method evaluate data
# if then else

import random

# ask the user to select the upper bound
upper_bound = int(input("What is the upper bound? "))

# generate a random integer starting at 1 and going to the upper_bound
random_number = random.randint(1, upper_bound)
print(random_number)

user_guess = None
# start and loop here
while user_guess != random_number:

# ask the user to guess
    user_guess = int(input("Guess a number between 1 and " + str(upper_bound) + ": "))

# check if the user guess = the random number
    if user_guess == random_number:
        print("You win!")

# user guess is not equal to random number
    else:
        print("You lose. Try again.")
print("Game Over")




# high_range = 100
# middle_number = int(high_range/2)
# my_guess = middle_number
# number_guesses = 0
# high_or_low = "lower"
# output = "{} is {} than {}"

# my_random_number = random.randint(1, high_range)

# print()
# print("The randomly generated number is: ", my_random_number, "\n")



# # evaluate the random number and compare it to the middle number
# if my_guess < my_random_number:
#     high_or_low = "lower"

# if my_guess > my_random_number:
#     high_or_low = "higher"

# print(output.format(my_guess, high_or_low, my_random_number))

# print()
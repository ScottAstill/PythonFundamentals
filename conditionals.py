# conditional
# method evaluate data
# if then else

import random


# ask the user to select the upper bound
invalid_upper_bound = True # boolean True or False

while invalid_upper_bound:
    upper_bound = input("What is the upper bound? ")
    # check if upper bound is valid returns -> string
    if upper_bound.isdigit():
        upper_bound = int(upper_bound)
        invalid_upper_bound = False
    else:
        print("Please enter a valid input.")

# generate a random integer starting at 1 and going to the upper_bound
random_number = random.randint(1, upper_bound)
print(random_number)

user_guess = 0
number_of_guesses = 1


# start and loop here
while user_guess != random_number:


# ask the user to guess
# check if guess is a digit
    invalid_user_guess = True
    while invalid_user_guess:
        user_guess = input("Guess a number between 1 and " + str(upper_bound) + ": ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            invalid_user_guess = False

    

# check if the user guess = the random number
    if user_guess == random_number:
        print("You win!")
# exit the loop

# user guess is not equal to random number
    else:
        print("You lose. Try again.")
        number_of_guesses += 1

print("Game Over. You took " + str(number_of_guesses) + " guesses.")




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
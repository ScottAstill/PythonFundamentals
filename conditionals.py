# conditional
# method evaluate data
# if then else

import random

high_range = 100
middle_number = int(high_range/2)
my_guess = middle_number
number_guesses = 0
high_or_low = "lower"
output = "{} is {} than {}"

my_random_number = random.randint(1, high_range)

print()
print("The randomly generated number is: ", my_random_number, "\n")



# evaluate the random number and compare it to the middle number
if my_guess < my_random_number:
    high_or_low = "lower"

if my_guess > my_random_number:
    high_or_low = "higher"

print(output.format(my_guess, high_or_low, my_random_number))

print()
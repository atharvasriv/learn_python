# the input() function prompts the user to enter data into the cli
# returns the input as a string

input()

# will allow the user to enter data into the cli
# can be filled with an argument telling the usr what to fill

input("Please enter your name: ")

# this does not do anything in itself, as it just stores the value but cannot be called upon
# we can create a variable to store the input value

usr_age = input("Please input your age: ")
print(f"Your age is {usr_age}.")

# since the variable will be a string, if we want to perform arithmetic operations on it
# we first have to convert it to an int

usr_age = int(usr_age)
next_age = usr_age + 1
print(f"Next year, you will be {next_age} years old.")

# instead of doing all these extra steps, we can typecast the input itself

usr_pnumber = int(input("Please enter your phone number: "))
print(f"Your phone number is {usr_pnumber}.")
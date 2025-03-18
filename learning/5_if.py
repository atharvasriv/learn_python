# if - execute some code IF the condition is satisfied
# elif - otherwise, execute this code if this condition is met
# else - otherwise, execute this code

print("Welcome to the PAN card condition checker!")

age = int(input("Please enter your age here: "))

if age >= 21:
    print("You are eligible to apply for a PAN card")
elif age <= 0:
    print("Please enter a valid age.")
else:
    print("You are not eligible to apply for a PAN card")

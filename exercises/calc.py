operator = input(
    "Please enter the operation you want to perform (+, -, *, /): "
)

num_1 = float(input("Please enter the first number: "))
num_2 = float(input("Please enter the second number: "))

if operator == '+':
    result = num_1 + num_2
    print(
        f"The result is {round(result, 2)}"
    )
elif operator == '-':
    result = num_1 - num_2
    print(
        f"The result is {round(result, 2)}"
    )
elif operator == '*':
    result = num_1 * num_2
    print(
        f"The result is {round(result, 2)}"
    )
elif operator == '/':
    result = num_1 / num_2
    print(
        f"The result is {round(result, 2)}"
    )
else:
    print(
        "Please enter a valid operation."
    )

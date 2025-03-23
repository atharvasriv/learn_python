# while loops -> execute code WHILE some condition is true

name = input("Please enter your name: ")

while name == '':
    print("You have not entered a name.")
    name = input("Please enter your name: ")

print(f"Your name is {name}")

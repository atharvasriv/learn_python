# objectives:
# 1. username not more than 12 char
# 2. must not contain spaces
# 3. must not contain digits

username = input(
    "Please enter your username: ")

if len(username) > 12:
    print(
        "Your username can only be upto 12 characters long"
    )
elif not username.find(" ") == -1:
    print(
        "Your username cannot contain spaces."
    )
elif not username.isalpha():
    print(
        "Your username can only contain alphabets."
    )
else:
    print(
        "Username accepted."
    )

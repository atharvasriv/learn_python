# logical operators - evaluate multiple conditions
#                     or - at least one condition true
#                     and - all conditions true
#                     not - inverts the condition

temp = float(input(
    "Please enter the current temperature (in °C): "
))
is_raining = input(
    "Is it currently raining? (Y/N): "
)

if is_raining == 'Y':
    is_raining = True
elif is_raining == 'N':
    is_raining = False

if is_raining or temp > 30 or temp < 10:
    print(
        "It is advisable to cancel the event."
    )
else:
    print(
        "The event can be held."
    )

if temp < 20 and is_raining:
    print(
        "It is expected to be very cold today."
    )
else:
    print(
        "It is not expected to be very cold today."
    )

if 35 >= temp >= 25 and not is_raining:
    print(
        "It is a good day to go outside."
    )

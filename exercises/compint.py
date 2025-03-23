principle = 0
rate = 0
time = 0
number_of_compounds = 0

while principle <= 0:
    principle = float(input("Please enter the principle: "))
    if principle <= 0:
        print("The principle cannot be negative or equal to zero.")

while rate <= 0:
    rate = float(input("Please enter the rate of interest: "))
    if rate <= 0:
        print("The rate cannot be less than or equal to zero.")

while time <= 0:
    time = int(input("Please enter the time in years: "))
    if time <= 0:
        print("The time cannot be less than or equal to zero.")

while number_of_compounds <= 0:
    number_of_compounds = int(input(
        "Please enter the number of times the amount should get compounded: "))
    if number_of_compounds <= 0:
        print(
            "The number of coumpounds cannot be less than or equal to zero."
        )

total = (principle
         * pow((1 + rate/number_of_compounds), number_of_compounds*time))

print(
    f"The total amount after {time} year(s) with {number_of_compounds} compoun\
d(s) per year will be: {total:.2f}"
)

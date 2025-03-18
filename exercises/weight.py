weight = float(input(
    "Please enter your weight (numerical): "
))

unit = input(
    "Please enter the units (kg, lbs): "
)

if unit == 'kg':
    result = weight * 2.205
    print(
        f"Your weight in lbs is {round(result, 2)}lbs"
    )
elif unit == 'lbs':
    result = weight / 2.205
    print(
        f"Your weight in kg is {round(result, 2)}kg"
    )
else:
    print(
        "Please enter a valid unit."
    )

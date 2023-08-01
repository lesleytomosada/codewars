# DESCRIPTION:
# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"


def bmi(weight, height):
    body_mass_index = weight / height**2
    if body_mass_index > 30:
        return "Obese"
    elif body_mass_index > 25:
        return "Overweight"
    elif body_mass_index > 18.5:
        return "Normal"
    else:
        return "Underweight"

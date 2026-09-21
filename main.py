#reads user height and weight,calculates BMI and prints the result with BMI category
#using imperial units (pounds and inches) to calculate BMI
weight_MIN = 95
weight_MAX = 350


weight = input("enter your weight in pounds(lb): ")

#validating weight input
try:
    weight = float(weight)
    if weight < weight_MIN or weight > weight_MAX:
        print(f" {weight} is out of range, Please make sure to enter weight in lbs between {weight_MIN} and {weight_MAX} pounds.")
        raise SystemExit(1)
except ValueError:
    print("Invalid weight input, Please enter a valid number.")
    raise SystemExit(1)


height_feet = input("enter your height(feet part only):")

#validating height input in feet
try:
    height_feet = float(height_feet)

    if height_feet.is_integer():
        height_feet = int(height_feet)
    else:
        print("please enter height in feet as a whole number, for example 5 or 6.")
        raise SystemExit(1)
    
    if height_feet < 3 or height_feet >= 7:
        print(f" {height_feet} is out of range, Please make sure entered height is in feet.")
        raise SystemExit(1)
    
except ValueError:
    print("Invalid height input, Please enter a valid number")
    raise SystemExit(1)


height_inches = input("enter your height (inches part only): ")

#validating height input in inches
try:
    height_inches = float(height_inches)
    if height_inches < 0 or height_inches >= 12:
        print(f" {height_inches} is out of range, Please make sure entered height is in inches.")
        raise SystemExit(1)
except ValueError:
    print("Invalid height input, Please enter a valid number.")
    raise SystemExit(1)


# converting user height into inches
height_total_inches = (height_feet * 12) + height_inches

#calculate BMI
bmi = (weight / (height_total_inches ** 2)) * 703

#determine weight category based on BMI value

if bmi <18.5:
    category = "Underweight"
elif bmi >= 18.5 and bmi < 25.0:
    category = "Normal weight"
elif bmi >= 25.0 and bmi < 30.0:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is {bmi:.2f}, which is categorized as {category}.")
#Taking input from user; weight in lb and height in feet and inches
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


height_feet = input("enter your height in feet(ft): ")
#validating height input in feet
try:
    height_feet = int(height_feet)
    if height_feet < 3 or height_feet >= 7:
        print(f" {height_feet} is out of range, Please make sure entered height is in feet.")
        raise SystemExit(1)
except ValueError:
    print("Invalid height input, Please enter a valid number")
    raise SystemExit(1)

height_inches = input("enter your height in inches(in): ")
#validating height input in inches
try:
    height_inches = float(height_inches)
    if height_inches < 0 or height_inches >= 12:
        print(f" {height_inches} is out of range, Please make sure entered height is in inches.")
        raise SystemExit(1)
except ValueError:
    print("Invalid height input, Please enter a valid number.")
    raise SystemExit(1)









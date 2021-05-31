## BMI Calculator

# Instructions

# Write a program that calculates the Body Mass Index (BMI) from a 
#  user's weight and height.

# The BMI is a measuring of some's weight taking into account their
#  height. e.g. If a tall person and a short person both weight the same 
#  amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square
#  of their height(in m):

#  BMI = Weight(kg) / Height^2(m^2)

# Example Input

# weight => 80
# height => 1.75

# Example Output

# 80/1.75*1.75 = 26.12 

Weight = float(input("Enter your Weight in kg: "))
Height = float(input("Enter your Height in m: "))

BMI = round(Weight/Height**2, 2)

print(f"Your BMI Index value is: {BMI}")
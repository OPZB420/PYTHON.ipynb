#BMI Calculator 2.0

#Instructions

#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

#It should tell them the interpretation of their BMI based on the BMI value.

#* Under 18.5 they are underweight.
#* Over 18.5 but below 25 they have a normal weight.
#* Over 25 but below 30 they are overweight.
#* Over 30 but below 35 they are obese.
#* Above 35 they are clinically obese.

#=> The BMI is calculated by dividing a person's weight (in kg) by the square of their height(in m).

#=>> BMI = Weight(kg)/Height^2(m^2)



print("Welcome to **! BMI Calculator 2.0 !**")

weight = float(input("Enter your Weight in kg : "))
height = float(input("Enter your Height in m : "))

bmi = round(weight / height**2, 2)


if bmi < 18.5:
  print(f"Your BMI is: {bmi}, you are Under Weight! ")
elif bmi <= 25:
  print(f"Your BMI is: {bmi}, you are Normal Weight! ")
elif bmi <=30:
  print(f"Your BMI is: {bmi}, you are Over Weight! ")
elif bmi <= 35:
  print(f"Your BMI is: {bmi}, you are Obese")
else:
  print(f"Your BMI is: {bmi}, you are Clinically obese")

print("**************************************************")


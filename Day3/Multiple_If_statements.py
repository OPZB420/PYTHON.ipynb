# Multiple If Statements 

# Make a Game ticket counter code
# * Check height min 120 cm
# * Ask age ,Prices like 0 -12 => $5, 12 - 18 => $7, 18 + => $12
# * Ask if they want photo taken if yes then add +$3 in the total bill.
# * Print total bill.

print("Welcome to the game !")

height = int(input("Please Enter your height in cm: "))
bill = 0

if height > 120:
  print("You can paly game !")
  age = int(input("What is your age: "))
  if age < 12:
    bill = 5
    print("Pay $5 ")
  elif age<=18:
    bill = 7
    print("Pay $7")
  elif age>18:
    bill = 12
    print("Pay $12")
  
  want_photo = input("Want photo taken for yes 'Y' for no 'N': ")
  if want_photo == "Y":
    bill += 3
  print(f"Your total bill is: {bill}")
else:
  print("Sorry, You can't paly game, Try next time !")
  
print("Thanks for comming !")
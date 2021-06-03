

print("Welcome to the Game !")

height = int(input("Enter you height in cm : "))

if height >= 120:
  print("You can play Game!")
  age = int(input("What is your age? : "))
  if age < 12:
    print("You pay $5.")
  elif age<=18:
    print("Yu pay $7.")
  else:
    print("You pay $12.")
else:
  print("You cant play game until your height match!")
  

### Password Generator

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
           'w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['1','2','3','4','5','6','7','8','9']

symbols = ['!',',','#','$','%','^','&','*','(',')']

print("Welcome to Python Password Generator !\n")

nr_letters = int(input("How many letters would you like in your Password?: "))

nr_numbers = int(input("How many numbers would you like in your Password?: "))

nr_symbols = int(input("How many symbols would you like in your Password?: "))

## Password is a variable that store all the data
#  Easy way to do that

Password = ""

### For taking random letters

for char in range(1, nr_letters + 1):
  Password += random.choice(letters)

for char in range(1, nr_numbers + 1):
  Password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
  Password += random.choice(symbols)
  
# print(Password)

## Hard way to do that

Password_list = []


for char in range(1, nr_letters + 1):
  Password_list += random.choice(letters)

for char in range(1, nr_numbers + 1):
  Password_list += random.choice(numbers)

for char in range(1, nr_symbols + 1):
  Password_list += random.choice(symbols)
  
  
# print(Password_list)

random.shuffle(Password_list)

# print(Password_list)

## Take password output in strings
pass_str = ""
for i in Password_list:
  pass_str += i
  
print(f"Your Password is: {pass_str}")
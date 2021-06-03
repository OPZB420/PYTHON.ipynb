## Day3 Exercise 1

##  Odd or Even

#  Instructions

# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# e.g. 86 is even because 86 / 2 = 43
# 43 does not have any decimal places. Therefore the division is clean.
# e.g. 59 is odd because 59 / 2 = 36.875
# 36.875 is not a whole number, it has decimal places, Therefore there is a remainder of 0.875,
#  so the division is not clean.
# The modulo is written as a percentage sign(%) in python. It gives you the remainder after a division.

# e.g.
# 6 / 2 = 3 with no  remainder.

# 5 / 2 = 2*2+1 , remainder is 1.
# 14 / 4 = 3*4+2, remainder is 2.

number = int(input("Enter any number : "))

if number%2 == 0:
  print(f"Number {number} is an even number !")
else:
  print(f"Number {number} is an odd number !")
  
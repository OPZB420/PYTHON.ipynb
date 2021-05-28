### Day 2 Exercise 1
# Instructions

# Write a program that adds the digits in a 2 digit number. e.g. if the 
#  input was 35, then the output should be 3 + 5 = 8

# Type two digit number: ?
# Input => 35
#Output => 3+5 = 8

two_digit_num = input("Enter two digit number: ")

first_digit = two_digit_num[0]
second_digit = two_digit_num[1]

result = int(first_digit) + int(second_digit)

print(f"Output => {first_digit} + {second_digit} = {result}")


# Who's Paying

# Instructions

# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string name_string into indivisual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name,name,name


#####     Example Input

# Angela, Ben, Jenny, Michale, Chloe

# Note: Notice that there is a space between the command the next name.

######   Example Output

# Michael is going to buy the meal today!

##############################################################################


import random

print("Welcome to Random Bill Seprater code!\n")
## take name input from user.

name_str = input("Enter the names of all persons using Comma to seprate: ")
print("")

## Seprate the names and store in a list using split function

name = name_str.split(",")

# print(name_str)
## To use random function we need to find the length of total names in the list
## for that we need to use len - 1 function

x = len(name) -1

## now we need to use random function to find a random number from the list.

ran_name = random.randint(0,x)

print(f"*=> {name[ran_name]} is going to buy the meal today! <=*")


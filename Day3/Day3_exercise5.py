#### ___________ Love Calculator 

## Instructions

# You are going to write a program that tests the compatibility between two
# people. We're going to use the super scientific method recommended by BuzzFed.
# To work out the love score between two people :

## * Take both peoples name and check the number of times the letters in the word TRUE occurs.
#     Then check for the number of times the letters in the word LOVE occurs.
#     then combine these numbers to make a 2 digit numbers.

##=> For Love score less than 10 or greater than 90, the message should be:

## *> Your Score is X, You go together like coke and mentos.

##=> For Love scores between 40 and 50, the message should be:

## *> Your score is Y, You are alright together.


##=> Otherwise, the message will just their score, e.g.:
## *> Your score is Z.

#$### e.g.:

## name_1 = "Angela Yu"
## name_2 = "Jack Bauer"

## TRUE

#> T - occurs 0 times
#> R - occurs 1 times
#> U - occurs 2 times
#> E - occurs 2 times

## Total = 5

## LOVE

#> L - occurs 1 times
#> O - occurs 0 times
#> V - occurs 0 times
#> E - occurs 2 times

## Total = 3

#.> Love Score = 53
## print = "Your score is 53"



print("!****** Welcome to Love Calculator ******!")
print("")
name_1 = input("What's your name: ")
name_2 = input("What's their name: ")

add_name = name_1.lower() + name_2.lower()

t = add_name.count("t")
r = add_name.count("r")
u = add_name.count("u")
e = add_name.count("e")

true = t + r + u + e

l = add_name.count("l")
o = add_name.count("o")
v = add_name.count("v")
e = add_name.count("e")

love = l + o + v + e

true_love = str(true) + str(love)

print(true_love)
print(type(true_love))
## Score 

if int(true_love) <= 10 or int(true_love) >= 90 :
  print(f"Your Score is : {true_love}, You go together like coke and mentos.")
elif int(true_love) >= 40 and int(true_love) <= 50:
  print(f"Your score is: {true_love}, You are alright together")
else:
  print(f"You score is: {true_love} !")
  





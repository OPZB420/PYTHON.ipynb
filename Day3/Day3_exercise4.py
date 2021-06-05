## Pizza Order

#  Instructions

# Congratulations, you've got a job at Python pizza. Your first job is  to build an automatic pizza
# order program.

# Based on a user's order, work out their final bill.

##  * Small Pizza : $15
##  * Medium Pizza : $20
##  * Large Pizza  : $25

## * Pepperoni for small pizza : +$2
## * Pepperoni for Medium Pizza or Large Pizza : +$3
## * Extra Cheese for any size Pizza : +$1




print("*******! Welcome to Python Pizza !******")
print("What would you like to eat?____")

pizza = input("Please Enter S for small pizza, M for Medium pizza and L for Large pizza: ")
bill = 0

## If user select Small size pizza

if pizza == "S":
  bill = 15
  ## Ask for pepperoni
  pepperoni_s = input("Would you like to add Pepperoni $2 for your small pizza if yes= Y, no = N: ")
  if pepperoni_s =="Y":
    bill +=2
  ## Ask user for Extra Cheese
  cheese = input("Would you like to add Extra Cheese $1 with your pizz, for yes= Y , no = N: ")
  if cheese == "Y":
    bill +=1
    
  print(f"Your Total bill is : ${bill}")
    
## If user select Medium Size Pizza
    
elif pizza == "M":
  bill = 20
    ## Ask for pepperoni
  pepperoni_ml = input("Would you like to add Pepperoni $3 for your Medium or Large pizza if yes= Y, no = N: ")
  if pepperoni_ml =="Y":
    bill +=3
    ## Ask user for Extra Cheese
  cheese = input("Would you like to add Extra Cheese $1 with your pizz, for yes= Y , no = N: ")
  if cheese == "Y":
    bill +=1
    
  print(f"Your Total bill is : ${bill}")
    
## If user select Large Size Pizza

elif pizza == "L":
  bill = 25
  ## Ask for pepperoni
  pepperoni_ml = input("Would you like to add Pepperoni $3 for your Medium or Large pizza if yes= Y, no = N: ")
  if pepperoni_ml =="Y":
    bill +=3

## Ask user for Extra Cheese
  cheese = input("Would you like to add Extra Cheese $1 with your pizz, for yes= Y , no = N: ")
  if cheese == "Y":
    bill +=1
 
  print(f"Your Total bill is : ${bill}")
  
else:
  print("Please Enter right size!")


print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")





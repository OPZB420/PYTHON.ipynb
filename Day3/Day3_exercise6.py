### --------------  Treasure Island ----------

# Your mission to find the treasure.

## *> You're at a cross road. Where do you want to go? Type "left" or "right" 
## ---
##  |-> right => Game Over
##  |
##  |-> left => You come to a lake. There is an island in the middle of the lake. Type "wait" to wait 
##       |       for a boat. Type "swim" to swim a cross
##       |
##       |-> swim => Game Over
##       |
##       |-> wait => You arrive at the island unharmed. There is a house with 3 doors, One Red
##             |      , One Yellow and One Blue. Which colour do you choose?
##             |
##             |-> Red => Game Over
##             |
##             |-> Yellow => You win!
##             |
##             |-> Blue => Game Over


print("************! Welcome to Treasure Island !*************")
print("")
print("Your Mission to find the Treasure !")


direction = input('You`re at a cross road. Where do you want to go? Type "left" or "right": ').lower()


if direction == "left":
  options = input("You come to a lake. There is an island in the middle of the lake.Type 'Wait' to wait for a boat. Type 'Swim' to swim a cross: ").lower()

  if options == "wait":
    doors = input('You arrive at the island unharmed. There is a house with 3 doors, One Red One Yellow and One Blue. Which colour do you choose?: ').lower()
   
    if doors == "yellow":
      print("You Win! ***")
   
    else:
      print("Game Over")  
  
  else:
    print("Game Over!")    

else:
  print("Game Over")
### Rock Paper Scissors
import random

rock = '''
    
    ____________
---'      ______)
          (______)
          (______)
          (_____)
----,____(____)

'''

paper = '''

     ________
____'    ____)___
           ______)
          ________)
         ________)
----,__________)

'''

scissors = '''

     ______
----'  ____)___
          _____)
        ________)
        (____)
---,_____(__)

'''
## Create a Game images list
game_img = [rock,paper,scissors]

print("     Welcome to Rock Paper Scissors Game!\n")

## Ask for user input
user_choice = int(input("What you want to chose 0 for Rock, 1 for Paper and 2 for Scissors: "))

## Computer Input
computer_choice = random.randint(0,2)

## User Choice 

if user_choice >= 3 or user_choice < 0:
  print("\n"+f"It's Invalid number: {user_choice}, please chose a number b/w 0 to 2.")
else:
  print("\n"+"User chose "+str(user_choice)+"\n"+game_img[user_choice])


## Computer Choice

print(f"Computer Chose {computer_choice}")
print(game_img[computer_choice])

## Function define for the game 

if user_choice >= 3 or user_choice< 0:
  print("You chose Invalid Number!")
elif user_choice==0 and computer_choice ==2:
  print("You Wins!")
elif computer_choice == 0 and user_choice == 2:
  print("Computer Wins!")
elif computer_choice > user_choice:
  print("Computer Wins!")
elif user_choice> computer_choice:
  print("You wins!")
elif computer_choice == user_choice:
  print("It's a Draw!")
else:
  print("Not Working")
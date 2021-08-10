# Treasure Map

# Instructions 

# You are going to write a program which will make a spot with an X.

# The map is made of 3 rows of blank squares.

# ["*","*","*"]
# ["*","*","*"]
# ["*","*","*"]

# Your program should allow you to enter the position of the treasure using a two-digit system. 
# The first digit is the horizontal column number and second digit is the vertical row number e.g.:

# Example Input 

# column 2, row 3 would be entered as:
# 23

# Example OutPut
# ["*","*","*"]
# ["*","*","*"]
# ["*","X","*"]

#############################################

row1 = ["*","*","*"]
row2 = ["*","*","*"]
row3 = ["*","*","*"]

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put your Treasure: ")

horizontal = (int(position[0]) - 1)

vertical = (int(position[1]) - 1)

selected_row= map[vertical]
selected_row[horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}")
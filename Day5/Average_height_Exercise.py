##       Average Height

# Instructions

# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

# e.g.
# 180+124+165+173+189+169+146 = 1146

# There are a total of 7 heights in student_heights 1146/7 = 163.71
# Average height rounded to the nearest whole number = 164

# Example Input

# 156 178 165 171 187

# Example Output

# 171

## Take user input 

student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(student_heights'\n')

### Add all the students heights using for loop 

total_height = 0

for height in student_heights:
  total_height += height
  
print(f"Sum of all students heights {total_height}""\n") 

### find the total number of students using for loop

num_of_student = 0

for student in student_heights:
  num_of_student += 1
  
print(f"Total number of student: {num_of_student}"'\n')

### Average height 

average_height = round(total_height / num_of_student)

print(f"Average Height is: {average_height}")
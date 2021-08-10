###                     Highest Scores 

# Instructions 

# You are going to write a program that calculates the heighest score form a List of Score.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. The output words must match the example. i.e.

# The highest score in the class is: X

# Example input

# 78 65 89 86 55 91 64 89

# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

# Example Output

# The highest score in the class is: 91


####### Take input from the user 

student_scores = input("Enter the scores of students: ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  
print(student_scores)

#### Find the highest score without using max function.

highest_score = 0

for score in student_scores:
  if score > highest_score:
    highest_score = score
print(highest_score)
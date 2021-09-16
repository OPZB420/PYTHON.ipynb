## Grading Program Project

## Instructions

# You have access to a database of student_scores in the formate of a dictionary.
# The keys in student_scores are the names of the students and the values are their
#  exam scores.

# Write a program that converts their scores to grades. By the end of your program, 
#  you should have a new dictionary called student_grades that should 
#  contain student names for keys and their grades for values.
#  The final version of the student_grades dictionary will be checked.

## This is the scoring criteria.
    # Scores 91 - 100 : Grade = "Outstanding"
    # Scores 81 - 90 : Grade = "Exceeds Expectation"
    # Score 71 - 80 : Grade = "Accetable"
    # Score 70 or lower : Grade = "Fail"

student_scores = {
    "Harry": 81,
    "Ron": 78, 
    "Hermon": 99,
    "Draco": 74,
    "Neville": 62,
 }

#TODO -1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO -2: Write your code below to add the grades to student_grades

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70:
        student_grades[student] = "Accetable"
    else:
        student_grades[student] = "Fail"
        

#Don't change the code below
print(student_grades)
## Your Life in Weeks

# I was reading this article by Tim Urban - Your Life in Weeks and realized.
#  just how little time we actually have.

# Create a program using maths and f-Strings that tells us how many days,
#  Weeks, Months we have left if we live until 90 years old.

# It Will take your current age as the input and output a message with our 
#  time left in this format:

#  => You have x Days, y Weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning => Your output should match the example output format exactly,
#             even the positions of the commas and full stops.

## Example Input

# What is your current age? => 56

# OUTPUT

# You have 12410 days, 1768 weeks, and 408 months left.



# year = 90
# weeks = 90*52
# days = weeks*7

user = int(input("Enter your age?: "))

user_year = 90 - user
user_weeks = user_year*52
user_days = user_weeks * 7
user_month = user_year * 12
print(f"You have {user_days} Days, {user_weeks} Weeks and {user_month} Months left.")
# print(user_year, user_weeks, user_days, user_month)
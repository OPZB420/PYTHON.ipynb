# This is a Difficult Challenge

# Instructions

# Write a program that works out whether if a given year is a leap year. A normal year has 365
# days, leap year have 366, with an extra day in February. The reason why we have leap year is 
# really fascinating.

# This is how you work out whether if a particular year is a leap year.

# On every year that is evenly divisible by 4
#   Except every year that is evenly divisible by 100
#    Unless the year is also evenly divisible by 400

# e.g. The year 2000:
# 2000/4 = 500(leap)
# 2000/100 = 20 (Not leap)
# 2000/400 = 5(leap!)

# So the year 2000 is a leap year.

# But the year 2100 is not leap year because:
# 2100 / 4 = 525(leap)
# 2100 / 100 = (Not leap)
# 2100 / 400 = 5.25(Not leap)  



year = int(input("Enter the year which you want to check as a leap year : "))

if year % 4 == 0:
  if year % 100 ==0:
    if year % 400 ==0:
      print("Leap year")
  else:
    print("Leap year")
else:
  print("Not Leap year")
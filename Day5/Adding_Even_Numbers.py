##### Adding Even Numbers 


# Instruction 

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 1 to 100.

# e.g. 2 + 4 + 6 + 8 + 10 ....+ 98 + 100

# Important, there should only be 1 print statement in your console output.
#  It should just print the final total and not every step of the calculation.

### Add even  numbers between 1 to 100

total = 0 
for n in range(2,101,2):
  total += n
  
print(total)

################# Second way to use the code.

total2 = 0
for n in range(1,101):
  if n % 2 == 0:
    total2 += n

print(total2)

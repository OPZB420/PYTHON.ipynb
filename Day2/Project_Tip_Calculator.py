### Tip Calculator

# If a $150 bill then add 12% tip and Split bill in 5 .

total_bill = float(input("Enter the bill amount $"))

tip_amount = int(input("What percentage of tip would you like to give? 10, 12 or 15 ?: "))

after_tip = (tip_amount/100)*total_bill
             
split_bill = int(input("How many people to split the bill?: "))

final_bill = round((total_bill + after_tip)/split_bill,2)
print(f"Each person should have pay: ${final_bill}")


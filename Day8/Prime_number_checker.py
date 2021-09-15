## prime number checker function

def prime_checker(number):
    is_prime = True
    for i in range(2,number-1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a Prime number.")
    else:
        print("It's not a prime number.")
    


n = int(input("Enter the number you want to check: "))
prime_checker(number=n)
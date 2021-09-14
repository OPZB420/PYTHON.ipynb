## function with more than one input data 
## but it's positional function 
# if we change the inputs of variables it's hole function change
# Like (name,location) if i put (azamgarh, Siddhartha)
#then it's going to change the hole function


def greet_with(name,location):
    print(f"My name is {name}, I am from {location}.")
    
    
greet_with("Azamgarh","Siddhartha")
print("")

## Function with keyword Arguments 
# It's like (a,b) = (b=2,a=1) = a =1, b = 2

def greet_with_key(name,age,location):
    print(f"Hello!")
    print(f"My name is {name}, I am {age} year's old.")
    print(f"I am from {location}.")
          
greet_with_key(age=20,location="India",name="Siddhartha")
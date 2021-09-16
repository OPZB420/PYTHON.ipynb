## Dictionary in Python

##  dictionary{key:value}


programming_dictionary = {
    "Bug": "An error in a program that prevent the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing somthing over and over again.",
}

## Retriving items from dictionary

# print(programming_dictionary["Bug"])

## Adding new items to dictionary.

programming_dictionary["new"] = "This is a new item adding in dictionary."

# print(programming_dictionary)

## Creating a empty dictionary 

empty_dictionary = {}

## Wipe a exesting dictionary.

# programming_dictionary= {}
# print(programming_dictionary) 

## Edit an item in dictionary

# print(programming_dictionary["Bug"]+"\n")

programming_dictionary["Bug"] = "Editing the item in this value."

# print(programming_dictionary["Bug"])

## Loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]+"\n")
## Multi return function values

# return -: Means end of function


def formate_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "Please Enter your name"# Here return used because if user did't input its f_name or l_ name then function stops here.
    formate_f_name = f_name.title()
    formate_l_name = l_name.title()
    
    return f"{formate_f_name} {formate_l_name}"

    
print(formate_name(input("Enter Your first name :\n"),input("Enter your last name: \n")))

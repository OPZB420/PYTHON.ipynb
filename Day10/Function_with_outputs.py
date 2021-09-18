# Function With Outputs 

def formate_name(f_name,l_name):
    formate_f_name = f_name.title()
    formate_l_name = l_name.title()
    
    return f"{formate_f_name} {formate_l_name}"

formated_string= formate_name("SiddharTha","SINGH")
    
print(formated_string)
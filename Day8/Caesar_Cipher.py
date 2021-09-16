alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Define a new function insted of more than one function.

def cipher(c_text,c_shift,c_direction):
    end_text = ""
    if c_direction == "decode":
        c_shift *= -1
        
    for char in c_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + c_shift
            end_text += alphabet[new_position]
        else:
            end_text += char
        #TODO -1:> What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded
        #e.g. start_text = "meet me at 3"
        #end_text = "....... ... ... 3"
        
    print(f"The {c_direction}d message is {end_text}.")



#TODO -:> Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes then ask them for the direction/text/shift again and call the caesar() function 
# again?
# Hint: Try creating a new function that calls itself if they type 'yes'.
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode'to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ##todo- if user input shift number grater than 26.
    shift = shift % 26

    cipher(c_direction=direction,c_shift=shift,c_text=text)
    
    result = input("Type 'yes' for continue or 'no' to end. \n")
    
    if result == 'no':
        should_continue = False
        print("Good Bye!")












##################################################################################################
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def encrypt(plain_text,shift_num):
#     cipher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_num
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
    # print(f"The encoded message is {cipher_text}")


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 



#TODO -1:> Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# def decrypt(cipher_text, d_shift):
#     d_text = ''
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - d_shift
#         d_text += alphabet[new_position]
        
    # print(f"The decoded text is {d_text} ")
    

        #TODO -2:> Inside the 'decrypt' function, shift each letter of the 'text' *backword* in the alphabet by the shift
                #  amount and print the decrypted text.
        #e.g.
        #cipher_text = "mjqqt"
        #shift = 5
        #plain_text = "hello"
        #print_output: "The decoded text is hello"

#TODO -3:> Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.  Then 
        #   call the correct function based on that 'direction' variable. You should be able to test the code to 
        #   encrypt *and* decrypt a message.

# if direction == "encode":
#     encrypt(plain_text=text,shift_num=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text,d_shift=shift)
import random
import string 

UPPERCASE =  string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBER = string.digits
SPECIAL_CHARACTER = string.punctuation

print ("""----------------------------
PASSWORD GENERATOR
----------------------------""")

def generate_password(number):
    password_list = [random.choice(UPPERCASE),
    random.choice(LOWERCASE), random.choice(NUMBER), random.choice(SPECIAL_CHARACTER)]
    ALL_CHARACTER = NUMBER + UPPERCASE + NUMBER + LOWERCASE + NUMBER + SPECIAL_CHARACTER + NUMBER
    password_list += random.choices(ALL_CHARACTER, k=(number-4))
    random.shuffle(password_list)
    return ("".join(password_list))

while True:
    try:
        User_Password_len = int(input("How many characters would you like in your password: "))
        if User_Password_len < 4:
            print ("Password length must be atleast 4 characters.\n")
        else:
            password = generate_password(User_Password_len)
            print (f"Your generated password is: {password}\n")
    except:
        print ("Please Enter a valid Integer.\n")
    
    again_input = input("Woulf you like to generate another password? (y/n): ")
    if again_input != 'y':
        break    

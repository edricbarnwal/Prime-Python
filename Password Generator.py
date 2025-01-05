import random
import string 

ALPHABET =  (string.ascii_letters)
NUMBER = (string.digits)
SPECIAL_CHARACTER = (string.punctuation)

User_Password_len = int(input("How many characters do you want in a password: "))
Special_Character = input("Do you need a special character: ")

def generate_password(number):
    New_List = ALPHABET + NUMBER
    random_num = []
    for x in range(number):
        newl = random.choice(New_List)
        random_num.append(newl)
        
    print (random_num)
        
        
generate_password(User_Password_len)       
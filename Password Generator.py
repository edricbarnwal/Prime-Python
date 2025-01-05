import random
import string 

ALPHABET =  (string.ascii_letters)
NUMBER = (string.digits)
SPECIAL_CHARACTER = (string.punctuation)

User_Password_len = int(input("How many characters do you want in a password: ))
Special_Character = input("Do you need a special character: ")

def generate_password(number):

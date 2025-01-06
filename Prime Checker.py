print ("""--------------------
PRIME CHECKER
--------------------
""")

def prime_checker(num):
    if num < 2:
        return False
    for x in range(2, int(num*0.5)+1):
        if num % x == 0:
            return False
    return True
    
while True:
    try:
        user_input_number = int(input("Enter a number: "))
        if prime_checker(user_input_number):
            print (f"Number {user_input_number} is a Prime Number.\n")
        else:
            print (f"Number {user_input_number} is not a Prime Number.\n")
        check_again = input("Would you like to check again(y/n): ")
        if check_again != 'y':
            print ("Thanks for using.")
            break
    except:
        print ("Please Enter a valid Integer.\n")

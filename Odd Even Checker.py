print ("""--------------------
Odd Even Checker
--------------------
""")

def check_odd_even(Number):
    if Number % 2 == 0:
        return (f"Number {Number} is Even Number.\n")
    else:
        return (f"Number {Number} is Odd Number.\n")

while True:
    try:
        Number = int(input("Enter a integer: "))
        print (check_odd_even(Number))
        check_again = input("Would you like to check again (y/n): ")
        if check_again != 'y':
            break
    except ValueError:
        print ("!Enter a valid Integer!\n")

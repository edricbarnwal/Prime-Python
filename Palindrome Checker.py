def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

def palindrome_checker():
    user_input = input("Enter a value to check if it's a palindrome: ")

    if is_palindrome(user_input):
        print(f"Yes, '{user_input}' is a palindrome.")
    else:
        print(f"No, '{user_input}' is not a palindrome.")

print ("""--------------------
 PALINDROME CHECKER
--------------------""")

while True:
    palindrome_checker()
    again_input = input("\nDo you want to check again (y/n): ")
    if again_input != 'y':
        print ("Thank You for using.")
        break

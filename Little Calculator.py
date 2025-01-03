add = lambda x, y: x+y
    
subtraction = lambda x, y: x-y
    
multiply = lambda x, y : x*y

divide = lambda x, y: x/y
    
print ("***Little Calculator***")

def mini_calculator():
    try:
        num1 = float(input("Enter your first number : "))
        num2 = float(input("Enter your second number : "))
        operation = input("Enter operation : '+', '-'. '*', '/' : ")
                
        if operation == "+":
            print(add(num1, num2))
                
        elif operation == "-":
            print(subtraction(num1, num2))
                
        elif operation == "*":
            print(multiply(num1, num2))
                
        elif operation == "/":
            if num2 == 0:
                print ("Error: Division by Zero is Not Allowed")
            else:
                print(divide(num1, num2))
        else:
            print ("Enter a valid operation")
        
    except:
        print ("Please enter a valid number.")
        mini_calculator()
        
while True:
    mini_calculator()
    again = input("Do you want to calculate again (y/n) : ").lower()
    if again != 'y':
        print ("Thanks you for using the calculator.")
        break

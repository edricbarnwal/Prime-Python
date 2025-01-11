print ("""--------------------
BMI CALCULATOR
--------------------
""")

def BMI_Calculator():
    User_Weight = float(input("Enter your Weight in Kg: "))
    User_Height = float(input("Enter your Weight in Metere: "))
    BMI = round(User_Weight/(User_Height**2), 2)
    BMI_Range(BMI)
    
def BMI_Range(User_BMI):
    if User_BMI < 18.5:
        print(f"BMI is {User_BMI}: Underweight. You need to gain weight.\n")
    elif User_BMI < 24.9:
        print(f"BMI is {User_BMI}: Normal weight. Keep maintaining your healthy lifestyle.\n")
    elif User_BMI < 29.9:
        print(f"BMI is {User_BMI}: Overweight. Consider adopting a healthier lifestyle.\n")
    elif User_BMI < 34.9:
        print(f"BMI is {User_BMI}: Obesity (Class I). Seek guidance to manage your weight.\n")
    elif User_BMI < 39.9:
        print(f"BMI is {User_BMI}: Obesity (Class II). Take action to improve your health.\n")
    else:
        print(f"BMI is {User_BMI}: Obesity (Class III). Immediate medical intervention is recommended.\n")

while True:
    try:
        BMI_Calculator()
    except:
        print (f"Please enter a valid input in numbers.\n")
        BMI_Calculator()

    check_again = input("Do you want to check again (y/n): ").lower()
    if check_again != 'y':
        print ("Thank You for using the BMI Calculator.")
        break

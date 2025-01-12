print("""-------------------
UNIT CONVERTER
-------------------
""")

def Unit_Converter():

    def Length():
        try:
            meters = float(input("Enter a value in meters "))
            print (f"{meters} meters is equl to:")
            print (f"{meters/1000} Kilometeres")
            print (f"{meters * 3.28084} feet")
            print (f"{meters/1609.34} miles")
        except:
            print ("Enter a valid input!\n")
            Length()

    def Weight():
        try:
            kilograms = float(input("Enter a value Kg "))
            print (f"{kilograms} kg is equal to:")
            print (f"{kilograms * 1000} grams")
            print (f"{kilograms * 2.20462} pounds")
            print (f"{kilograms * 35.274} ounces")
        except:
            print ("Enter a valid input!\n")
            Weight()
        
    def Temperature():
        try:
            celsius = float(input("Enter a value in Celsius "))
            print (f"{celsius}°C is equal to:")
            print (f"{(celsius * 9/5) + 32}°F (Fahrenheit)")
            print (f"{celsius + 273.15} K (Kelvin)")
        except:
            print ("Enter a valid input!\n")
            Temperature()

    print ("\nChoose a conversion type!")
    print ("1. Length (meteres to kilometers, feet, or miles)")
    print ("2. Weight (Kilograms to grams, pounds or ounces)")
    print ("3. Temperature (Celsius to Fahrenheit or Kelvin)")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        Length()   
    elif choice == "2":
        Weight()
    elif choice == "3":
        Temperature()
    else:
        print("Invalid choice! Please select a valid option.\n")
        Unit_Converter()
    
while True:
    Unit_Converter()
    again_input = input("Do you want to check again (y/n): ")
    if again_input != 'y':
        print ("Thank you for using.")
        break

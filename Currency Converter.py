from currency_converter import CurrencyConverter

c = CurrencyConverter()

def get_valid_curency(prompt):
    while True:
        from_currency = input(prompt).upper()
        if from_currency in c.currencies:
            return from_currency
        else:
            print ("Invalid currency code! Please enter a valid currency (e.g., USD, EUR, INR).")
        
def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            return amount
        except:
            print ("Enter a valid amount!")

def exchange_function():
    from_currency = get_valid_curency("Enter the base currency (e.g., USD): ")
    to_currency = get_valid_curency("Enter the target currency (e.g., INR): ")
    amount = get_valid_amount(f"Enter the amount in {from_currency}: ")
    converted_amount = c.convert(amount, from_currency, to_currency)
    print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}.\n")

print ("""-------------------------
   CURRENCY CONVERTER
-------------------------              
""")        
        
while True:
    exchange_function()
    user_input = input("Do you want to check again (y/n): ").lower()
    if user_input not in ["y", "yes"]:
        print ("Thank You For using.")
        break

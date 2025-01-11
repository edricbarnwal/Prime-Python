print ("""--------------------
BUDGET TRACKER
--------------------""")

def Add_Income(Capital, Income, Source):
    Capital['balance'] = Capital['balance'] + Income
    Capital['transaction'].append({"type":"income", "amount":Income, "source":Source})
    
def Add_Expense(Capital, Expense, category):
    Capital['balance'] = Capital['balance'] - Expense
    Capital['transaction'].append({"type":"expense", "amount":Expense, "categor":category})

def view_balance(Capital):
    print (f"Curret Balance: ${Capital['balance']:.2f}")

def view_transaction(Capital):
    for transaction in  (Capital['transaction']):
        print (transaction)

Budget = {
    'balance':0,
    'transaction':[]
    }

while True:
    def income_add():
        try: 
            User_Income = int(input("Enter income amount: "))
            Income_Source = (input("Enter Income Source: "))
            Add_Income(Budget, User_Income, Income_Source)
            print(f"${User_Income} added successfully.")
        except ValueError:
            print ("Enter a valid Amount.")
            income_add()

    def expense_add():
        try:
            User_Expense = int(input("Enter expense amount: "))
            category = input("Enter category: ")
            Add_Expense(Budget, User_Expense, category)
        except ValueError:
            print ("Enter a valid amount.")
            expense_add()

    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transactions")
    print("5. Exit")

    user_choice = input("Choose an option: ")

    if user_choice == "1":
        income_add()

    elif user_choice == '2':
        expense_add()

    elif user_choice == '3':
        view_balance(Budget)

    elif user_choice == '4':
        print (view_transaction(Budget))

    elif user_choice == '5':
        print("Thanks For Using. Good Bye")
        break

    else:
        print("Invaid Choice! Please Try Again")

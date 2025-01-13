import random

def roll_dice():
    while True:
        User_Input = input("Press Enter to roll the dice, or type 'exit' to quit: ").strip().lower()
        if User_Input == 'exit':
            print("Thanks for playing Goodbye!")
            break
        else:
            dice_value = random.randint(1, 6)
            print (f"You rolled a:  {dice_value}")
            print ("-"*30)

print ("""--------------------
ROLL DICE SIMULATOR
--------------------       
""")

roll_dice()

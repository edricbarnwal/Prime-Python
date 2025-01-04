import random 

print ("*** Welcome to Think & Guess! ***")
print ("Can you guess the number I'm thinking of?")
print ("You have 6 chances to guess a number between 1 to 100")

def guess_number(lives=6):
    guessing_num = random.randint(1, 100)
    while lives >= 0:
        try:
            lives -= 1 
            user_guess = int(input("Enter you guess: "))
            if guessing_num == user_guess:
                print ("!You win!")
                break
            
            elif guessing_num > user_guess and user_guess:
                print ("To Low!")
            
            elif guessing_num < user_guess and user_guess:
                print ("To High!")
            print (f"{lives} lives left.")
               
            
        except:
            print ("Enter a valid integer between 1 to 100.")
        if lives == 0:
            print (f"You've used all your lives. Game Over!\nCorrect guess is {guessing_num}")
            break

while True:
    guess_number()
    play_again = input("Do you want to play again (y/n): ").lower()
    if play_again != "y":
        print ("Thanks for playing")
        break

import random 

print ("*** Think & Guess ***")
print ("Guess Number in 6 lives\nBetween 1 to 100\nEnjoy!")

guessing_num = random.randint(1, 100)

def guess_number(lives=6): 
    while lives >= 0:
        try:
            user_guess = int(input("Enter you guess: "))
            if guessing_num == user_guess:
                print ("!You win!")
                break
            
            elif guessing_num > user_guess and user_guess:
                print ("!To Low")
            
            elif guessing_num < user_guess and user_guess:
                print ("!To High")
            lives -= 1
        except:
            print ("Enter a valid integer between 1 to 100.")
        if lives == 0:
            print (f"You out of all lives\nCorrect guess is {guessing_num}")
            break

while True:
    guess_number()
    play_again = input("Do you want to play again (y/n): ").lower()
    if play_again != "y":
        print ("Thanks for playing")
        break

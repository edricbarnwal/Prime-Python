import random 

print ("*** Think & Guess ***")

guessing_num = random.randint(1, 100)




lives = 5

while lives > 0:
    user_guess = int(input("Enter you guess: "))
    lives -= 1

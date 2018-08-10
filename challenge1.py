#challenge 1 prompt: create a guess the number uding a while loop
from random import * #import * is a wild card that says import all information


aRandomNumber = randint(1,20) #inclsuive
#generates a randominteger


guess = input("Guess a number between 1 and 20 inclusive: ")
#assume user's guess is equal to 5

if not guess.isnumeric(): #checks to see if users guess is a real number
    print("That's not a positive whole number, try again!")

else:
    guess = int(guess) #converts a string to an integer
    if guess < 1 or guess > 20:
        print("That's not a positive whole number, try again!")
    elif(guess > aRandomNumber):
        print("Pick a smaller number")
    elif(guess < aRandomNumber):
        print("Pick a smaller number")
    else:
        print("You win!")

print("game over")

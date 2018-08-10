from random import *

aRandomNumber = randint(1, 2)
tries = 0

for i in range(3):
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric():
        print("That's not a positive whole number, try again!")
    else:
        guess = int(guess)
    if (guess == aRandomNumber):
        print("That's correct!")
        break
    if (guess > aRandomNumber):
        print("Guess lower!")
        tries +=1
    if (guess < aRandomNumber):
        print("Guess higher!")
        tries += 1

    if (tries == 3) & (guess != aRandomNumber):
        print("You lose. Try again next time!")
        break

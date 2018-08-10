# choose a word
# validate the input (check that it is not a number)
# use while loop to keep asking for valid input
# make everythign the same case (upper and lower case)
# create winning and losing conditions
# display how many letters are in the word
# tell the player if the answer is right or wrong
# display the correct letter in the word
# tell the player if the answer is right or wrong
# display the correct letter in the word
# let them know how many tries they have left
#find ways to create a word using the guessed letters
#collect letters that have already been guessed
# check each guess asainst used letters

#at the end of each try:
# check if the play wonder
# display how many tries left
# if out of tries: player loses
# if not out of tries: display tries and keep going


from random import *
words = ["normal"]
word = randint(0,len(words)-1)
print("Welcome to Hangman! Guess the word according to the amount of dashes it has: ")
for i in range(len(words[word])):
    print("_", end=" ")
win = False
tries = 7
guess = input()
guesses=''


while tries > 0:
    if guess.isnumeric():
        print("that's not a letter, try again")
        guess = input()
    for char in words[word]:
        if char in guess:
            print(char, end=" ")
            
        else:
            print("_", end=" ")
            tries -= 1



if tries == 0:
    print("You lose.")

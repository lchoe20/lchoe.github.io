





#example of while loop
#evaluate the loop while the condition is True
i = 0 #instantiating the variable i
happyPoints = 0
numOfTImes = 5
notHappy = True

while i < 5:
    print(i)
    print("I am inside of the inside of the while loop")
    i += 1

print("done with while loop")


#example of for loop
#evaluate the loop a given number of times
j = 0
for i in range(5): #for for loop instantiate i in loop
    print(j)
    print("I am inside of the for loop")

print("done with for loop")

while(notHappy):
    print("I am still not happy")
    happyPoints += 1

    if(happyPoints >10):
        notHappy = False #change notHappy to false, end of loop.

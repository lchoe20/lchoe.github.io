#This is a comment
#Python doesn't read
#what goes here
#Only for HUmans!

#prints hello world


i = -1
while True:
    i += 1

    if(i > 20):
        break

    #i is odd
    if(i % 2 != 0):
        continue

    print(i)


answer = input("What is your favorite color?")
if(answer == "blue"):
    print("Me too!")
print(answer, "looks good on you!")
done = True



value = True
anotherValue = False
yetAnotherValue = True
print("&", value & anotherValue)
print("^", value ^ anotherValue)
print("==", value == yetAnotherValue)

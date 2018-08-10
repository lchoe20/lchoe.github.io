


def print_name():
    name = input("What's your name?")
    print("Hi " + name + "!")
def siblings():
    sibling = input("How many siblings do you have?")
    sibling = int(sibling)
    if sibling == 0:
        print("Must be pretty lonely...")
    if sibling == 1:
        print("Me too!")
    if sibling == 2:
        print("That's cool!")
    if sibling > 2:
        print("Must be pretty loud in the house...")





def compare():
    sibling = input("How many siblings do you have?")
    sibling = int(sibling)
    mySibling = 1
    if sibling > mySibling:
        more = sibling - mySibling
        more = str(more)
        print("You have " + more + " more siblings than I do!")
    if sibling == mySibling:
        print("We both have 1 sibling!")
    elif sibling < mySibling:
        print("You have 1 less sibling than me!")


print_name()
siblings()
compare()






def your_year(year):
    print_name()
    myYear = 1995
    if(myYear > year):
        print("I am younger than you")
    elif(myYear < year):
        print("I am older than you")
    else:
        print("We're the same age")

def print_sum(a,b):
    print(a+b)

age = input("What year were you born?")
age = int(age)
your_year(age)
your_year(1932)


print("Now printing sums: \n")
print_sum(5,4) #parameter inserts it in
print_sum("winter","sammy")

















def add(a,b):
    return a + b

yourFirstNum = input("Please enter your first favorite number ")
yourFirstNum = int(yourFirstNum)
yourSecondNum = input("Please enter your second favorite number ")
yourSecondNum = int(yourSecondNum)


print(add(yourFirstNum,yourSecondNum))

print(add(5,4))

result = add(5,4)
print(result)

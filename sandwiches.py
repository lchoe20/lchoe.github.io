print("TIme for lunch!") #print string

breadSlices = 10
peanutButter = 100
jelly = 100
sandwhich = 0

while breadSlices > 0:
    print("It's peanut butter jelly time!")
    breadSlices = breadSlices - 2
    print("I have %d breadslices left over" %(breadSlices))
    peanutButter = peanutButter - 5
    jelly -= 5
    sandwhich += 1

print("I made %d sandwiches." %(sandwhich))
print("I have %dg of peanut butter and %dg of jelly left over." %(peanutButter, jelly))
print("Delicious")

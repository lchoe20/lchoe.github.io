import math
import turtle

def printName():
    print("Winter Smith") # not return function
printName()

def PrintNameReturn():
    return("Winter Smith") # return function


print(math.sqrt(4)) # return function that takes parameter
print(math.floor(10.2)) # return function that takes parameter

from turtle import *
color('blue', 'teal')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

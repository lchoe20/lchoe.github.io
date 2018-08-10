# this is a global variable

a = 0

if a == 0:
    # this is still a gloval variable
    b = 1

def my_function(c):
    # this is a local variable
    d = 3
    print(c)
    print(d)

# now we call the function, passing the value 7 as the first and only parameter

my_function(7) # prints 7 and 3

# a and b still exist
print(a)
print(b)

print(c) # parameter that only gets turned into c when in the function
print(d) # d is inside the function

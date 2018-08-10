fileVar = open("dictionary.txt")

print("Can your password survive a dictionary attack?")

test_password = input("Type in a trial password:")

in_dictionary = False

for line in fileVar:
    if line.strip() in test_password.strip():
        print("Password found in dictionary")
        in_dictionary = True
        break
    else:
        continue

if(in_dictionary == False):
    print("Your password wasn't found in this dictionary")

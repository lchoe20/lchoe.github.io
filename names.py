from random import randint

print("Find out your name from your past life!")

names = ["Janice", "David", "George", "Ricky", "Bella", "Haley", "James", "Jack", "John", "Tori", "Danica", "Mary", "Caroline"]

aRandomIndex = randint(0,len(names)-1)

print(names[aRandomIndex])

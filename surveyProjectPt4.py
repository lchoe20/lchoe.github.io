# this program loads survey data that is saved in a JSON file and does some simple analysis of the data

import json
from pprint import pprint
may = 0

fileVar = open("allanswers.json","r") # reading from the file that is opened
data = json.load(fileVar) # converts fileVar into something that json can read
print(type(data))
print(data)
fileVar.close()

# do some analysis with our data
ages = []
for s in range(len(data)):
    if data[s]['age'] is not '': # skips over blank enteries
        ages.append(int(data[s]['age']))

print(ages)
total = sum(ages)
average = total/len(ages)

print(average)

print(len(data))


# how many people have the same birthday
# take in a month in number format as the parameter
def how_many_birthdays(month):
    num_of_respondents = 0
    for s in range(len(data)): # iterate through the data
        new_birthday = data[s]['DOB'] # save a birthday as a string called new_birthday
        new_month = new_birthday[0]+new_birthday[1]
        print(new_month)
        if(new_month == month):
            num_of_respondents += 1
    print("The number of people with birthdays in "+month+" is equal to: ")
    print(num_of_respondents)
how_many_birthdays("05")

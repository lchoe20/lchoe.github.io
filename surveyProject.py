import json


# create a dictionary to store the responses

# create a list of survery questions and a list of related keys

survey = ["What is your name?",
         "How old are you?",
         "What is your hometown?",
         "What is your date of birth?"]

keys = ["name","age","hometown","DOB"]

# iterate over the list of survey
# questions and take in user responses


list_of_answers = []

done = "NO"

while done == "NO":
    answers = {}
    print("New entry! Please answer the questions below.")
    for x in range(len(survey)):
        answer = input(survey[x]+": ")
        answers[keys[x]] = answer
    list_of_answers.append(answers)
    done = input("Are you done collecting information? Type YES or NO").upper()



#open the file containing all past results and append them to our current list
fileVar = open("allanswers.json","r")
old_data = json.load(fileVar) # makes it readable for python
list_of_answers.extend(old_data)
fileVar.close()


# reopen the file in write mode and write each entry in json format
fileVar = open("allanswers.json","w")
fileVar.write('[\n')
index = 0
for currentDictionary in list_of_answers:
    if(index < len(list_of_answers)-1):
        json.dump(currentDictionary,fileVar) # dumping current dictionary to file
        fileVar.write(',\n')
    else:
        json.dump(currentDictionary,fileVar)
        fileVar.write('\n')
    index += 1

fileVar.write(']')
fileVar.close()

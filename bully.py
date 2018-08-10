import json

survey = ["Have you ever been bullied?",
           "Have you ever bullied someone?",
           "Are you currently being bullied?",
           "Are you currently bullying someone?"]

info = ['victimized','bullied','victim','bully']



list_of_answers = []

done = "NO"

while done == "NO":
    answers = {}
    print("New entry! Please answer the questions below.")
    for x in range(len(survey)):
        answer = input(survey[x]+": ")
        answers[info[x]] = answer
    list_of_answers.append(answers)
    done = input("Are you done collecting information? Type YES or NO").upper()

#open the file containing all past results and append them to our current list
fileVar = open("allanswers.json","r")
old_data = json.load(fileVar) #makes it readable for python
list_of_answers.extend(old_data)
fileVar.close()

index = 0

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
        fileVar('\n')
    index += 1

fileVar.write(']')
fileVar.close()

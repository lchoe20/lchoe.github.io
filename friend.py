friends = ["Beyonce", "Jay-Z", "Chrissy Teigen", "Barack Obama", "Stephen Colbert"]
weight = [153.4, 81.2, 1293.4, 432.6]
random_data = ["George", 8, 10.2]

print(friends[0])
print(weight)
print(random_data)

print(len(friends)) #length of the list

print("Beyonce" in friends) #returns a boolean to see if Beyonce is in the list friends

for i in range(5):
    print(friends[i]) #same thing as below

for i in friends:
    print(i) #same thing as above


print("Sammy" + "Con") #same thing

name = "Sammy"
print(name + "Con") #same thing

event = "Con"
print("Sammy" + event) #same thing

print(name + event) #same thing

chris_list = ["Chris Pratt","Chris Evans","Chris Hemsworth","Chris Pine"]

print(chris_list[1:3]) #print 1 and 2, not including 3
print(chris_list[:3]) #print everything to 3
print(chris_list[3:]) #print 3 to everything
print(chris_list[:]) #print everything
print(chris_list[-1]) #starts backward from Chris Pine

alphabetized_list = chris_list.sort()
print(alphabetized_list)

scream = "SCREAM"
print(scream)
print(scream.lower()) #print lower case

whisper = "shhh"
print(whisper.upper())

print(chris_list.append("Chris Hunter")) #add Chris Hunter to the list






response = input("Do you want to go left or right?")
if response == "right":
    print("We are going right") #noob way

if "right" in response.lower(): #allows more input
    print("We are going right")
if "left" in response.lower(): #allows more input
    print("We are going left")

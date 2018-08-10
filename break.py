
# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in an abandoned hospital bed. You look around at the decaying walls with paint peeling off. You smell mold and feel the cold humid air pressing down on yourself.
You see a cutain near your bed and a door.
'''
from random import *

randomNumber = randint(1, 2)

print(start)

print("Which way do you choose to go...through the 'curtain' or the 'door'?") # Update to match your story.
curtainOrDoor = input()
if curtainOrDoor == "curtain":
    print("You go through the curtain and you see a woman breathing heavily. She seems do be hurt and vulnerable, but she also seems like she has the capability of hurting you. You also see a key next to her, and it seems important but you wonder if it is worth the risk. Do you run away quickly and return to safety or atttempt to get the key? Choose 'run' or 'key'.") # Update to match your story.
    runOrKey = input()
    if runOrKey == "run":
        print("You run out the door and...you can choose to go down the hallway and attempt to exit through the 'window' or the 'stairs'. What do you choose?") # Update to match your story.
        windowOrStairs = input()
        if windowOrStairs == "window":
            if randomNumber == 1:
                print("As you take a deep breath, you attempt to jump out the 4th story window. You landed on a bush and Thankfully, it breaks your fall and you escape.")
            else:
                print("You jump out the window and scream, you fall on the cement and die.")
        if windowOrStairs == "stairs":
                print("You trip on the steps falling into a hole and fell forever, dying.")
    if runOrKey == "key":
        print("You attempt to get the key. The woman stays there and you back away. You can now choose to go through the 'locked door' and try your chances, or just go out of the 'unlocked door' that looks to be safer.")
        lockedDoorOrDoor = input()
        if lockedDoorOrDoor == "unlocked door":
            print("You go through the unlocked door and...you can choose to go down the hallway and attempt to exit through the 'window' or the 'stairs'. What do you choose?") # Update to match your story.
            windowOrStairs = input()
            if windowOrStairs == "window":
                if randomNumber == 1:
                    print("As you take a deep breath, you attempt to jump out the 4th story window. You landed on a bush and Thankfully, it breaks your fall and you escape..")
                else:
                    print("You jump out the window and scream, you fall on the cement and die.")
            if windowOrStairs == "stairs":
                    print("You trip on the steps falling into a hole and fell forever, dying.")
        if lockedDoorOrDoor == "locked door":
            print("You went through the locked door. Inside the room there is nothing, but a tunnel that seems to lead nowhere. The door suddenly slams shut and you have no choice but to enter the tunnel. Once inside, you have the choice to travel 'left' or 'right'. Which way should you go?")
            leftOrRight = input()
            if leftOrRight == "left":
                print ("You meet good dog named something. He leads you out of the creepy tunnel to the fresh outdoors. You look back at the hospital and feel a sense of happiness.")
                print("Congratulations! You made it out safely!") #name later
            if leftOrRight == "right":
                print ("You meet bad dog named something. He leads you towards a dimly lit room. Inside is an old creepy doctor who starts starign at you.")
                print("Doctor: I didn't think you would make it this far...... ")
                print("I'll make sure not to let you make it any further.")
                print("You unfortunately died!")


    # Continue code to finish story.

elif curtainOrDoor == "door":
    print("You go through the door and...you can choose to go down the hallway and attempt to exit through the 'window' or the 'stairs'. What do you choose?") # Update to match your story.
    windowOrStairs = input()
    if windowOrStairs == "window":
        if randomNumber == 1:
            print("As you take a deep breath, you attempt to jump out the 4th story window. You landed on a bush and Thankfully, it breaks your fall and you escape..")
        else:
            print("You jump out the window and scream, you fall on the cement and die.")
    if windowOrStairs == "stairs":
            print("You trip on the steps falling into a hole and fell forever, dying.")
    # Continue code to finish story.

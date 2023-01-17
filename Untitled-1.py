# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Part 1
response = ""
while response not in directions:
    print("To your left, you see a bear.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The bear eats you. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You head deeper into the forest.\n")
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = "" 
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")
        # Part 2
        response = ""
        while response not in directions:
            print("To your left you see a house")
            print("To your right you see more forest")
            print("There is a waterfall ahead you can get water from")
            print("Beihind you is a bear")
            response = input("What diretion do you move?\nleft/right/forward/backward\n")
            if response == "left":
                print("You go inside the house and you meet a old man")
            elif response == "right":
                print("You go further into the forest")
            elif response == "forward":
                print("You Drink some water")
            elif response == "backward":
                print("the bear ate you. goodbye, " + name + ".")
                quit()
            else:
                print("I didn't understand that.\n")
                # Part 3
                response = ""
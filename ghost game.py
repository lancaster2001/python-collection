from random import randint                  #imports the random library
print("Ghost Game")                         #print ghost game to the screen
feeling_brave = True                        #sets variable to true
score = 0                                   #initialises a variable called score to 0
while feeling_brave:                        #starts while loop - while feeling_brave = true
    ghost_door = randint(1,3)               #sets ghost_door variable to a random between 1 and 3
    print ("Three doors ahead...")          #prints three doors ahead to the screen
    print ("A ghost behindone.")            #prints a ghost behind 1 to the screen
    print ("which door do you open?")       #prints whichdoor do you open to screen
    door = input("1,2 or 3?")               #takes use input 1,2 or 3 and stores it in a variable called doors
    door_num = int(door)                    #putting user variable (string) into another avriable called door_num (interger)
    if door_num == ghost_door:              #
        print("GHOST!")                     #
        feeling_brave = False               #
    else:                                   #
        print("No ghost")                   #
        print("you enter the next room.")   #
        score = score + 1                   #
print("Run away!")                          #
print("game over, you scored",score)        #

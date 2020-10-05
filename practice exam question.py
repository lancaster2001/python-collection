player_1_score = int(0)
player_2_score = int(0)
win = 0
D1 = 0
D2 = 0
move_by = 0
roll = ""
import random

print("game start")
print("type roll to roll")

while win == 0:
    D1 = (random.randint(1,6))
    D2 = (random.randint(1,6))
    roll = input("player 1's turn")
    move_by = D1+D2

    if D1 == D2:
        player_1_score = player_1_score - move_by

    if not D1 == D2:
        player_1_score = player_1_score + move_by

    print("Dice 1 =",D1)
    print("Dice 2 =",D2)
    print("player 1 moved",move_by,"spaces")
    print("player 1's place", player_1_score)
    print("")

    if player_1_score > 48:
        print ("player 1 wins")
        win = 1
    

    if win == 0:
        D1 = (random.randint(1,6))
        D2 = (random.randint(1,6))
        roll = input("player 2's turn")
        move_by = D1+D2jif D1 == D2:
        player_2_score = player_2_score - move_by

    if not D1 == D2:
        player_2_score = player_2_score + move_by

    print("Dice 1 =",D1)
    print("Dice 2 =",D2)
    print("player 2 moved",move_by,"spaces")
    print("player 2's place", player_2_score)
    print("")
    
    if player_2_score > 48:
        print ("player 2 wins")
        win = 1


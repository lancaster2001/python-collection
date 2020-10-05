player_1_score = int(0)
player_2_score = int(0)
win = 0
D1 = 0
D2 = 0
move_by = 0
import random

print("game start")

while win == 0:
    D1 = (random.randint(1,6))
    D2 = (random.randint(1,6))
    move_by = D1+D2
    if D1 == D2:
        player_1_score = player_1_score - move_by
    if not D1 == D2:
        player_1_score = player_1_score + move_by
    print("player 1's place", player_1_score)
    if player_1_score > 48:
        print ("player 1 wins")
        win = 1
    if win == 0:
        D1 = (random.randint(1,6))
        D2 = (random.randint(1,6))
        move_by = D1+D2
    if D1 == D2:
        player_2_score = player_2_score - move_by
    if not D1 == D2:
        player_2_score = player_2_score + move_by
        print("player 2's place", player_2_score)
        if player_2_score > 48:
            print ("player 2 wins")
            win = 1


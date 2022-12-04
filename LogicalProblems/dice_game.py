""".vscode\
    1. This is a game for two users. Each user takes turn rolling the dice. 
Dice values can be 0 to 12. If the user rolls 1,4,6,or 12, he gets a point and 
another chance to roll 
If the user gets a point three times in a row, Tehran he gets 5 additional points. 
Each user can play a maximum of 50 times. 
The user that takes max point wins. 

2. Same game as above. Add an additional condition to subtract one point when the user rolls 0. 
If the user rolls 9, then he will miss a turn.
    """

import random

user_1_point = 0
user_1_streak = 0 
user_1_turn = True
user_2_turn = False
user_2_point = 0
user_2_streak = 0
user_1_round = 0
user_2_round = 0
def numGenerator():
    user_number = random.randint(0, 12)
    return user_number
def addpoint (user_number):
    if(user_number == 1 or user_number == 4 or user_number == 6 or user_number == 12):
       return 1
    else:
        return 0
def subpoint (user_number):
    if(user_number == 0):
        return 1
    else:
        return 0
def loseTurn (user_number):
    if(user_number == 9 or user_number == 2 or user_number == 3 ):
        return 1
    else:
        return 0
for rounds in range(10):
    if(user_1_turn):
        user_1_round += 1
        user_2_streak = 0
        user_2_turn = True
        user_1_turn = False
        user_1_number = numGenerator()
        if(addpoint(user_1_number)):
            user_1_point += 1
            user_1_streak += 1
            if(user_1_streak == 3):
                user_1_point += 5
                user_1_streak = 0
                user_1_turn = True
                user_2_turn = False
        if(subpoint(user_1_number)):
            user_1_point -= 1
        if(loseTurn(user_1_number)):
            user_1_round += 1 
            if(user_1_round >= 5):
                user_1_turn = False
            break
    if(user_2_turn):
        user_2_round += 1
        user_1_streak = 0
        user_1_turn = True
        user_2_turn = False
        user_2_number = numGenerator()
        if(addpoint(user_2_number)):
            user_2_point += 1
            user_2_streak += 1
            if(user_2_streak == 3):
                user_2_point += 5
                user_2_streak = 0
                user_2_turn = True
                user_1_turn = False
        if(subpoint(user_2_number)):
            user_2_point -= 1
        if(loseTurn(user_2_number)):
            user_2_round += 1 
            if(user_2_round >= 5):
                user_2_turn = False
            break
    if(user_1_point <=0):
        user_1_point = 0
    elif(user_2_point <= 0):
        user_2_point = 0  
    if( user_1_round >= 5 and user_2_round >= 5):
        user_1_turn = StopIteration(rounds)
        user_2_turn = StopIteration(rounds) 

print("user 1 point : ",user_1_point)
print("user 2 point : ",user_2_point)
print("player 1 played round : ",user_1_round)
print("player 2 played round : ",user_2_round)

if(user_1_point > user_2_point):
    print("user 1 wins")
elif(user_1_point == user_2_point):
    print("match tied")
else:
    print("user 2 wins")
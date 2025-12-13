from random import *
def spin(y):
    roll = []
    points = 0
    if y == "cheat.func":
        roll = [5, 5, 5]
    else:
        for i in range (3):
            newroll = randint(1,5)
            roll.append(newroll)
            print("You rolled one", newroll)
    if roll[0] == roll[1] == roll[2]:
        points = roll[0] * 4
    else:
        highest = 0
        for i in range (3):
            if highest <= roll[i]:
                highest = roll[i]
        points = highest
        for i in range (3):
            if roll[i] != highest:
                points = points - roll[i]
    return points
points = 10
print(points)
while points > 0:
    print("LETS GO GAMBLING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    start = input("DO YOU WANNA GO GAMBLING? ")
    if start == "no":
        print("OK!")
        punishment = randint(1,5)
        if punishment == 1:
            print("BANISHMENT!!!!!!!!!!!!!!!!!")
        elif punishment == 2:
            print("DEATH...")
        elif punishment == 3:
            print("SEND THEM TO THE SHADOW REALM!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        elif punishment == 4:
            print("CAR BATTERY TO THE HEAD!!!!!!!!!")
        elif punishment == 5:
            print("EXODIA OBLIDERATE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        quit()
            
    else:
        points = points - 1
        score = spin(start)
        print("You scored", score)
        print("Gambling costs 1 score so...")
        points = points + score
        print("You now have", points, "in total")
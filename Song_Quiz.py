from random import randint

#Shows the high scores
def highscores():
    with open ("Points.txt") as file:
        listpoints = file.readlines()
        file.close
    with open("Usernames.txt") as file:
        users = file.readlines()
        file.close
    highest = 0
    location = 0
    high5 = []
    highusers = []
    for i in range (5):
        highest = 0
        for y in range(len(listpoints)):
            currentscore = listpoints[y]
            currentscore = currentscore.strip()
            currentscore = int(currentscore)
            if currentscore > highest:
                highest = currentscore
                highestuser = users[y].strip()
                location = y
        high5.append(highest)
        listpoints.pop(location)
        highusers.append(highestuser)
        users.pop(location)
    for z in range (5):
        x = z + 1
        print(x, high5[z], highusers[z])
    menu()
            

#Checks for a valid user
def login():
    entrypath = input("Would you like to log in or sign up? ")
    if entrypath == "sign up":
        users = open("Usernames.txt", "a")
        passwords = open("Passwords.txt", "a")
        user = input("Enter your username: ")
        activeuser = user
        password = input("Enter your password: ")
        users.write(user + '\n')
        passwords.write(password + '\n')
        users.close()
        passwords.close()
        points = open("Points.txt", "a")
        points.write('\n')
        points.write("0")
        points.close()
        
    else:
        with open("Usernames.txt") as file:
            users = file.readlines()
            file.close
        with open("Passwords.txt") as file:
            passwords = file.readlines()
            file.close
        enter1 = "Q"
        enter2 = "Q"
        attempts = 0
        correctuser = False
        correctpass = False
        while correctuser == False or correctpass == False:
            if attempts == 5:
                print("Too many attempts")
                exit()
            else:
                print("Enter your username and password")
                enter1 = input("Enter your username: ")
                enter2 = input("Enter your password: ")
                attempts += 1
            for i in users:
                if i.strip() == enter1:
                    correctuser = True
            for i in passwords:
                if i.strip() == enter2:
                    correctpass = True
        activeuser = enter1
    play(activeuser)

#Runs the game
def play(user):
    lives = True
    points = 0
    while lives == True:
        with open("Songs.txt") as file:
            songs = file.readlines()
            file.close
        with open("Artists.txt") as file:
            artists = file.readlines()
            file.close
        indexofanswers = randint(0, 24)
        newsong = songs[indexofanswers].strip()
        displaysong = newsong[0]
        for i in range (len(newsong)):
            if newsong[i] == ' ':
                displaysong += ' '
                displaysong += newsong[i + 1]
        newartist = artists[indexofanswers].strip()
        print(displaysong, "by", newartist)
        ans = input("What's your answer? ")
        if ans != newsong:
            ans = input("Try again. What's your answer? ")
            if ans != newsong:
                lives = False
            else:
                points += 1
        else:
            points += 1
    print("Out of lives!")
    print("You scored", points)
    with open ("Points.txt") as file:
        listpoints = file.readlines()
        file.close
    with open("Usernames.txt") as file:
        users = file.readlines()
        file.close
    location = users.index(user + '\n')
    currenthigh = listpoints[location]
    currenthigh = currenthigh.strip()
    print(currenthigh)
    if int(currenthigh) < points:
        listpoints.pop(location)
        listpoints.insert(location, str(points) + '\n')
        Points = open("Points.txt", "w")
        Points.write("")
        Points.close()
        Points = open("Points.txt", "a")
        for i in listpoints:
            Points.write(i)

#Gives the user instructions for how to play
def menu():
    print("Time to FACE THE MUSIC")
    begin = input("Press y to begin and h to see the high scores! ")
    if begin == "y":
        login()
    else:
        highscores()

menu()
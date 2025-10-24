from random import randint

menu = '''WELCOME TO GAME.PY!!!!!!!!!!!!!

Press 1 to play Guesser

Press 2 to find out your Fantasy Name

Press 3 to play NUM BOMBER

Press 4 to play Number Race

Press 5 to play blackjack

Press 6 to play unscramble

Press 7 to play hangman


At any time, you can quit your game and return here by typing QUIT'''

def Guesser():
    guess = 101
    ans = randint(1, 100)
    guesses = 0
    while guess != ans:
        guess = input("Guess a number: ")
        if guess == "QUIT":
            print("Returning")
            guess = ans
        else:
            guess = int(guess)
            if guess > ans:
                print("Lower")
            elif guess < ans:
                print("Higher")
        
        guesses = guesses + 1
    print("YOU GOT IT RIGHT :)")
    print("You took", guesses, "tries")

def Fantasy_Name():
    name = input("What is your first name? ")
    if name != "QUIT":
        name = name[0].lower()
    match name:
        case "a":
            Fname = "Alphus"
        case "b":
            Fname = "Belphezark"
        case "c":
            Fname = "Choralung"
        case "d":
            Fname = "Dorian"
        case "e":
            Fname = "Elara"
        case "f":
            Fname = "Flirgest"
        case "g":
            Fname = "Grekort"
        case "h":
            Fname = "Horunok"
        case "i":
            Fname = "Ilkin"
        case "j":
            Fname = "Jangmoch"
        case "k":
            Fname = "Koren"
        case "l":
            Fname = "Lunaris"
        case "m":
            Fname = "Muyna"
        case "n":
            Fname = "Norille"
        case "o":
            Fname = "Orbus"
        case "p":
            Fname = "Penumbru"
        case "q":
            Fname = "Quensh"
        case "r":
            Fname = "Rosufvele"
        case "s":
            Fname = "Srntook"
        case "t":
            Fname = "Thorenvale"
        case "u":
            Fname = "Unobloss"
        case "v":
            Fname = "Voralle'thuk"
        case "w":
            Fname = "Whoontuum"
        case "x":
            Fname = "Xeriale"
        case "y":
            Fname = "Deltae'yure"
        case "z":
            Fname = "Z'thomeggar"
        case _:
            Fname = "Emptarr'ollz"
    if name != "QUIT":
        birth = input("What month were you born in? ").capitalize()
        match birth:
            case "January":
                Sname = "Dawnspark"
            case "February":
                Sname = "Leapyor"
            case "March":
                Sname = "Firstbloom"
            case "April":
                Sname = "Rejoicer"
            case "May":
                Sname = "Highbloom"
            case "June":
                Sname = "Glornt'ark"
            case "July":
                Sname = "Sunsporrk"
            case "August":
                Sname = "Gloe-dusk"
            case "September":
                Sname = "Dorwarenon"
            case "October":
                Sname = "Hauntmoon"
            case "November":
                Sname = "Crimmzont"
            case "December":
                Sname = "Everwinter"
            case _:
                Sname = "Voiddusk"
        if birth != "Quit":
            title = randint(1,6)
            if title == 1:
                title = "the Wise Sage"
            elif title == 2:
                title = "the Fierce Warlord"
            elif title == 3:
                title = "the Stalwart Warden"
            elif title == 4:
                title = "the Regal Ruler"
            elif title == 5:
                title = "the Frail Idiot"
            else:
                title = "the Crusading Champion"
            print("Hello", Fname, Sname, title)
            back = input("Press enter to return to menu")
    
def Num_Bomber():
    board1 = ['X', 'X', 'X', 'X']
    board2 = ['X', 'X', 'X', 'X']
    board3 = ['X', 'X', 'X', 'X']
    board4 = ['X', 'X', 'X', 'X']
    enemyboard1 = ['X', 'X', 'X', 'X']
    enemyboard2 = ['X', 'X', 'X', 'X']
    enemyboard3 = ['X', 'X', 'X', 'X']
    enemyboard4 = ['X', 'X', 'X', 'X']
    print("You may place stations in 4 spaces, your aim is to eliminate all of your enemies stations before they can eliminate your's")
    x = ""
    y = ""
    for i in range (4):
        if x != "QUIT" and y != "QUIT":
            x = input("What is the x coordinate of the next station? 1, 2, 3 or 4 ")
            if x != "QUIT":
                x = int(x)
                y = input("What is the y coordinate of the next station? 1, 2, 3 or 4 ")
                if y != "QUIT":
                    y = int(y)
                    x = x - 1
                    match y:
                        case 1:
                            if board1[x] != "1":
                                board1.pop(x)
                                board1.insert(x, "1")
                            else:
                                while board1[x] == "1":
                                    x = x - 1
                                    if x == -1:
                                        x = 3
                                board1.pop(x)
                                board1.insert(x, "1")
                        case 2:
                            if board2[x] != "1":
                                board2.pop(x)
                                board2.insert(x, "1")
                            else:
                                while board2[x] == "1":
                                    x = x - 1
                                    if x == -1:
                                        x = 3
                                board2.pop(x)
                                board2.insert(x, "1")
                        case 3:
                            if board3[x] != "1":
                                board3.pop(x)
                                board3.insert(x, "1")
                            else:
                                while board3[x] == "1":
                                    x = x - 1
                                    if x == -1:
                                        x = 3
                                board3.pop(x)
                                board3.insert(x, "1")
                        case 4:
                            if board4[x] != "1":
                                board4.pop(x)
                                board4.insert(x, "1")
                            else:
                                while board4[x] == "1":
                                    x = x - 1
                                    if x == -1:
                                        x = 3
                                board4.pop(x)
                                board4.insert(x, "1")
                    y = randint(1,4)
                    x = randint(0,3)
                    match y:
                        case 1:
                            if enemyboard1[x] != "1":
                                enemyboard1.pop(x)
                                enemyboard1.insert(x, "1")
                            else:
                                while enemyboard1[x] == "1":
                                    x = x - 1
                                    if x == -1:
                                        x = 3
                                enemyboard1.pop(x)
                                enemyboard1.insert(x, "1")
                        case 2:
                            if enemyboard2[x] != "1":
                                enemyboard2.pop(x)
                                enemyboard2.insert(x, "1")
                            else:
                                while enemyboard2[x] == "1":
                                    x = x - 1
                                    if x == -1:
                                        x = 3
                                enemyboard2.pop(x)
                                enemyboard2.insert(x, "1")
                        case 3:
                            if enemyboard3[x] != "1":
                                enemyboard3.pop(x)
                                enemyboard3.insert(x, "1")
                            else:
                                while enemyboard3[x] == "1":
                                    x = x - 1
                                    if x == -1:
                                        x = 3
                                enemyboard3.pop(x)
                                enemyboard3.insert(x, "1")
                        case 4:
                            if enemyboard4[x] != "1":
                                enemyboard4.pop(x)
                                enemyboard4.insert(x, "1")
                            else:
                                while enemyboard4[x] == "1":
                                    x = x - 1
                                    if x == -1:
                                        x = 3
                            enemyboard4.pop(x)
                            enemyboard4.insert(x, "1")
                    print("Your current board is")
                    print(board1)
                    print(board2)
                    print(board3)
                    print(board4)
    if x != "QUIT" and y != "QUIT":
        score = 0
        enemyscore = 0
        targetx = ""
        targety = ""
        while not score == 4 or enemyscore == 4:
            if targetx != "QUIT" and targety != "QUIT":
                targetx = input("What is the x coordinate of the space you would like to target? ")
                if targetx != "QUIT":
                    targetx = int(targetx)
                    targetx = targetx - 1
                    targety = input("What is the y coordinate of the space you would like to target? ")
                    if targety != "QUIT":
                        targety = int(targety)
                        match targety:
                            case 1:
                                if enemyboard1[targetx] == "1":
                                    enemyboard1.pop(targetx)
                                    enemyboard1.insert(targetx, "!")
                                    print("Hit")
                                    score = score + 1
                                else:
                                    enemyboard1.pop(targetx)
                                    enemyboard1.insert(targetx, 0)
                                    print("Miss")
                            case 2:
                                if enemyboard2[targetx] == "1":
                                    enemyboard2.pop(targetx)
                                    enemyboard2.insert(targetx, "!")
                                    print("Hit")
                                    score = score + 1
                                else:
                                    enemyboard2.pop(targetx)
                                    enemyboard2.insert(targetx, 0)
                                    print("Miss")
                            case 3:
                                if enemyboard3[targetx] == "1":
                                    enemyboard3.pop(targetx)
                                    enemyboard3.insert(targetx, "!")
                                    print("Hit")
                                    score = score + 1
                                else:
                                    enemyboard3.pop(targetx)
                                    enemyboard3.insert(targetx, 0)
                                    print("Miss")
                            case 4:
                                if enemyboard4[targetx] == "1":
                                    enemyboard4.pop(targetx)
                                    enemyboard4.insert(targetx, "!")
                                    print("Hit")
                                    score = score + 1
                                else:
                                    enemyboard4.pop(targetx)
                                    enemyboard4.insert(targetx, 0)
                                    print("Miss")
                        print("Your board is:")
                        print(board1)
                        print(board2)
                        print(board3)
                        print(board4)
                        proceed = input("Press enter to continue")
                        targetx = randint(0,3)
                        targety = randint(0,3)
                        match targety:
                            case 0:
                                if board1[targetx] == "1":
                                    board1.pop(targetx)
                                    board1.insert(targetx, "!")
                                    print("You've been hit!!!")
                                    enemyscore = enemyscore + 1
                                else:
                                    board1.pop(targetx)
                                    board1.insert(targetx, 0)
                                    print("You've been missed :v)")
                            case 1:
                                if board2[targetx] == "1":
                                    board2.pop(targetx)
                                    board2.insert(targetx, "!")
                                    print("You've been hit!!!")
                                    enemyscore = enemyscore + 1
                                else:
                                    enemyboard2.pop(targetx)
                                    enemyboard2.insert(targetx, 0)
                                    print("You've been missed :v)")
                            case 2:
                                if board3[targetx] == "1":
                                    board3.pop(targetx)
                                    board3.insert(targetx, "!")
                                    print("You've been hit!!!")
                                    enemyscore = enemyscore + 1
                                else:
                                    board3.pop(targetx)
                                    board3.insert(targetx, 0)
                                    print("You've been missed :v)")
                            case 3:
                                if board4[targetx] == "1":
                                    board4.pop(targetx)
                                    board4.insert(targetx, "!")
                                    print("You've been hit!!!")
                                    enemyscore = enemyscore + 1
                                else:
                                    board4.pop(targetx)
                                    board4.insert(targetx, 0)
                                    print("You've been missed :v)")
                else:
                    score = 4
            else:
                score = 4
def NumberRace(target):
    MaxInput = target // 3
    InputLimit = target / 3
    if MaxInput == InputLimit:
        InputLimit = InputLimit // 4
        MaxInput = MaxInput - InputLimit
    while target > 0:
        print("Input a number between 1 and", MaxInput)
        PInput = int(input(""))
        while PInput > MaxInput or PInput < 0:
            print("Input a number between 1 and", MaxInput)
            PInput = int(input(""))
        target = target - PInput
        print(target)
        if target > 0:
            if MaxInput >= target - 1 and target > 1:
                AIInput = target - 1
            else:
                AIInput = randint(1, MaxInput)
            target = target - AIInput
            print("The AI inputted", AIInput, "so the total is down to", target)
            print("Make sure you don't leave it at 0!")
        else:
            print("Womp womp wooooooomp!")
        if target < 1:
            print("WINNNNNNNNNNEEEEEEERRRRRRR")
    proceed = input("Press enter to continue")
def StickOrTwist():
    PHand = []
    BHand = []
    def Draw(Hand, num, who):
        for i in range (num):
            deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,]
            drawwhat = randint(1,52)
            drawwhat = drawwhat - 1
            if deck[drawwhat] == 1:
                if who == "Player":
                    print("You drew and ace!!!!!!!")
                    ace = int(input("Would you like it to be 1 or 11? "))
                    while ace != 1 and ace != 11:
                        ace = int(input("Would you like it to be 1 or 11? "))
                else:
                    BTotal = 0
                    for i in range (len(Hand)):
                        BTotal = BTotal + BHand[i]
                    if BTotal <= 10:
                        ace = 11
                    else:
                        ace = 1
                drawwhat = ace
            else:
                drawwhat = deck[drawwhat]
            Hand.append(drawwhat)
        return Hand
    stop = 0
    PHand = Draw(PHand, 2, "Player")
    BHand = Draw(BHand, 2, "Bot")
    player = "twist"
    bot = "twist"
    BotMode = randint(1,3)
    while stop == 0:
        if player != "stick":
            print("Your hand is:")
            PTotal = 0
            for i in range (len(PHand)):
                print(PHand[i])
                PTotal = PTotal + PHand[i]
            print("The total is...", PTotal)
            if PTotal > 21:
                print("You're bust! Game over, AI wins.")
                player = "bust"
                stop = 1
            else:
                player = input("Stick or twist on your next turn? ")
                player = player.lower()
                if player == "twist":
                    PHand = Draw(PHand, 1, "Player")
        if bot != "stick":
            BTotal = 0
            for i in range (len(BHand)):
                BTotal = BTotal + BHand[i]
            if BTotal > 21:
                bot = "bust"
                stop = 1
                print("The bot's gone bust! You win!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                if BotMode == 1:
                    if BTotal < 15:
                        bot = "twist"
                        BHand = Draw(BHand, 1, "Bot")
                    else:
                        bot = "stick"
                elif BotMode == 2:
                    if BTotal < 16:
                        bot = "twist"
                        BHand = Draw(BHand, 1, "Bot")
                    else:
                        bot = "stick"
                else:
                    if BTotal < 18:
                        bot = "twist"
                        BHand = Draw(BHand, 1, "Bot")
                    else:
                        bot = "stick"
        if player == "stick" and bot == "stick":
            stop = 1
            print("You and the bot have decided to stick...")
            print("Your hand is:")
            PTotal = 0
            for i in range (len(PHand)):
                print(PHand[i])
                PTotal = PTotal + PHand[i]
            print("The total is...", PTotal)
            proceed = input("Press enter to proceed")
            print("And the AI has drawn:")
            BTotal = 0
            for i in range (len(BHand)):
                print(BHand[i])
                BTotal = BTotal + BHand[i]
            print("The total is...", BTotal)
            proceed = input("Press enter to proceed")
            if PTotal > BTotal:
                print("You win!")
            elif PTotal < BTotal:
                print("Bot wins...")
                print("Better luck next time")
            else:
                print("DRAW!")
            proceed = input("Press enter to proceed")
def WordScramble():
    words = ["plays", "beach", "hello", "weigh", "petal", "rains", "chair", "doors", "green", "plate", "rates", "diets", "deity", "drink", "odour", "cable", "cabal", "cabin", "dimes", "domes", "eager", "eagle", "hairs", "ichor", "iambs", "maces", "oasis", "trees", "water", "drunk", "drank", "socks", "sweat", "tears", "blood", "mouse", "heart", "loves", "birds", "polar", "train", "sloth", "snows", "earth", "death", "storm", "waves", "winds", "tides", "tools", "phone", "tidal", "seeds", "rocks", "deers", "shock", "spies", "spite", "flame", "raven", "reeds", "reads", "skies", "stars", "stair", "floor", "cloud"]
    word = randint(1,len(words))
    word = word - 1
    word = words[word]
    letters = []
    for i in range (5):
        letters.append(word[i-1])
    newword = []
    for i in range (5):
        letter = randint(1, len(letters))
        letter = letter - 1
        newword.append(letters[letter])
        letters.pop(letter)
    guess = "897!"
    display = ["_", "_", "_", "_", "_"]
    print(newword)
    while guess != word:
        guess = input("Unscramble the word: ")
        for i in range (5):
            if guess[i] == word[i] and display[i] == "_":
                display.pop(i)
                display.insert(i, word[i])
        print(display)
            
def Hangman():
    topic = int(input("Do you want the topic to be animals (1), movies and TV shows (2), countries(3) or random (4)? "))
    if topic == 4:
        topic = randint(1,3)
    match topic:
        case 1:
            possible = ["lion", "sloth", "aligator", "mandrill", "gecko", "gorilla", "bear", "labrador", "snake", "rabbit", "armadillo", "hermit crab", "tazmanian devil", "gila monster", "pterodactyl", "bongo", "ram", "sheep", "butterfly", "giraffe", "rhino", "falcon", "kite", "badger", "lemur", "pengiun", "orca", "elephant", "porcupine", "pig", "crocodile", "locust", "praying mantis", "slow lorris", "pug", "goat", "llama", "alpaca", "beetle", "salamnder", "tardigrade"]
            word = possible[randint(0, 19)]
            print("The topic is animals!")
        case 2:
            possible = ["snow white", "home alone", "big hero 6", "x men", "brother bear", "tarzan", "harry potter", "star wars", "men in black", "minions", "how to train your dragon", "wild kratts", "power rangers", "wizard of oz", "wicked", "star treck", "jurassic park", "wallace and grommit", "spiderman", "mufasa", "titanic", "inside out", "lord of the rings", "toy story", "lilo and stitch", "the santa clause", "atlantis", "trolls", "pokemon", "doctor who", "avatar", "bambi", "aristocats", "fox and the hound", "jurassic world", "beauty and the beast", "the little mermaid", "aladin", "moana", "spyfall", "fan4stic", "X men", "train spotting", "italian job", "shrek"]
            word = possible[randint(0, 19)]
            print("The topic is movies or TV shows!")
        case 3:
            possible = ["america", "mozambique", "kenya", "cambodia", "canada", "mexico", "scotland", "france", "portugal", "india", "england", "ireland", "morocco", "germany", "greece", "italy", "brazil", "el salvador", "guianna", "china", "iran", "saudi arabia", "quatar", "greenland", "iceland", "congo", "south africa", "japan", "north korea", "south korea", "ivory coast", "wales", "turkey", "denmark", "finland", "norway", "australia", "ukraine", "russia", "spain", "lebanon"]
            word = possible[randint(0, 19)]
            print("The topic is countries!")
        case 5:
            word = "fan4stic"
    display = []
    answer = []
    for i in range (len(word)):
        if word[i] == " ":
            display.append(" / ")
            answer.append(" / ")
        else:
            display.append("_")
            answer.append(word[i])
    guesses = 11
    guess = ""
    while guess != word and display != answer and guesses >= 1:
        print(display)
        count = 0
        guess = input("Guess a letter or word: ")
        for i in range (len(display)):
            if guess == answer[i]:
                display.pop(i)
                display.insert(i, guess)
                count = count + 1
        if count == 0 and guess != word:
            guesses = guesses - 1
            print("You have", guesses, "wrong guesses left before you lose")
    if guesses == 0:
        print("Awww, you lose! The answer was", word)
    else:
        print("WE HAVE A WINNER!!!!!!!")
    resume = input()
            
    
while True:
    print(menu)
    game = int(input("Where do you want to go? 1, 2, 3, 4, 5, 6 or 7??? "))
    match game:
        case 1:
            Guesser()
        case 2:
            Fantasy_Name()
        case 3:
            Num_Bomber()
        case 4:
            target = int(input("What number would you like to be the target? Insert a number between 10 and 50 for it: "))
            while target < 10 or target > 50:
                target = int(input("Between 10 and 50. "))
            NumberRace(target)
        case 5:
            StickOrTwist()
        case 6:
            WordScramble()
        case 7:
            Hangman()
import random 
from player import player


def randomNumber(x, y):
    computer = random.randint(x, y) #Generates Random Number

    return computer 

def printMainMenu():
    print("*****Hello Welcome to Guess the Number!*****")
    print(("1. Guess the computers Number"))
    print("2. Have the Computer guess your number")
    print("3. Compete to who guesses number first") #Prints Menu
    print("4.View Statistics")


def playUserGame(number):


    c = 0
    while(True):
        
        try:
            guess = int(input("Enter the random number you would like to guess: "))
            c += 1
            
        except:
            print("The input must be an integer") #Makes Sure input is an integer
            continue

        
        if(guess == number):
            print("\n\nThe number was " + str(number) + ", it took you " + str(c) + " tries to get it right!") #If Number is right code outputs winning message and breaks the loop
            break

        elif(guess > number):
            print("Your Guess was " +str(guess)+ ", the computer's number is less than the number you guessed") #Gives User feedback and lets them know if number is more or less than their guess
            continue


        elif(guess < number):
            print("Your Guess was " +str(guess)+ ", the computer's number is more than the number you guesses") #Gives User feedback and lets them know if number is more or less than their guess
            continue
     

def playComputerGame(userNumber, rangeStart, rangeEnd):
    c = 0

    while(True):

        computerNumber = random.randint(rangeStart, rangeEnd) # Computer Generates Random number in the range
        c += 1

        if(userNumber == computerNumber):
            print("\n\nThe number was " + str(userNumber) + ", it took the computer " +str(c) + " tries to get it right") #Outputs how many tries it took computer
            break

        elif(userNumber < computerNumber):
            rangeEnd = computerNumber - 1 #Edits range so computer slowly narrows done guess pool
            continue
        
        elif(userNumber > computerNumber):
            rangeStart = computerNumber + 1 #Edits range so computer slowly narrows done guess pool
            continue
            
def playAgain():
    
    while(True):

        print("\n\n******Would you Like to Play again? (Y/N)******") #Asks user to play Aain
        choice = input("Enter either 'Y' or 'N': ")

        if(choice != "Y" and choice != "N"):
            print("\n\n******Please enter either 'Y' or 'N'******") #Makes sure input is correct
            continue

        if(choice == "Y"):
            return True #returns true if user wants to play again
        
        else:
            return False #Returns false if user does not want to play again


def versus(user, userNumber, rangeStart, rangeEnd, computerNumber):
    c = 0 
    z = False
    x = 0
    p = False

    while(True):
        
        try:
            guess = int(input("Enter the random number you would like to guess: ")) #Enter user guess
            c += 1
            
        except:
            print("The input must be an integer") #Makes sure guess is of int type
            continue

        
        if(guess == computerNumber):
            z = True #If guess is right z is labeled true, which is used later 

        elif(guess > computerNumber):
            print("\nUser Guess was " +str(guess)+ ", the computer's number is less than the number you guessed") #Output message to know if guess is lower or higher than number
            


        elif(guess < computerNumber):
            print("\nUser Guess was " +str(guess)+ ", the computer's number is more than the number you guesses") #Output message to know if guess is lower or higher than number

        
        computerGuess = random.randint(rangeStart, rangeEnd) #Computer guesses number
        x += 1

        if(userNumber == computerGuess):
            p = True #If guess is right p is labeled true, which is used later 

        elif(userNumber < computerGuess):
            print("\nComputer Guess was " +str(computerGuess) + " the user's number is less than the computer guess\n")  #Output message to know if guess is lower or higher than number
            rangeEnd = computerGuess - 1
            
        
        elif(userNumber > computerGuess):
            print("\nComputer Guess was " +str(computerGuess) + " the user's number is more than the computer guess\n") #Output message to know if guess is lower or higher than number
            rangeStart = computerGuess + 1
            
        if(z == True and p == True):
            print("It is a tie!!! Both took " +str(c) + " guesses to get the right number!!!") #Prints if it is a tie 
            user.addTies() 
            break

        elif(z == True):
            print("\n\n*********The User Wins!!!!! The number was " + str(computerNumber) + ", it took you " + str(c) + " tries to get it right!*********") #Prints if it is a user win
            user.addWins()
            break

        elif(p == True):
             print("\n\n*******The Computer Wins!!! The number was  " + str(userNumber) + ", it took the computer " +str(x) + " tries to get it right*********") #Prints if it is a computer win
             user.addLosses()
             break


        


        input("Press enter to go into the next round: ")

playerList = []


f = open("players.txt", "r")

players = f.readline()
players = f.readline()

while(players != ""):

    split = players.split(",")
    
    load = player(split[0], split[1], split[2], split[3]) #Reads through file and initializes data in instances of player class

    playerList.append(load) #Adds instances of the classes in a list to be able to iterate through

    players = f.readline()

f.close()

user = playerList[0]



while(True):
    print("Would you Like to load or add a new Game?")
    print("1. Load\n2.New")

    try:
        choice = int(input("Enter your Choice: "))

        if(choice != 1 and choice != 2): 
            print("\n\n******Please enter either 1 or 2*******") #Load or create New game depending on new 
            continue
    except:
        print("Choice must be of integer type") #Error Checks
        continue

    if(choice == 1):
        name = input("\n\nPlease enter your name: ")   #Enter name  
        b = False

        for i in playerList:
            if(name == i.getName()):
                print("Welcome " +i.getName() + "!!!!") #Welcome Message
                user = i
                b = True
                break 

        if b == False:
            print("Your Name is not in the saved games") 
            print("Enter another name or start new game")
            continue

        if b == True:
            break
        
    elif(choice == 2):
        name = input("\n\nPlease enter your name: ")   
        b = False

        for i in playerList:
            if(name == i.getName()):
                print("\n******Name Already Exists, either load game or enter in a different Name*********") #MAkes sure know duplicate answers
                b = True
                break

        if (b == True):
            continue

        user = player(name, 0, 0, 0) #Makes new player instance

        playerList.append(user) #adds to a list

        break
            


while(True):

    try:

        printMainMenu() #calls print menu song
        
        choice = int(input("Enter your Choice: "))
        
        if(choice != 1 and choice != 2 and choice !=3):
            if(choice != 4):
                print("/n/n*****Please enter either 1, 2, 3 or 4*****") #makes sure choice is either 1, 2, 3, 4
                continue
            

    except: 
        print("\n\n******Enter an int, and make sure it is either 1 2, 3, 4******")
        continue


    if(choice == 1):

        while(True):
    
            try:
                rangeStart = int(input('\nEnter your the start range of the numbers: '))
                rangeEnd = int(input("\nEnter the end range of the number: "))  #Enter range of numbers computer has to generate the random number

                if(rangeStart > rangeEnd):
                    print("\n\n******Range Start must be before the range end******")
                    continue

                computerNumber = randomNumber(rangeStart, rangeEnd)
                break

            except: 
                print("Please enter an int type for the range")
                continue
        

        playUserGame(computerNumber) #calls computer game function
    
        x = playAgain() #calls playAgain function to determine if the loop with continue or end the program

        if(x == True):
            continue

        else:
            break 
    
    elif(choice == 2):

        while(True):

            try:
                userNumber = int(input("\nEnter the number random number you would like the computer to guess: "))
                rangeStart = int(input('\nEnter your the start range of the numbers: ')) #Enter number for the computer to try to guess, and then make sure the number is within the range
                rangeEnd = int(input("\nEnter the end range of the number: "))

                if(rangeStart > rangeEnd):
                    print("\n\n******Range Start must be before the range end******")
                    continue
                
                if(userNumber <= rangeStart or userNumber >= rangeEnd):
                    print("\n\n******User number must be in between the start and end range*****")
                    continue
            
            except:
                print("*******Input Must be an Integer******")
                continue

            playComputerGame(userNumber, rangeStart, rangeEnd) #calls computer game 
            break
    
        
        x = playAgain() # play again function called, returns boolean if game should continue or not

        if(x == True):
            continue

        else:
            break 

        
    elif(choice == 3):
         
         
        try:
            userNumber = int(input("\nEnter the number random number you would like the computer to guess: "))
            rangeStart = int(input('\nEnter your the start range of the numbers: '))
            rangeEnd = int(input("\nEnter the end range of the number: ")) #Same as above, enter computer guess number along with the end and start range

            if(rangeStart > rangeEnd):
                print("\n\n******Range Start must be before the range end******")
                continue
                
            if(userNumber < rangeStart or userNumber > rangeEnd):
                print("\n\n******User number must be in between the start and end range*****")
                continue
            
        except:
            print("*******Input Must be an Integer******")
            continue 

        computerNumber = random.randint(rangeStart, rangeEnd) #gets random computer number

        versus(user, userNumber, rangeStart, rangeEnd, computerNumber) # calls versus function


        x = playAgain() #play again function as before

        if(x == True):
            continue

        else:
            break

    elif(choice == 4):

        print("What Do you want to see?")
        print("1.Most Wins\n2.Most Losses\n3.Most Ties\n4.Games Played")
        while(True):
            try:
                
                choice = int(input("Enter your Choice: "))
                
                if(choice != 1 and choice != 2 and choice != 3): 
                    if(choice != 4):
                        print("\n\n******Please enter either 1, 2, 3, 4*******") #Takes user integer input, makes sure it is between 1-4 and of type int
                        continue

                break
            
            except:
                print("Choice must be of integer type")
                continue

        if(choice == 1):

            winsLeader = [] #winsLeader list

            c = 0 

            for i in playerList:

                if c == 0:
                    winsLeader.append(i) #if the first loop, automatically adds the first player in the list
                    c = 1
                    continue

                if(i.getWins() > winsLeader[0].getWins()): #If wins in this instance is greater than the last, it clears the list, then appends the new leader to the list
                    winsLeader.clear()
                    winsLeader[0] = i

                elif(i.getWins() == winsLeader[0].getWins()): #If wins in this instance of loop is equal, it appends the wins to the end of the list and now has both
                    winsLeader.append(i)


            for i in winsLeader:
                print("\nName: " +i.getName() + "\tTotal Wins: " +str(i.getWins())) #Prints everything in the list

        elif(choice == 2):

            lossLeader = []

            c = 0 

            for i in playerList:

                if c == 0:
                    lossLeader.append(i)
                    c = 1
                    continue

                if(i.getLosses() > lossLeader[0].getLosses()): #Same thing as wins function, just with losses
                    lossLeader.clear()
                    lossLeader.append(i)

                elif(i.getLosses() == lossLeader[0].getLosses()):
                    lossLeader.append(i)


            for i in lossLeader:
                print("\nName: " +i.getName() + "\tTotal Losses: " +str(i.getLosses()))

        
        elif(choice == 3):

            tieLeader = []

            c = 0 

            for i in playerList:

                if c == 0:
                    tieLeader.append(i)
                    c = 1
                    continue

                if(i.getTies() > tieLeader[0].getTies()): # Same thing as losses/wins function just with ties
                    tieLeader.clear()
                    tieLeader.append(i)

                elif(i.getTies() == tieLeader[0].getTies()):
                    tieLeader.append(i)


            for i in tieLeader:
                print("\nName: " +i.getName() + "\tTotal Ties: " +str(i.getTies()))

        elif(choice == 4):

            print()
    
            for i in playerList:
                totalGames = i.getLosses() + i.getWins() + i.getTies()
                print(i.getName()+ " has played " +str(totalGames)+ "!!!!!") #Prints the total games played for everyone in the text file



               

                



f = open("players.txt", "w")

f.write("Player,Wins,Losses,Ties\n") #Writes all data in a file at end of program to be used for later

for i in playerList:
    f.write(i.getName()+","+str(i.getWins())+","+str(i.getLosses())+","+str(i.getTies()) +"\n")

f.close()

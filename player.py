class player:

    def __init__(self, player, wins, losses, ties):
        self.__player = player
        self.__wins = int(wins) 
        self.__losses = int(losses)
        self.__ties = int(ties) 

    def getName(self):
        return self.__player

    def getWins(self):
        return self.__wins

    def getLosses(self):
        return self.__losses

    def getTies(self):
        return self.__ties


    def addWins(self):
        self.__wins += 1

    def addLosses(self):
        self.__losses += 1

    def addTies(self):
        self.__ties += 1
    



        
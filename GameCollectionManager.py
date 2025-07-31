#A game collection manager made for Introduction to Python
#By Spencer Lowe
import os

#Creates a blank list of games to be stored and organized for viewing.
Games = []
#Creation of the Game Class.
class Game:
    #Game class initialization function with name, releaseDate, platform, rating, playtime and notes arguments and are set to the sent values.
    def __init__ (self, name, releaseDate, platform, rating, playtime, notes):
        self.name = name
        self.releaseDate = releaseDate
        self.platform = platform
        self.rating = rating
        self.playtime = playtime
        self.notes = notes

    #GetGame function of the class that prints and returns the data of the sent Game object.
    def GetGame(self):
        line = self.name + "," + str(self.releaseDate) + "," + self.platform + "," + str(self.rating) + "," + str(self.playtime) + "," + self.notes
        print(line)
        return line

#ConvertToInt function with the value argument.
def ConvertToInt(value):
    #The function attempts to return value as an int, if it cannot, an error is thrown and the value is returned as it was.
    try:
        return int(value)
    except(ValueError, TypeError):
        return value


#Creates and checks for the existence of a file.
filepath = os.getcwd() + "\\myCollection.txt"
if os.path.exists(filepath):
    #If that file does exist, the user is told that a collection has been found and an answer string variable is created.
    print("Collection found!")
    answer = ""
    while True:
        #So long as the answer to the following text box is not yes or no, the question will be repeated.
        if(answer != "Yes" and answer != "No" and answer != "yes" and answer != "no"):
            answer = input("Would you like to open this collection? ")
        #If the answer to the previous question is yes, the detected file is opened.
        elif(answer == "Yes" or answer == "yes"):
            file = open(filepath, 'r')
            print("Your collection has been loaded.")
            #The file is read line by line and each line is split by the seperator and added as attributes to Game objects.
            fileLines = file.readlines()
            for line in fileLines:
                cleanedline = line.split(",")
                newGame = Game(cleanedline[0], int(cleanedline[1]), cleanedline[2], int(cleanedline[3]), int(cleanedline[4]), cleanedline[5])
                Games.append(newGame)
            break
        else:
            #If the answer is no, a new collection is created.
            print("New collection will be created.")
            Games = []
            break
else:
    #If no file is found, a new one is created.
    print("No collection was found. A new one will be created.")
    file = open(filepath, "w")

#The options choice variable is reset to 0.
options = int(0)
while True:
    #If the options variable is outside intended range, the instructions are repeated until the user inputs a valid option.
    if type(options) is str or options <= 0 or options > 4:
        options = input("\nIf you would like to create a new collection, type 1.\nIf you would like to append the current collection, press 2.\nIf you would like to view your collection, press 3.\nTo exit, press 4.\n")
        options = ConvertToInt(options)
    #If the first option is chosen, a new collection is created and the options variable is reset.
    elif options == 1:
        print("New collection created.")
        Games = []
        options = 0
    #If the second option is chosen, the player is asked to assign name, releaseDate, platform, rating, playtime and notes for a new Game object.
    elif options == 2:
        print("Altering current collection.")
        newgame = None
        name = input("Enter the name of the game you want to add: ")
        releaseDate = input("Enter the release year of the game: ")
        releaseDate = ConvertToInt(releaseDate)
        #If the releaseDate is incorrect, a new one is requested.
        while True:
            if(type(releaseDate) is str or releaseDate < 1950 or releaseDate > 2025):
                print("Release date is not valid.")
                releaseDate = ConvertToInt(input("Please reenter your release date: "))
            else:
                break
        releaseDate = int(releaseDate)
        platform = input("Enter the platform you own this game on: ")
        rating = input("Enter the rating you would give this game: ")
        rating = ConvertToInt(rating)
        #If the rating is incorrect, a new one is requested.
        while True:
            if(type(rating) is str or rating < 0 or rating > 10):
                print("Rating is not valid.")
                rating = ConvertToInt(input("Please reenter your rating: "))
            else:
                break
        playtime = input("Enter the amount of time (in hours) that you played the game: ")
        playtime = ConvertToInt(playtime)
        #If the playtime is incorrect, a new one is requested.
        while True:
            if(type(playtime) is str or playtime < 0):
                print("Playtime is not valid.")
                playtime = ConvertToInt(input("Please reenter your playtime: "))
            else:
                break
        notes = input("Enter any additional notes you have on the game: ")
        #The inputs are used to initialize a new Game object, which is then added to the Games list and the options variable is reset.
        newGame = Game(name, releaseDate, platform, rating, playtime, notes)
        Games.append(newGame)
        options = 0
    #If the third option is selected, a second set of options is presented.
    elif options == 3:
        print("How would you like to sort your collection?")
        sortOption = int(0)
        sortedGames = []
        while True:
            #If no option has been selected or the sortOption variable is outside of its range, the options are presented again.
            if(type(sortOption) is str or sortOption <= 0 or sortOption > 5):
                sortOption = input("1: By Name\n2: By Release Year\n3: By Platform\n4: By Rating\n5: By Playtime\n")
                sortOption = ConvertToInt(sortOption)
            #If the first option is selected, the Games list is sorted by name.
            elif(sortOption == 1):
                sortedGames = sorted(Games, key=lambda p:p.name)
                break
            #If the second option is selected, the Games list is sorted by releaseDate.
            elif(sortOption == 2):
                sortedGames = sorted(Games, key=lambda p:p.releaseDate)
                break
            #If the third option is selected, the Games list is sorted by platform.
            elif(sortOption == 3):
                sortedGames = sorted(Games, key=lambda p:p.platform)
                break
            #If the fourth option is selected, the Games list is sorted by rating in reverse.
            elif(sortOption == 4):
                sortedGames = sorted(Games, key=lambda p:p.rating, reverse = True)
                break
            #If the fifth option is selected, the Games list is sorted by playtime in reverse.
            elif(sortOption == 5):
                sortedGames = sorted(Games, key=lambda p:p.playtime, reverse = True)
                break
            print("Viewing current collection.")
        #The new sorted games list has each of its Games call their respective GetGame functions, then options is reset.
        for Game in sortedGames:
            Game.GetGame()
        options = 0      
    #If the fourth option is selected and the user has not previously loaded a collection.
    elif options == 4:
        print("Saving your collection.")
        if answer != "Yes" or answer != "yes":
            file = open(filepath, "w")
        #The current collection of games is written to the file line by line and the file is closed and the while loop is broken.
        for Game in Games:
            file.writelines(Game.GetGame())
        file.close()
        break
#A game collection manager made for Introduction to Python
#By Spencer Lowe
import os

Games = []
class Game:
    def __init__ (self, name, releaseDate, platform, rating, playtime, notes):
        self.name = name
        while True:
                if releaseDate >= 1950 & releaseDate <= 2025:
                    self.releaseDate = releaseDate
                    break
                else:
                    print("Release date is not valid.")
                    releaseDate = input("Please reenter your release date: ")
        self.platform = platform
        while True:
            if rating >= 0 & rating <= 10:
                self.rating = rating
                break
            else:
                print("Rating is not valid.")
                rating = input("Please reenter your rating: ")
        self.playtime = playtime
        self.notes = notes

    def GetGame(self):
        line = self.name + "," + str(self.releaseDate) + "," + self.platform + "," + str(self.rating) + "," + self.playtime + "," + self.notes
        print(line)
        return line

filepath = os.getcwd() + "\\myCollection.txt"
if os.path.exists(filepath):
    print("Collection found!")
    answer = ""
    while True:
        if(answer != "Yes" and answer != "No" and answer != "yes" and answer != "no"):
            answer = input("Would you like to open this collection? ")
        elif(answer == "Yes" or answer == "yes"):
            file = open(filepath, 'r')
            print("Your collection has been loaded.")
            fileLines = file.readlines()
            for line in fileLines:
                #file.readline(line)
                cleanedline = line.split(",")
                newGame = Game(cleanedline[0], int(cleanedline[1]), cleanedline[2], int(cleanedline[3]), cleanedline[4], cleanedline[5])
                Games.append(newGame)
            break
        else:
            print("New collection will be created.")
            break
else:
    print("No collection was found. A new one will be created.")
    file = open(filepath, "w")

options = int(0)
while True:
    if options <= 0:
        options = input("If you would like to create a new collection, type 1. If you would like to append the current collection, press 2. If you would like to view your collection, press 3. To exit, press 4.")
        options = int(options)
    elif options == 1:
        print("New collection created.")
        Games = []
        options = 0
    elif options == 2:
        print("Altering current collection.")
        name = input("Enter the name of the game you want to add: ")
        releaseDate = input("Enter the release year of the game: ")
        releaseDate = int(releaseDate)
        platform = input("Enter the platform you own this game on: ")
        rating = input("Enter the rating you would give this game: ")
        rating = int(rating)
        playtime = input("Enter the amount of time (in hours) that you played the game: ")
        notes = input("Enter any additional notes you have on the game: ")
        newGame = Game(name, releaseDate, platform, rating, playtime, notes)
        Games.append(newGame)
        options = 0
    elif options == 3:
        print("Viewing current collection.")
        sortedGames = sorted(Games, key=lambda p:p.name)
        for Game in sortedGames:
            Game.GetGame()
        options = 0
    elif options == 4:
        print("Saving your collection.")
        if answer != "Yes" or answer != "yes":
            file = open(filepath, "w")
        for Game in Games:
            file.write(Game.GetGame())
        file.close()
        break
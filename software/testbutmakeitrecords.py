import csv


class Game():
    def __init__(self, gameTitle, genre, ageRating, platform):
       self.gameTitle = gameTitle
       self.genre = genre
       self.ageRating = ageRating
       self.platform = platform


# Function to read data from CSV file into paralel arrays
def readGameDataFromCSV():
    games = []
    with open("software/gamesExtended.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            newgame = Game(row[0], row[1], int(row[2]), row[3])
            games.append(newgame)
    return games


# Procedure to count amount of games in specific genre that are suitable for under 18yrs
def countSuitableGames(games, genre_to_check):
    count = 0
    for x in range(len(games)):
       if games[x].genre == genre_to_check and games[x].ageRating <18: # Checks if the position has the correct genre and if its suitable for under 18yrs
          print(games[x].gameTitle)
          count = count + 1
    print("total games with " + genre_to_check + " genre is: " + str(count))


# Procedure to write names of games from specific genre that are suitable for under 18yrs to a txt file and show the platform they can be played on
def countSuitableGamesPlatform(games, genre_to_check, platform_to_check):
    count = 0
    with open("software/platform_suitable_games.txt", "w") as file:
        for x in range(len(games)):
            if games[x].genre == genre_to_check and games[x].ageRating <18 and games[x].platform == platform_to_check:
               count = count + 1
               file.write(games[x].gameTitle + " - " + games[x].platform)
               file.write("\n")
    print("total games in " + genre_to_check + " genre that are available on " + platform_to_check + " is: " + str(count))            


#main
games = readGameDataFromCSV()
genre_to_check = "Fantasy"
platform_to_check = "PC"
countSuitableGames(games, genre_to_check)
countSuitableGamesPlatform(games, genre_to_check, platform_to_check)
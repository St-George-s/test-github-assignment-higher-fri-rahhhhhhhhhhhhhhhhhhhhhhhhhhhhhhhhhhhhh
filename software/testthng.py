import csv

genre_to_check = input("genre to check: ")


# Function to read data from CSV file into paralel arrays
def readGameDataFromCSV():
    with open("software/gamesExtended.csv", "r") as file:
     gameTitles = []
     genres = []
     ageRatings = []
     platform = []
     reader = csv.reader(file)
     for row in reader:
        gameTitles.append(row[0])
        genres.append(row[1])
        ageRatings.append(int(row[2]))
        platform.append(row[3])

     return gameTitles, genres, ageRatings, platform


# Procedure to count amount of games in specific genre that are suitable for under 18yrs
def CountSuitableGames(gameTitles, genres, ageRatings, genre_to_check, platform):
    count = 0
    for x in range(len(gameTitles)):
       if genres[x] == genre_to_check and ageRatings[x] <18: # Checks if the position has the correct genre and if its suitable for under 18yrs
          print(gameTitles[x])
          count = count + 1
    print(count)


# Procedure to write names of games from specific genre that are suitable for under 18yrs to a txt file and show the platform they can be played on
def CountSuitableGamesPlatform(gameTitles, genres, ageRatings, genre_to_check, platform):
    count = 0
    with open("software/platform_suitable_games.txt", "w") as file:
        for x in range(len(gameTitles)):
            if genres[x] == genre_to_check and ageRatings[x] <18:
               file.write(gameTitles[x] + " - " + platform[x])
               file.write("\n")

               
#main
globalgameTitles, globalgenres, globalageRatings, globalplatform = readGameDataFromCSV()
CountSuitableGames(globalgameTitles, globalgenres, globalageRatings, genre_to_check, globalplatform)
CountSuitableGamesPlatform(globalgameTitles, globalgenres, globalageRatings, genre_to_check, globalplatform)
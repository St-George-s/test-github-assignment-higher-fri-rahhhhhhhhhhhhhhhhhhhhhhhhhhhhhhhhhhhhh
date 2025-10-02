import csv

genre_to_check = input("genre to check: ")


# Function to read data from CSV file into paralel arrays
def readGameDataFromCSV():
    with open("software/games.csv", "r") as file:
     gameTitles = []
     genres = []
     ageRatings = []
     reader = csv.reader(file)
     for row in reader:
        gameTitles.append(row[0])
        genres.append(row[1])
        ageRatings.append(int(row[2]))

     return gameTitles, genres, ageRatings


# Procedure to count amount of games in specific genre that are suitable for under 18yrs
def CountSuitableGames(gameTitles, genres, ageRatings, genre_to_check):
    count = 0
    for x in range(len(gameTitles)):
       if genres[x] == genre_to_check and ageRatings[x] <18: # Checks if the position has the correct genre and if its suitable for under 18yrs
          print(gameTitles[x])
          count = count + 1
    print(count)


#main
globalgameTitles, globalgenres, globalageRatings= readGameDataFromCSV()
CountSuitableGames(globalgameTitles, globalgenres, globalageRatings, genre_to_check)

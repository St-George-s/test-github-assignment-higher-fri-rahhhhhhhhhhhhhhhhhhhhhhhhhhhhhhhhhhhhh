class Sighting():
    def __init__(self, town, mammal, date, age):
        self.town = town
        self.mammal = mammal
        self.date = date
        self.age = age


def readDataFromTXT():
    sightings = []
    with open("software/mammals.txt", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            newsighting = Sighting(row[0], row[1], row[2], int(row[3]))
            sightings.append(newsighting)
    return sightings


def findOldestWalker(sightings):
     
    maximumValue = age[0]
    for counter in range(len(age)):
        if age[counter] > maximumValue: 
            maximumValue = age[counter]          
    
         



def findMammalDatesTown():



def countSightingDates():
    count = 0
import csv

# function to read the CSV file into parallel arrays
def getdata():
    with open("software/parallel arrays/athletes.csv", "r") as file:
         entryID=[]
         location=[]
         forename=[]
         surname=[]
         jumps=[]
         reader = csv.reader(file)
         for row in reader:
              entryID.append(row[0])
              location.append(row[1])
              forename.append(row[2])
              surname.append(row[3])
              jumps.append(int(row[4]))
    return entryID, location, forename, surname, jumps


def genbibvalue(entryID, location, forename, surname):
    with open("software/parallel arrays/bibValues.csv", "w") as file:
        writer = csv.writer(file)
        for x in range(30):
            bibValue = forename[x][0] + surname[x] + str(ord(location[x][0]))
            file.write(entryID[x] + " " + bibValue)
            file.write("\n")

#funtion to find the highest number of jumps that was achieved
def maxjump(jumps):
    maxJumps = jumps[0]
    for x in range(1, len(jumps)):
        if jumps[x] > maxJumps:
            maxJumps = jumps[x]
    return maxJumps

#procedure to find and display the names of the athletes who have the highest number of jumps
def findmaxjumpers(maxJumps, forename, surname, jumps):
    for x in range (len(jumps)):
        if jumps[x] == maxJumps:
            print(forename[x] + " " + surname[x])

#main
entryID, location, forename, surname, jumps = getdata()
genbibvalue(entryID, location, forename, surname)
maxJumps = maxjump(jumps)
findmaxjumpers(maxJumps, forename, surname, jumps)
import csv


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
    pass


def maxjump(jumps):
    maxJumps = jumps[0]
    for x in range(1, len(jumps)):
        if jumps[x] > maxJumps:
            maxJumps = jumps[x]
    return maxJumps


def findmaxjumpers(maxJumps, forename, surname, jumps):
    for x in range (len(jumps)):
        if jumps[x] == maxJumps:
            print(forename[x] + " " + surname[x])


entryID, location, forename, surname, jumps = getdata()
genbibvalue(entryID, location, forename, surname)
maxJumps = maxjump(jumps)
findmaxjumpers(maxJumps, forename, surname, jumps)
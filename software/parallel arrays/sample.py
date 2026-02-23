import csv

#function to read the CSV file into parallel arrays
def getData():
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
              jumps.append(int(row[4])) #assigns each row of the CSV file into a paralell array
    return entryID, location, forename, surname, jumps

# Gnerate bib values and write to new file
def generateBibValue(entryID, location, forename, surname):
    with open("software/parallel arrays/bibValues.csv", "w") as file:
         for x in range(len(entryID)):
            #takes first letter from forename, the surname and the ascii value of the first letter of the location to create the bib value
            bibValue = forename[x][0] + surname[x] + str(ord(location[x][0])) 
            file.write(entryID[x] + " " + bibValue)
            file.write("\n")

#funtion to find the highest number of jumps that was achieved
def findMaxJump(jumps):
    maxJumps = jumps[0]
    for x in range(1, len(jumps)): #
        if jumps[x] > maxJumps:
            maxJumps = jumps[x]
    return maxJumps

#procedure to find and display the names of the athletes who have the highest number of jumps
def findMaxJumpers(maxJumps, forename, surname, jumps):
    for x in range (len(jumps)):
        if jumps[x] == maxJumps:
            print(forename[x] + " " + surname[x])

# COMMENT HERE
def findNumFinalists(location):
    invCount = 0
    kirCount = 0
    coaCount = 0
    motCount = 0
    for x in range(len(location)):
        if location[x] == "Inverness":
            invCount +=1
        elif location[x] == "Kirkcaldy":
            kirCount +=1
        elif location[x] == "Coatbridge":
            coaCount +=1
        elif location[x] == "Motherwell":
            motCount +=1
    print("Inverness has " + str(invCount) + " finalists.")
    print("Kirkcaldy has " + str(kirCount) + " finalists.")
    print("Coatbridge has " + str(coaCount) + " finalists.")
    print("Motherwell has " + str(motCount) + " finalists.")

#main
# entryID, location, forename, surname, jumps = getdata()
# genbibvalue(entryID, location, forename, surname)
# maxJumps = maxjump(jumps)
# findmaxjumpers(maxJumps, forename, surname, jumps)
# findnumfinalists(location)

findMaxJump([100,87,102,108,95])
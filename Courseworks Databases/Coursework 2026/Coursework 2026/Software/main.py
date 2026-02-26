import csv

# procedure to read csv file into paralel arrays
def readFile():
    #opens csv file in read mode
    with open("Courseworks Databases/Coursework 2026/Coursework 2026/Software/tools.csv", "r") as file:
          tool=[]
          manufacturer=[]
          dateRented=[]
          returned=[]
          fee=[]
          reader = csv.reader(file)
          for row in reader:
               tool.append(row[0])
               manufacturer.append(row[1])
               dateRented.append(row[2])
               returned.append(row[3])
               fee.append(int(row[4]))

    return tool, manufacturer, dateRented, returned, fee


def findManufactureTools(tool, manufacturer): 
     chosenManufacturer = "BrownTech"
     count = 0
     for x in range(len(manufacturer)):
          if manufacturer[x] == chosenManufacturer:
               print(tool[x])
               count += 1
     print("total number of tools from "+ chosenManufacturer + " is: " + str(count))

# function to calculate late fees for tools rented in 2025 and not returned
def calcuLateFee(dateRented, returned, fee):
     for x in range(len(dateRented)):
          if dateRented[x][-4:] == "2025" and returned[x] == "No":
               if int(dateRented[x][3:5]) <= 6:
                    fee[x] += 10
               else:
                    fee[x] += 5
     return fee

# write tool name, date rented, and fee amount of tools with a late fee to an external file
def writeLateTools(tool, dateRented, fee):
    with open("Courseworks Databases/Coursework 2026/Coursework 2026/Software/lateTools.csv", "w") as file:
        for x in range(len(tool)):
          if fee[x] != 0:
            file.write(tool[x] + ", " + dateRented[x] + ", " + str(fee[x]))
            file.write("\n")

#main
tool, manufacturer, dateRented, returned, fee = readFile()
findManufactureTools(tool, manufacturer)
calcuLateFee(dateRented, returned, fee)
writeLateTools(tool, dateRented, fee)
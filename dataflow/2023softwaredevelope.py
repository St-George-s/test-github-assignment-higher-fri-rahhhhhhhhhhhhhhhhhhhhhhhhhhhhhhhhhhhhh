import csv

#function to read csv file into paralell arrays 
def readfile():
    with open("dataflow/attractions.csv", "r") as file:
        attraction=[]
        category=[]
        visitors=[]
        daysOpen=[]
        height=[]
        reader = csv.reader(file)
        for row in reader:
            attraction.append(row[0])
            category.append(row[1])
            visitors.append(int(row[2]))
            daysOpen.append(int(row[3]))
            height.append(row[4])
        return attraction, category, visitors, daysOpen, height


# procedure to find the attractions with most/least amount of visitors
def leastmostattract(attraction, visitors):
    leastVisited = 0
    mostVisited = 0
    for x in range(1, len(visitors)):
        if visitors[x] < visitors[leastVisited]:
            leastVisited = x
        if visitors[x] > visitors[mostVisited]:
            mostVisited = x
    print("the most visited attraction is: " + attraction[mostVisited])
    print("the least visited attraction is: " + attraction[leastVisited])


#procedure to write names of attractions that need service to a csv file
def needservice(attraction, category, daysOpen):
    with open("dataflow/service.csv", "w") as file:
        writer = csv.writer(file)
        for x in range(len(category)):
          if category[x] == "Roller Coaster":
              days = daysOpen[x] % 90 
              if (90-days) <= 7: # check if 7 or less days until repair needed
                  writer.writerow([attraction[x]])
                  

#main program
globalattraction, globalcategory, globalvisitors, globaldaysopen, globalheight = readfile()
leastmostattract(globalattraction, globalvisitors)
needservice(globalattraction, globalcategory, globaldaysopen)
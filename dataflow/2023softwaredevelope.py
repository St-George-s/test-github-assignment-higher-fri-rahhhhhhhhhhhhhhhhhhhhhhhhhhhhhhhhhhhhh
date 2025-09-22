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
    leasvisited = 0
    mostvisited = 0
    for x in range(len(visitors)):
        if visitors[x] < visitors[leasvisited]:
            leasvisited = x
        if visitors[x] > visitors[mostvisited]:
            mostvisited = x
    print("the most visited attraction is: " + attraction[mostvisited])
    print("the least visited attraction is: " + attraction[leasvisited])

def needservice(attraction, category, daysOpen):
    with open("dataflow/service.csv", "w") as file:
        for x in range(len(category)):
          if category[x] == "Roller Coaster":
              days = daysOpen[x] % 90
              if (90-days) <= 7:
                  file.write(attraction[x])
                  
                  
              

    


#main program
globalattraction, globalcategory, globalvisitors, globaldaysopen, globalheight = readfile()
leastmostattract(globalattraction, globalvisitors)
needservice(globalattraction, globalcategory, globaldaysopen)
import csv

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
            visitors.append(row[2])
            daysOpen.append(row[3])
            height.append(row[4])
        return attraction, category, visitors, daysOpen, height
    
def leastmostattract(attraction, visitors):
    mostattract = 

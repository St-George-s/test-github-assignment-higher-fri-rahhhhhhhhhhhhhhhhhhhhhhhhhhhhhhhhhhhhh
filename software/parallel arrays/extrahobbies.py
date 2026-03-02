import csv

# Function to read csv file into parallel arrays 
def readFile():
    # opens csv file into read mode
    with open("software/parallel arrays/Fun_Users.csv", "r") as file:
        name=[] #
        hobby=[]
        pokemon=[]
        fallout=[]
        age=[]
        job=[]
        reader = csv.reader(file) 
        next(reader) #skips header row
        for row in reader: 
            name.append(row[0])
            hobby.append(row[1])
            pokemon.append(row[2])
            fallout.append(row[3])
            age.append(row[4])
            job.append(row[5])
        return pokemon, age, name, hobby, job, fallout

# procedure to count to amount of a pokemon in the pokemon array
def countpokemon(pokemon):
    search = input("What pokemon: ")
    counter = 0
    for x in range(len(pokemon)):
        if search == pokemon[x]:
            counter = counter + 1
    print(counter)

# procedure to find the largest age in the age array and display it
def findOld(age):
    maximumValue = age[0]
    for counter in range(1, len(age)): # check over remaining values in age
        if age[counter] > maximumValue: 
            maximumValue = age[counter] 

    print(f"The largest value was {maximumValue}") 

# proceduere to find the smallest age in the age array and display it
def findYoung(age):
    minimumValue = age[0]
    for counter in range(1, len(age)): # check over remaining values in age
        if age[counter] < minimumValue:
            minimumValue = age[counter] 

    print(f"The smallest value was {minimumValue}") 

# procedure to do a linear search based on a user name and print details for any matches
def findDetails(name, pokemon, age, hobby, job, fallout):
    searchName = input("find details of: ") 
    for x in range(len(name)):
        if searchName == name[x]:
            print(name[x] +" is "+ age[x]+" years old, their job is " +job[x]+", their favourite pokemon is "+pokemon[x]+", their favourite fallout is "+fallout[x]+", and their hobby is " +hobby[x])


#main program
globalPokemon, globalAge, globalName, globalHobby, globalJob, globalFallout=readFile()
#countpokemon(globalpokemon)
findOld(globalAge)
findYoung(globalAge)
findDetails(globalName, globalPokemon, globalAge, globalHobby, globalJob, globalFallout)

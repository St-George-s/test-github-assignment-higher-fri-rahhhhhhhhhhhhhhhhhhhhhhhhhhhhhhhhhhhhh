class Competitor:
    def __init__(self, name, year_group, event, seed_time):
        self.name = name
        self.year_group = year_group
        self.event = event
        self.seed_time = seed_time
c1 = Competitor("Amira", 1, "100m", 14.8)
c2 = Competitor("Beth", 3, "200m", 30.6)
c3 = Competitor("Chloe", 2, "100m", 15.2)
c4 = Competitor("Dina", 4, "200m", 28.9)

print(c1.name)
print(c2.event)
print(c3.seed_time)

c1.seed_time = 14.5
#print(c1.name + " runs " + c1.event + " in " + str(c1.seed_time) +"s")
#print(c4.name + " runs " + c4.event + " in " + str(c4.seed_time) +"s")

competitors =[c1, c2, c3]
#print(competitors)
#print(competitors[0])
#print(competitors[0].event)
competitors.append(c4)

for x in range(len(competitors)):
    print(competitors[x].name + "(Y" + str(competitors[x].year_group) + ") " + competitors[x].event +": "+ str(competitors[x].seed_time)+ "s")

count100=0
for x in range(len(competitors)):
    if(competitors[x].event) == "100m":
        count100 += 1
print("100m entries: "+ str(count100))

fasted100=None
for x in range(len(competitors)):
    if(competitors[x].event) == "100m":
        if fasted100 == None or competitors[x].seed_time < fasted100:
            fasted100 = competitors[x].seed_time
print("fastest 100m speed: " + str(fasted100) +"s")
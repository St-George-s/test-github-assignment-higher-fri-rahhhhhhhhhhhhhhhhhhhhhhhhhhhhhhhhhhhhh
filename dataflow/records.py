class Competitor:
    def __init__(self, name, year_group, event, seed_time):
        self.name = name
        self.year_group = year_group
        self.event = event
        self.seed_time = seed_time
c1 = Competitor("Amira", 1, "100m", 14.8)
c2 = Competitor("Beth", 3, "200m", 30.6)
c3 = Competitor("Chloe", 2, "100m", 15.2)

print(c1.name)
print(c2.event)
print(c3.seed_time)
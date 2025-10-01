class Clubmember:
    def __init__(self, name, year_group, club, permission):
        self.name = name
        self.year_group = year_group
        self.club = club
        self.permission = permission
c1 = Clubmember("Steph", 12, "coding", True)
c2 = Clubmember("Mr Walker", 9, "gaming", False)
c3 = Clubmember("Sahana", 13, "maths", True)
c4 = Clubmember("Lara", 12, "coding", False)

members=[c1, c2, c3, c4]
for x in range(len(members)):
    print(members[x].name + " (Y" + str(members[x].year_group) + ") Club: " + members[x].club +", Permission: "+ str(members[x].permission))
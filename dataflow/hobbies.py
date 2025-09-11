def getusername():
    username=input("give username: ")
    return username

def getage(uname):
    age=input( uname+" enter age: ")
    return age

def gethobbies(uname):
    hobbies=[]
    for x in range(2):
        hobby=input("what hobby: ")
        hobbies.append(hobby)
    return hobbies

def counthobbies(hobbies):
    return len(hobbies) 

def hobbysearch(hobbies):
    searchhobby=input("what hobby to search for: ")
    for x in range(len(hobbies)):
        if searchhobby == hobbies[x]:
            return x



globalusername=getusername()
print(globalusername)
globalage=getage(globalusername)
print(globalage)
globalhobbies=gethobbies(globalusername)
print(globalhobbies)
globalcounthobbies=counthobbies(globalhobbies)
print(globalcounthobbies)
globalhobbysearch=hobbysearch(globalhobbies)
print(globalhobbysearch)
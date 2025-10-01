import csv

#Function to get information of a new member
def newmember(): 
    firstname = input("enter first name: ")
    lastname = input("enter last name: ")
    category= input("Enter category- Junior, adult, senior: ")
    password=input("enter password: ")
    return firstname, lastname, category, password


# procedure to read csv file into paralel arrays
def readdisplayfile(firstname, lastname, category, password):
    #opens csv file in read mode
    with open("software/parallel arrays/members.csv", "r") as file:
          firstname=[firstname]
          lastname=[lastname]
          category=[category]
          password=[password]
          reader = csv.reader(file)
          for row in reader:
               firstname.append(row[0])
               lastname.append(row[1])
               category.append(row[2])
               password.append(row[3])
    return category


#procedure to count amount of people in specific category
def numbercategory(category): 
     search = input("what category to count- Junior, Adult, Senior: ")
     counter=0
     for x in range (len(category)):
          if category[x].lower() == search.lower():
               counter=counter+1
     print(counter)


#procedure to check if password is valid or not
def validpassword(password):
     valid=False
     while not valid:
          password=input("enter password: ")
          #checks if password has any capital letters at start and if it has a symbol at the end of the password using unicode values
          if ord(password[0]) >=65 and ord(password[0])<=90 and ord(password[-1])>=35 and ord(password[-1])<=37:
               print("valid")
               valid = True
          else:
               print("invalid")
               valid=False


#main program
globalfirstname, globallastname, globalcategory, globalpassword = newmember()
globalcategory=readdisplayfile(globalfirstname, globallastname, globalcategory, globalpassword)
numbercategory(globalcategory)
validpassword(globalpassword)


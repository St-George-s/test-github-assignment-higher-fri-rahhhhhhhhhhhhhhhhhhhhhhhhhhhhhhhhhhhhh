import csv

def newmember():
    firstname = input("enter first name: ")
    lastname = input("enter last name: ")
    category= input("Enter category- Junior, adult, senior: ")
    password=input("enter password: ")
    return firstname, lastname, category, password


def readdisplayfile(firstname, lastname, category, password):
    with open("dataflow/members.csv", "r") as file:
          firstname=[]
          lastname=[]
          category=[]
          password=[]
          reader = csv.reader(file)
          for row in reader:
               firstname.append(row[0])
               lastname.append(row[1])
               category.append(row[2])
               password.append(row[3])

    return category


def numbercategory(category):
     search = input("what category to count- Junior, Adult, Senior: ")
     counter=0
     for x in range (len(category)):
          if category[x].lower() == search.lower():
               counter=counter+1
     print(counter)
               
               
          

globalfirstname, globallastname, globalcategory, globalpassword = newmember()
globalreaddisplay=readdisplayfile(globalfirstname, globallastname, globalcategory, globalpassword)
numbercategory(globalcategory)



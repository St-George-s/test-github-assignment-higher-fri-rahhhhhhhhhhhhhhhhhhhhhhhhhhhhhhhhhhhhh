import csv

def newmember():
    firstname = input("enter first name: ")
    lastname = input("enter last name: ")
    category= input("Enter category- Junior, adult, senior: ")
    password=input("enter password: ")
    return firstname, lastname, category, password


def readdisplayfile(firstname, lastname, category, password):
    with open("\members.csv", "r") as file:
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

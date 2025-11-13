import csv

class Order():
    def __init__(self, customerID, name, product, spent, category):
        self.customerID = customerID
        self.name = name
        self.product = product
        self.spent = spent
        self.category = category



# Reads orders from CSV file into an array
def readordersfromCSV():
    orders = []
    with open("software/records/ordersExtended.csv", "r") as file:
     
     reader = csv.reader(file)
     next(reader)
     for row in reader:
        neworder = Order(int(row[0]), row[1], row[2], float(row[3]), row[4])
        orders.append(neworder)

    return orders


# Finds maximum amount of money spent on a TV
def findmax(orders):
   maxorder = orders[0]
   for x in range(len(orders)):
      if "TV" in orders[x].product and orders[x].spent > maxorder.spent: # Checks if the product is a TV first and checks price if it isj
         maxorder = orders[x]
         print(maxorder.spent)


# Gives discount to customer if ID is divisible by 5 and writes to txt file with product as first 3 letters
def discount(orders):
    with open("software/records/discounts.txt", "w") as file:
        for x in range(len(orders)):
            productname = orders[x].product[0:3] 
            if orders[x].customerID % 5 == 0:
                file.write(str(orders[x].customerID) + " " + productname + " DISCOUNT CODE ASSIGNED")
            else:
               file.write(str(orders[x].customerID) + " " + productname + " NO DISCOUNT")
            file.write("\n") # new line in txt file


#main
orders = readordersfromCSV()
findmax(orders)
discount(orders)
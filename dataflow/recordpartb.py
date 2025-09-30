import csv

class Order():
    def __init__(self, name, product, spent):
        self.name = name
        self.product = product
        self.spent = spent


# Reads orders from CSV file into an array
def readordersfromCSV():
    orders = []
    with open("dataflow/orders.csv", "r") as file:
     
     reader = csv.reader(file)
     next(reader)
     for row in reader:
        neworder = Order(row[0], row[1], float(row[2]))
        orders.append(neworder)

    return orders


# Finds maximum amount of money spent on a TV
def findmax(orders):
   maxorder = orders[0]
   for x in range(len(orders)):
      if "TV" in orders[x].product and orders[x].spent > maxorder.spent: # Checks if the product is a TV first and checks price if it is
         maxorder = orders[x]
         print(maxorder.spent)


#main
orders = readordersfromCSV()
findmax(orders)
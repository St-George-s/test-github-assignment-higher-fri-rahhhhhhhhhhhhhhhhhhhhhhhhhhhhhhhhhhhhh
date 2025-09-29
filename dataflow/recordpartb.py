import csv

class Order():
    def __init__(self, name, product, spent):
        self.name = name
        self.product = product
        self.spent = spent

def readordersfromCSV():
    orders = []
    with open("dataflow/orders.csv", "r") as file:
     
     reader = csv.reader(file)
     next(reader)
     for row in reader:
        neworder = Order(row[0], row[1], float(row[2]))
        orders.append(neworder)

    return orders

def findmax(orders):
   maxorder = orders[0]
   for x in range(len(orders)):
      pass



#main
orders = readordersfromCSV()
#print(orders[1].spent)
from abc import ABC, abstractmethod
import csv
from pprint import pprint


class Cupcake(ABC):
    size = 'regular'
    def __init__(self, name, price, flavor, filling, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.filling = filling
        self.frosting = frosting
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for i in args:
            self.sprinkles.append(i)

    @abstractmethod    
    def calculate_price(self, quantity):
        return quantity * self.price
    

class MiniCC(Cupcake):
    size = 'mini'

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price


class RegularCC(Cupcake):

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price
    
class LargeCC(Cupcake):
    size = 'large'

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price    
    


cupcake1 = RegularCC("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Chocolate")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = MiniCC("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = LargeCC("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)



cupcake_list = [    
    cupcake1,
    cupcake2,
    cupcake3
]

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)
            # cupcake_list.append(row)


def create_csv(file, cupcakes):
    with open(file, 'w', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for cake in cupcakes:
            if hasattr(cake, 'filling'):
                writer.writerow({'size': cake.size, 'name': cake.name, 'price': cake.price, 'flavor': cake.flavor, 'frosting': cake.frosting, 'sprinkles': cake.sprinkles, 'filling': cake.filling})
            else:
                writer.writerow({'size': cake.size, 'name': cake.name, 'price': cake.price, 'flavor': cake.flavor, 'frosting': cake.frosting, 'sprinkles': cake.sprinkles})

# # read_csv('sample.csv')
# create_csv('sample2.csv', cupcake_list)
# pprint

def add_cupcakes(file, cupcakes):
    with open(file, 'a', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for cake in cupcakes:
            if hasattr(cake, 'filling'):
                writer.writerow({'size': cake.size, 'name': cake.name, 'price': cake.price, 'flavor': cake.flavor, 'frosting': cake.frosting, 'sprinkles': cake.sprinkles, 'filling': cake.filling})
            else:
                writer.writerow({'size': cake.size, 'name': cake.name, 'price': cake.price, 'flavor': cake.flavor, 'frosting': cake.frosting, 'sprinkles': cake.sprinkles})

# add_cupcakes('sample2.csv', cupcake_list)
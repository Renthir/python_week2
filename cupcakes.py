from abc import ABC, abstractmethod

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
    
    def __repr__(self):
        return self.items()

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

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

  
    def calculate_price(self, quantity):
        return quantity * self.price
    
class LargeCC(Cupcake):
    size = 'large'
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

  
    def calculate_price(self, quantity):
        return quantity * self.price    
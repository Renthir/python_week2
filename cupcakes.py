class Cupcake():
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
        pass
    

lemon_cake  = Cupcake('Lemon Cake', 5.99, 'Lemon', 'Lemon Creme', 'Lemon')
cookies_cake = Cupcake("Cookies and Cream", 2.99, "Chocolate", "Vanilla", "Oreo")

lemon_cake.filling = 'vanilla'

cookies_cake.is_mini = False

lemon_cake.add_sprinkles('Chocolate', 'Stars', 'vanilla')

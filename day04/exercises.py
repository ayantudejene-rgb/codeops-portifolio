# Exercise 1: 
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages.")

book1 = Book("The Alchemist", "Paulo Coelho", 208)
book2 = Book("Python Crash Course", "Eric Matthes", 544)
book1.describe()
book2.describe()

# Exercise 2: 
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price   # ETB
        self.quantity = quantity

    def restock(self, n):
        self.quantity += n

    def sell(self, n):
        if n > self.quantity:
            print(f"Cannot sell {n} of {self.name} – only {self.quantity} in stock.")
        else:
            self.quantity -= n

# Exercise 3 & 4:
class PrivateProduct:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity   # private

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self.__quantity = value

    def restock(self, n):
        if n <= 0:
            raise ValueError("Restock amount must be positive")
        self.__quantity += n

    def sell(self, n):
        if n <= 0:
            raise ValueError("Sell amount must be positive")
        if n > self.__quantity:
            raise ValueError(f"Insufficient stock. Only {self.__quantity} available.")
        self.__quantity -= n
print("\n--- PrivateProduct demo ---")
p1 = PrivateProduct("Laptop", 25000, 5)
print(f"{p1.name}: {p1.quantity} in stock")
p1.restock(3)
print(f"After restock: {p1.quantity}")
p1.sell(2)
print(f"After selling 2: {p1.quantity}")

# Exercise 5:
print("\n--- Independence proof ---")
prod1 = Product("Pen", 10, 100)
prod2 = Product("Notebook", 50, 30)
prod3 = Product("Eraser", 5, 200)
prod1.sell(10)     
print(f"{prod1.name}: {prod1.quantity}")
print(f"{prod2.name}: {prod2.quantity}")   
print(f"{prod3.name}: {prod3.quantity}")   
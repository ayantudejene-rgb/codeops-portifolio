# Exercise 1: 
class ReportData:
    """Responsibility: hold report data."""
    def __init__(self, content):
        self.content = content

class ReportSaver:
    """Responsibility: save report to file."""
    def save(self, report, filename):
        with open(filename, 'w') as f:
            f.write(report.content)

class ReportEmailer:
    """Responsibility: email the report."""
    def email(self, report, recipient):
        print(f"Emailing report to {recipient}: {report.content}")

# Exercise 2: 
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Square(4), Triangle(3, 6)]
for s in shapes:
    print(f"{s.__class__.__name__} area: {s.area():.2f}")

# Exercise 3: 
class AppSettings:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance

s1 = AppSettings()
s2 = AppSettings()
print(f"s1 is s2: {s1 is s2}")  # True
print(f"Currency: {s1.currency}")

# Exercise 4: 
class ShapeFactory:
    @staticmethod
    def create(kind, *args):
        if kind == "circle":
            return Circle(*args)
        elif kind == "square":
            return Square(*args)
        elif kind == "triangle":
            return Triangle(*args)
        else:
            raise ValueError(f"Unknown shape: {kind}")

circle = ShapeFactory.create("circle", 10)
square = ShapeFactory.create("square", 5)
print(f"Circle area: {circle.area():.2f}, Square area: {square.area():.2f}")

# Exercise 5: 
class NewsAgency:
    def __init__(self):
        self._observers = []
        self._news = None

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify(self):
        for obs in self._observers:
            obs.update(self._news)

    def set_news(self, news):
        self._news = news
        self.notify()

class TVNews:
    def update(self, news):
        print(f"TV: Breaking news – {news}")

class RadioNews:
    def update(self, news):
        print(f"Radio: News flash – {news}")

agency = NewsAgency()
tv = TVNews()
radio = RadioNews()
agency.subscribe(tv)
agency.subscribe(radio)
agency.set_news("Ethiopia wins gold medal!")
# Connor Critchley
# Day 13 objects lab
import math


# Valid class checks for valid input
class Validator:
    def __init__(self):  # init creates data placeholder
        self.data = None

    # Data method checks if data can be cast to float
    def valid(self):
        try:
            self.data = float(self.data)
        except ValueError:
            print("Invalid input")
        except TypeError:  # If type error, None type, means first run upon reaching loop
            return False
        return type(self.data) is float

    # Gets the data, ideally after casting to float
    def get_data(self):
        return self.data

    # Sets the data variable, for use in bad initial input
    def set_data(self, data):
        self.data = data


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_diameter(self):
        return self.radius * 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius * self.radius)

    def grow(self):
        self.radius = self.radius * 2

    def get_radius(self):
        return self.radius


valid = Validator()  # Create Validator instance
while not valid.valid():  # While input not valid, set radius
    valid.set_data(input("Enter a radius\n"))
circ = Circle(valid.get_data())  # Once validated, create Circle instance with cast radius

# Primary loop
running = True
while running:
    print(f"Diameter: {circ.calculate_diameter()}")
    print(f"Circumference: {circ.calculate_circumference()}")
    print(f"Area: {circ.calculate_area()}")
    if input("Grow the circle? y/n\n") != 'y':
        print(f"Goodbye!\nCircle radius: {circ.get_radius()}")
        running = False
    else:
        circ.grow()

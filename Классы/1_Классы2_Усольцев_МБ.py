class Grade():
    minimum_passing = 65

class Rules():
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes"

class Circle():
    def __init__(self, diameter):
        print(f"New circle with diameter: {diameter}")
        self.radius = diameter / 2

    def __repr__(self):
        return f"Circle with radius: {self.radius}"

    pi = 3.14

    def area(self, radius):
        return self.pi * radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius


teaching_table = Circle(36)
medium_pizza = Circle(12)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

print(dir(5))

def this_function_is_an_object():
    pass

print(dir(this_function_is_an_object))

print(medium_pizza)
print(teaching_table)
print(round_room)
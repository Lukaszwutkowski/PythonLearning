def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 4, 6, 12, 45, 2, 8))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(4, add=3,  multiply=3))

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

    def __str__(self):
        return self.make + " model: " + self.model + " colour: " + self.colour + " seats: " + self.seats

my_car = Car(make="Toyota", model="Prius Plus Seven", colour="Grey", seats="Grey skin")
print(my_car.make)
print(my_car)
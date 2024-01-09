class Car:
    color = None
class Motorcycle:
    size = None
def color_change(car,color):
    car.color = color
def describe_size(bike,size):
    bike.size = size
car1 = Car()
car2 = Car()
bike1 = Motorcycle()
color_change(car1,"blue")
color_change(car2,"red")
describe_size(bike1,"Large")
print(car1.color)
print(car2.color)
print(bike1.size)
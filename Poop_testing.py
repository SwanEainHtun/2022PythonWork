from car import Car

car_1 = Car("Cherry","Marcedee",2001,"black")
car_2 = Car("Ellen","Prada",1999,"white")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_2.stop()
print(car_1.wheels)
Car.wheels = 2
print(car_1.wheels)
print(car_2.wheels)
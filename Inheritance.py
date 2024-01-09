class Animal():
    alive = True
    def eat(self):
        print("This animal " + " is eating")
    def sleep(self):
        print("This animal " + " is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This animal is running")

class Fish(Animal):
    def swim(self):
        print("This animal is swimming")
class Hwak(Animal):
    def fly(self):
        print("This animal is flying")
animal1 = Rabbit()
animal2 = Fish()
animal3 = Hwak()

print(animal1.alive)
animal1.run()
animal2.sleep()
animal3.fly()
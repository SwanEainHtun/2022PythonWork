class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is chuckling")
class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is tweeting")
class Person:
    def caught(self,animal):
        animal.talk()
        animal.walk()
        print("You are caught bitter")
duck = Duck()
chicken = Chicken()
person = Person()
person.caught(duck)
print("------------------------")
person.caught(chicken)
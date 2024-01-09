class Prey:
    def flee(self):
        print("This animal flees")
class Predator:
    def hunt(self):
        print("This animal is hunting")

class Fish(Prey,Predator):
    def swim(self):
        print("This animal is swimming")
class GoldenF(Fish):
    def live(self):
        print("This type iof fish live in ocean")
fish = GoldenF()
fish.flee()
fish.hunt()
fish.swim()
fish.live()
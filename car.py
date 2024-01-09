
#Creating an object

class Car:
    wheels = 4 #class variable

    def __init__(self,make,model,year,color):#This function is a special functiion or constructor
        self.make = make  #instance variable
        self.model = model
        self.year = year
        self.color = color
    def drive(self):
        print(self.model + " is running")
    def stop(self):
        print(self.model+" stopped")


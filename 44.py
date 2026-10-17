class Car:
        wheels=4
        def __init__(self,brand): self.brand=brand
        def display(self): print(self.brand,"has",self.wheels,"wheels")
Car(input("Car brand: ")).display()
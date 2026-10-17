class Student:
        def __init__(self,name,roll): self.name=name; self.roll=roll
        def display(self): print("Name:",self.name,"Roll:",self.roll)
Student(input("Name: "),input("Roll: ")).display()
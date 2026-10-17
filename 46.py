class Person:
        def __init__(self,name): self.name=name
class Student(Person):
        def display(self): print("Student name:",self.name)
Student(input("Name: ")).display()

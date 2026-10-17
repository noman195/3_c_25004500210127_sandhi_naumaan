class Student:
        def __init__(self,name,marks): self.name=name; self.marks=marks
        def grade(self): return "Pass" if self.marks>=35 else "Fail"
s=Student(input("Name: "),float(input("Marks: "))); print(s.name,s.grade())
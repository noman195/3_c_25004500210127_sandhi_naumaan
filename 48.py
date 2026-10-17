class Rectangle:
        def __init__(self,l,b): self.l=l; self.b=b
        def area(self): return self.l*self.b
class Circle:
        def __init__(self,r): self.r=r
        def area(self): return 3.14159*self.r**2
for shape in [Rectangle(4,5),Circle(3)]: print("Area:",shape.area())

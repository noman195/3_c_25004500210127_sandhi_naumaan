class Temperature:
        def __init__(self,celsius): self.celsius=celsius
        @property
        def celsius(self): return self._celsius
        @celsius.setter
        def celsius(self,value): self._celsius=value
t=Temperature(float(input("Celsius: "))); print("Celsius",t.celsius,"Fahrenheit",t.celsius*9/5+32)

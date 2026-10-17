a=set(map(int,input("Set A: ").split())); b=set(map(int,input("Set B: ").split()))
print("Union",a|b,"Intersection",a&b,"A-B",a-b,"Symmetric difference",a^b)
values=[10,20,30]
try:
        i=int(input("Index 0 to 2: ")); print(values[i])
except ValueError: print("Index must be an integer")
except IndexError: print("Index out of range")
try:
        a=float(input("A: ")); b=float(input("B: ")); print(a/b)
except ZeroDivisionError: print("Cannot divide by zero")
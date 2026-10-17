n=int(input("Non-negative integer: ")); result=1
if n<0: print("Not defined for negative numbers")
else:
    for i in range(1,n+1): result*=i
print("Factorial:",result)

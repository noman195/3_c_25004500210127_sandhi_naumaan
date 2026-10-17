def fibonacci(count):
        a,b=0,1; result=[]
        for _ in range(count): result.append(a); a,b=b,a+b
        return result
print(fibonacci(int(input("Terms: "))) )

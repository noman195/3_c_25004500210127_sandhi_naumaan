def check_age(age):
        if age<0: raise ValueError("Age cannot be negative")
        return age
try: print(check_age(int(input("Age: "))))
except ValueError as error: print("Error:",error)
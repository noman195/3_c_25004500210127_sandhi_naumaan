try: n=int(input("Integer: "))
except ValueError: print("Invalid integer")
else: print("You entered",n)
finally: print("Program finished")

m=float(input("Marks out of 100: "))
if m>=90: g="A+"
elif m>=80: g="A"
elif m>=70: g="B"
elif m>=60: g="C"
elif m>=35: g="Pass"
else: g="Fail"
print("Grade:",g)
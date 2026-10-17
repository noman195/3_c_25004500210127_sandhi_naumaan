s=input("Text: ").lower().replace(" ","")
print("Palindrome" if s==s[::-1] else "Not palindrome")

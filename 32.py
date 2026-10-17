text=input("Text to save: ")
with open("sample.txt","w",encoding="utf-8") as f: f.write(text)
print("Saved to sample.txt")
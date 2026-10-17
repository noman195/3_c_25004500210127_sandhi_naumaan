source=input("Source filename: "); target=input("Destination filename: ")
with open(source,"r",encoding="utf-8") as src: data=src.read()
with open(target,"w",encoding="utf-8") as dst: dst.write(data)
print("Copied")
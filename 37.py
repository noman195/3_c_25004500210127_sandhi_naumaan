with open("sample.txt","r",encoding="utf-8") as f: data=f.read()
print("Lines",len(data.splitlines()),"Words",len(data.split()),"Characters",len(data))
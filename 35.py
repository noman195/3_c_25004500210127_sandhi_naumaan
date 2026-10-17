with open("sample.txt","r",encoding="utf-8") as f:
        for number,line in enumerate(f,1): print(number,line.rstrip())
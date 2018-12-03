with open("data") as f:
        data = f.readlines()
        print(data)
        start = 0 
        for d in data:
            if d[0] == "+":
                start += int( d[1:-1])
            else:
                start -= int( d[1:-1])
        print(start)

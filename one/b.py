with open("data") as f:
        data = f.readlines()
        start = 0 
        i = 0 
        seen = {start}
        while True:
            d = data[i] 
            i += 1
            i = i % len(data)
            if d[0] == "+":
                start += int( d[1:-1])
            else:
                start -= int( d[1:-1])
            if start in seen:
                break
            else:
                seen.add(start)
        print(start)

size = 1000

with open("data") as f:
    data = f.readlines()
    # print(data)
    data1 = [d.split(" ")[2:] for d in data]
    data2 = [[  *d[0][:-1].split(","),   *d[1][:-1].split("x") ] for d in data1    ]
    parsed = [[int(k) for k in d] for d in data2]
    print(parsed[0])

    # [left, top, right, bottom ]
    bounds = [[d[0],d[1],d[0]+d[2], d[1]+d[3]] for d in parsed]
    print(max(d[2] for d in bounds), max(d[3] for d in bounds))
    fabric = [[0 for i in range(size)] for j in range(size)]

    for b in bounds:
        for y in range(b[1],b[3]):
            for x in range(b[0], b[2]):
                fabric[y][x] += 1  
    # for line in fabric:
        # print(line)
    # print()
    for y in range(size):
        for x in range(size):
            if fabric[y][x] == 1:
                fabric[y][x] = 0 
            elif fabric[y][x] > 0:
                fabric[y][x] = 1
    # for line in fabric:
        # print(line)


    print( sum( (sum(d) for d in fabric)))
    # print(fabric[0])
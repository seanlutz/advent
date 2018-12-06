with open("data") as f:
    data1 = f.readlines()
    data = [ [int(i.split(", ")[0]), int(i.split(", ")[1])] for i in data1]
    print(data[0])
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    board = [ ["" for j in range(min(x), max(x)+1)] for i in range(min(y), max(y)+1)   ]
    normalized = [[d[0]-min(x), d[1] - min(y)] for d in data   ]
    for i, d in enumerate(normalized):
        board[d[1]][d[0]] = str(i)

    def updateNB(nb, board, x, y):
        val = board[y][x]
        changed = False
        if x > 0:
            if nb[y][x-1] in ["-1",val]:
                pass
            elif nb[y][x-1] == "":
                nb[y][x-1] = val
                changed = True
            elif board[y][x-1] == "":
                nb[y][x-1] = "-1"
                changed = True
        if y > 0:
            if nb[y-1][x] in ["-1",val]:
                pass
            elif nb[y-1][x] == "":
                changed = True
                nb[y-1][x] = val
            elif board[y-1][x] == "":
                nb[y-1][x] = "-1"
                changed = True
        if x < len(nb[0])-1:
            if nb[y][x+1] in ["-1",val]:
                pass
            elif nb[y][x+1] == "":
                nb[y][x+1] = val
                changed = True
            elif board[y][x+1] == "":
                nb[y][x+1] = "-1"
                changed = True
        if y < len(nb)-1:
            if nb[y+1][x] in ["-1",val]:
                pass
            elif nb[y+1][x] == "":
                nb[y+1][x] = val
                changed = True
            elif board[y+1][x] == "":
                nb[y+1][x] = "-1"
                changed = True
        return changed





    change = True
    counterpls = 0 
    while change:
        # for row in board:
        #     print(row)
        print(counterpls)
        counterpls+=1
        change = False
        nb = [ [board[i][j] for j in range(len(board[0]))] for i in range(len(board))   ]
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] not in ["", "-1"]:
                    valid = updateNB(nb, board, x, y)
                    if valid:
                        # print(x,y)
                        change = True
        board = nb 
    counts = {}
    for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] not in counts:
                    counts[board[y][x]] = 0
                counts[board[y][x]] += 1 
    edges = set([*board[0], *board[-1],*[i[0] for i in board], *[i[-1] for i in board]] )
    for e in edges:
        del counts[e]
    # for row in board:
    #     print(row)
    print(max(counts.values()))

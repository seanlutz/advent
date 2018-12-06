with open("data") as f:
    data1 = f.readlines()
    data = [ [int(i.split(", ")[0]), int(i.split(", ")[1])] for i in data1]
    print(data[0])
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    board = [ ["_" for j in range(min(x), max(x)+1)] for i in range(min(y), max(y)+1)   ]
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

    def getDist(data, i, j ):
        tot = 0 
        for x, y in data:
            tot += abs(x-i) + abs(y-j)
        return tot

    total = 0
    # took me far too long to figure out there are valid points outside the bounds of the board 
    for i in range(-len(board), 2* len(board)):
        for j in range(-len(board[0]), 2*len(board)):
            if getDist(data, j, i) < 10000:
                total += 1
                # board[i][j] = "O"
    # for row in board:
        # print(row)
    print(total)

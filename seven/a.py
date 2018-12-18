with open("data") as f:
    data1 = f.readlines()
    data = [d.split(" ") for d in data1]
    data = [(d[1], d[7]) for d in data ]
    print(data[0])
    deps = {}
    vals = set()
    for x,y in data:
        vals.add(x)
        vals.add(y)
    for v in vals:
        deps[v] = []
    for t, f in data:
        deps[f].append(t)
    vals = sorted(list(vals))
    ans = []
    while vals:
        for v in vals:
            if v in deps and len(deps[v]) == 0:
                ans.append(v)
                for c in deps:
                    if v in deps[c]:
                        deps[c].remove(v)
                del deps[v]
                break
        vals.remove(ans[-1])
    print( "".join(ans))
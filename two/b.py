def inCommon(w1,w2):
    diff = 0
    if len(w1) != len(w2):
        return 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1 
    return diff

def lettersInCommon(w1,w2):
    res = [] 
    for i in range(len(w1)):
        if w1[i] == w2[i]:
            res.append(w1[i])
    return "".join(res)

with open("data") as f:
    data = f.readlines()
    for i, val1 in enumerate(data):
        for j, val2 in enumerate(data):
            if i != j:
                # print(inCommon(val1,val2))
                if inCommon(val1,val2)==1:
                    print(lettersInCommon(val1,val2))


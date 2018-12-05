from typing import Dict
with open("data") as f:
    data = f.readlines()
    two = 0 
    three = 0 
    for d in data:
        counts:Dict[str,int] = {}
        for w in d:
            if w in counts:
                counts[w] += 1 
            else:
                counts[w] = 1 
        s = set(counts.values()) 
        if 2 in s:
            two += 1 
        if 3 in s:
            three += 1 

    print(two*three)

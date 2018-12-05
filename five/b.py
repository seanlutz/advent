from typing import Dict, List, Tuple, NewType 
from collections import deque 
with open("data") as f:
    data = f.readlines()[0]
    print(set(data.lower()))
    # data = "dabAcCaCBAcCcaDA"
    # print(data)
    results = []
    for c in set(data.lower()):
        data1 = data.replace(c,"").replace(c.upper(), "")
        queue = deque(data1)
        # to make list not circular
        queue.append(" ")
        print(len(queue))
        iterations = len(queue)
        while queue and iterations:
            if len(queue) == 1:
                break
            if queue[0].lower()== queue[1].lower() and queue[0] != queue[1]:
                queue.popleft()
                queue.popleft()
                iterations = len(queue)
            elif queue[0].lower() == queue[-1].lower() and queue[0] != queue[-1]:
                queue.popleft()
                queue.pop()
                iterations = len(queue)
            else:
                queue.rotate(1)
                iterations -= 1
        # print(queue)
        print(len(queue)-1)
        results.append((len(queue)-1, c))

print(sorted(results))
        

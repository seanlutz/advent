from typing import Dict, List, Tuple, NewType 
from collections import deque 
with open("data") as f:
    # data = f.readlines()[0]
    data = "dabAcCaCBAcCcaDA"
    # print(data)
    queue = deque(data)
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
    print(queue)
    print(len(queue)-1)


        

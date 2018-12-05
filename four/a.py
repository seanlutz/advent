from typing import Dict, List, Tuple, NewType 
with open("data") as f:




    data = f.readlines()

    IntervalDict = NewType("IntervalDict", Dict[int, List[Tuple[int,int]]])
    

    def sortSeries(data:List[str]) -> Tuple[List[int], List[str]]:
        parsed1 = [d[1:].split("]")[0].split(" ") for d in data]
        times = [ [*d[0].split("-"), *d[1].split(":") ]  for d in parsed1  ]
        sort = sorted(zip(times,data), key = lambda x: x[0]) 
        minutes = [int(d[0][-1]) for d in sort ]
        timeseries = [d[1].split("] ")[1] for d in sort]
        return minutes, timeseries

    
    def getIntervals(timeseries:List[str], minutes:List[int]) -> Dict[int, List[Tuple[int,int]]]:
        guard = -1
        intermed: Dict[int, List[int]] = {}
        for i,val in enumerate(timeseries):
            vals = val.split(" ")
            if vals[0] =="Guard":
                guard = int(vals[1][1:])
                if guard not in intermed:
                    intermed[guard] = []
            else:
                intermed[guard].append(minutes[i])
                
        res:Dict[int, List[Tuple[int,int]]]=  {}
        for key in intermed:
            v = [] 
            for i in range(len(intermed[key])//2):
                v.append(  (intermed[key][2*i], intermed[key][2*i+1]) )
            res[key] = v 
        return res


    def maxTimeAndGuard(intervals:Dict[int, List[Tuple[int,int]]]) -> Tuple[int,int]:
        guard = -1 
        maxi = 0
        for i in intervals:
            val = sum([ d[1] - d[0] for d in intervals[i]])
            if not maxi or maxi < val:
                maxi = val
                guard = i 
        return guard, maxi


    def sleepiestMinute(interval:List[Tuple[int,int]]) -> int:  
        minutes = [0 for i in range(60)]
        for start,stop in interval:
            for i in range(start,stop):
                minutes[i] += 1
        return minutes.index(max(minutes))





    minutes, timeseries = sortSeries(data)
    intervals = getIntervals(timeseries, minutes)
    maxguard = maxTimeAndGuard(intervals)
    minute = sleepiestMinute(intervals[maxguard[0]])
    print(maxguard[0]*minute)



    
    
        
    

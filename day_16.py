def part_1():
    MAP = {}
    DIST = {}
    GRAPH = {}
    with open("day_16.txt") as f:
        
        for y,l in enumerate(f.readlines()):
            for x,c in enumerate(l.strip()):
                MAP[(y,x)]=c
                
    START = [coord for coord,val in MAP.items() if val =="S"][0]
    END = [coord for coord,val in MAP.items() if val =="E"][0]
    DIST[START]=0
    width = max([x for _,x in MAP.keys()]) +1
    height = max([y for y,_ in MAP.keys()]) +1
    visited = set()
    while END not in DIST:
        current_coord,current_dist = [ (c,v) for (c,v) in sorted(DIST.items(),key=lambda a:a[1]) if c not in visited][0]
        
        next = sorted([coord for coord,val in MAP.items() if val !="#" 
                and (( (current_coord[0]+1 == coord[0] or  current_coord[0]-1 == coord[0]) and current_coord[1] == coord[1])
                or ( (current_coord[1]+1 == coord[1] or  current_coord[1]-1 == coord[1]) and current_coord[0] == coord[0]))
                ])
        
        for n in next:
            d=DIST.get(n,10000000)
            prev = GRAPH.get(current_coord)

            if not prev: # Start
                DIST[n] =  current_dist+1
                GRAPH[n] = current_coord
                # print(n," COST ",current_dist+1)
            else:
                
                cost = 1
                if not (prev[0]==current_coord[0]==n[0] or prev[1]==current_coord[1]==n[1]): #edge
                    cost+= 1000
                if current_dist+cost<d:
                    # print(prev , " >> ",current_coord, " >> ", n)
                    # print(n," COST ",current_dist+cost)
                    DIST[n] =  current_dist+cost
                    GRAPH[n] = current_coord


        visited.add(current_coord)
        """for y in range(0,height):
            for x in range(0,width):
                if (y,x) in DIST :
                    print("█",end="")
                else:
                    print(MAP[(y,x)],end="")
            print()"""
    print(DIST[END])
    
    soluce = [END]
    g = GRAPH[END]
    """soluce.append(g)
    while MAP[g] != "S":

        g = GRAPH[g]
        soluce.append(g)
    edge = 0
    for s in range(1,len(soluce)-1):
        if not (soluce[s][0] == soluce[s-1][0] == soluce[s+1][0]):
            edge += 1"""
        
    """for y in range(0,height):
        for x in range(0,width):
            if (y,x) in soluce :
                print("×",end="")
            else:
                print(MAP[(y,x)].replace("."," ").replace("#","░"),end="")
        print()"""
def part_2():
    MAP = {}
    DIST = {}
    GRAPH = {}
    with open("day_16.test.txt") as f:
        
        for y,l in enumerate(f.readlines()):
            for x,c in enumerate(l.strip()):
                MAP[(y,x)]=c
                
    START = [coord for coord,val in MAP.items() if val =="S"][0]
    END = [coord for coord,val in MAP.items() if val =="E"][0]
    DIST[START]=0
    width = max([x for _,x in MAP.keys()]) +1
    height = max([y for y,_ in MAP.keys()]) +1
    visited = set()
    free = len([ k for k,c in MAP.items() if c == "."])
    while len(DIST) -2 !=  free:
        current_coord,current_dist = [ (c,v) for (c,v) in sorted(DIST.items(),key=lambda a:a[1]) if c not in visited][0]
        
        next = [coord for coord,val in MAP.items() if val !="#" 
                and (( (current_coord[0]+1 == coord[0] or  current_coord[0]-1 == coord[0]) and current_coord[1] == coord[1])
                or ( (current_coord[1]+1 == coord[1] or  current_coord[1]-1 == coord[1]) and current_coord[0] == coord[0]))
                ]
        for n in next:
            d=DIST.get(n,10000000)
            prev = GRAPH.get(current_coord)

            if not prev: # Start
                cost = 1
                if n[0] != current_coord[1]:
                    cost+=1000
                DIST[n] =  current_dist+cost
                GRAPH[n] = current_coord
                # print(n," COST ",current_dist+1)
            else:
                
                cost = 1
                if not (prev[0]==current_coord[0]==n[0] or prev[1]==current_coord[1]==n[1]): #edge
                    cost+= 1000
                if current_dist+cost<d:
                    # print(prev , " >> ",current_coord, " >> ", n)
                    # print(n," COST ",current_dist+cost)
                    DIST[n] =  current_dist+cost
                    GRAPH[n] = current_coord


        visited.add(current_coord)
        """for y in range(0,height):
            for x in range(0,width):
                if (y,x) in DIST :
                    print("█",end="")
                else:
                    print(MAP[(y,x)],end="")
            print()"""
    print(DIST[END])
    for y in range(0,height):
        for x in range(0,width):
            if DIST.get((y,x)) :
                print(f'{DIST.get((y,x))//1000}',end="")
            else:
                print(MAP[(y,x)].replace("."," ").replace("#","░"),end="")
        print()
    soluce = []
    to_visit = [END]
    exit()
    while to_visit:
        current = to_visit.pop()
        soluce.append(current)
        d = DIST[current]
        if prev := GRAPH.get(current):
            print(current, d)

            other =  [coord for coord,val in MAP.items() if val  not in ["#","E","S"]  and coord != prev and coord not in to_visit and coord not in soluce
                    and (( (current[0]+1 == coord[0] or  current[0]-1 == coord[0]) and current[1] == coord[1])
                    or ( (current[1]+1 == coord[1] or  current[1]-1 == coord[1]) and current[0] == coord[0]))
                    ]
            for o in other : 
                q = DIST.get(o)
                print(">>",o,q)
                if q and(q-d == 1001 or q-d == 1) :
                    to_visit.append(o)
                


            print("****")
            if prev := GRAPH.get(current):
                to_visit.append(prev)
    edge = 0
    """for s in range(1,len(soluce)-1):
        if not (soluce[s][0] == soluce[s-1][0] == soluce[s+1][0]):
            edge += 1"""
        
    for y in range(0,height):
        for x in range(0,width):
            if (y,x) in soluce :
                print("×",end="")
            else:
                print(MAP[(y,x)].replace("."," ").replace("#","░"),end="")
        print()
# part_1()
part_2()
# Too high 115476
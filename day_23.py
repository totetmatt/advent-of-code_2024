def part_1():
    with open("day_23.txt") as f:
        GRAPH = {}
        data =[l.strip().split("-") for l in f.readlines()]
        for a,b in data:
            if a not in GRAPH:
                GRAPH[a] = set()
            GRAPH[a].add(b)
            if b not in GRAPH:
                GRAPH[b] = set()
            GRAPH[b].add(a)
        TRIPLET = set()
        with open("edges.csv",'w') as f:
            f.write("source;target\n")
            for a,b in GRAPH.items():
                for bb in b:
                    f.write(f'{a};{bb}\n')
        for a in GRAPH.keys():
            for b in GRAPH.keys():
                if a != b and b in GRAPH[a] and a in GRAPH[b]:
                    it = GRAPH[a].intersection(GRAPH[b])
                    if it:
                        for i in it:
                            TRIPLET.add(tuple(sorted((a,b,i))))
        res = [ a for a in TRIPLET if any(['t' in x[0] for x in a])]
        print(len(res))
def part_2():
    with open("day_23.test.txt") as f:
        GRAPH = {}
        GROUPS = {}
        gid = 0
        data =[l.strip().split("-") for l in f.readlines()]
        for a,b in data:
            if a not in GRAPH:
                GRAPH[a] = set()
            GRAPH[a].add(b)
            if b not in GRAPH:
                GRAPH[b] = set()
            GRAPH[b].add(a)
            ga = GROUPS.get(a)
            gb = GROUPS.get(b)
            if ga and gb:
                
                for i in GROUPS.keys():
                    if i not in [a,b] and GROUPS[i] == GROUPS[a] or  GROUPS[i] == GROUPS[b]:
                       GROUPS[i] = gid
                GROUPS[a] = GROUPS[b] = gid
                gid+=1 
            elif ga and not gb :
                GROUPS[b]=GROUPS[a]
            elif gb and not ga:
                GROUPS[a]=GROUPS[b]
            else:
                GROUPS[a] = GROUPS[b] = gid
                gid += 1
            
        RGROUP = {}
        for k,v in GROUPS.items():
            if v not in RGROUP:
                RGROUP[v] = set()
            RGROUP[v].add(k)
        print(RGROUP)

        
        

part_1()
part_2()
# too high 2406
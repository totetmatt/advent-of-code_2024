from itertools import combinations
def part_1():
    with open("day_08.txt") as f:
        MAP = { y:{x:c.strip() for x,c in enumerate(l.strip()) } for y,l in enumerate(f.readlines())}
   

        ANTENNAS = {}
        for y,l in MAP.items():
            for x,c in l.items():
                if c != '.':
                    if c not in ANTENNAS:
                        ANTENNAS[c]=[]
                    ANTENNAS[c].append((y,x))

        
        cpt = 0
        def vec2add(a,b):
            return (a[0]+b[0],a[1]+b[1])
        
        for antena_pos in ANTENNAS.values():
            for l,r in combinations(antena_pos,2):
                for a,b in [(l,r),(r,l)]:
                    # Y,X
                    v = (a[0]-b[0],a[1]-b[1])
                    v2 = (v[0]*2,v[1]*2)

                    if vec2add(a,v)==vec2add(b,v2):
                        s = vec2add(a,v)
                        c = MAP.get(s[0],{}).get(s[1],None)
                        if c and c != "#":
                            cpt += 1
                        # if c == '.':
                            MAP[s[0]][s[1]] = "#"
                            
                    if vec2add(b,v)==vec2add(a,v2):
                        s = vec2add(a,v2)
                        c = MAP.get(s[0],{}).get(s[1],None)
                        if c:
                            cpt += 1
                        # if c == '.':
                            MAP[s[0]][s[1]] = "#"
    print(cpt)
def part_2():
    with open("day_08.txt") as f:
        MAP = { y:{x:c.strip() for x,c in enumerate(l.strip()) } for y,l in enumerate(f.readlines())}
   

        ANTENNAS = {}
        for y,l in MAP.items():
            for x,c in l.items():
                if c != '.':
                    if c not in ANTENNAS:
                        ANTENNAS[c]=[]
                    ANTENNAS[c].append((y,x))

        
        cpt = 0
        def vec2add(a,b):
            return (a[0]+b[0],a[1]+b[1])
        def vec2mul(a,s):
            return (a[0]*s,a[1]*s)
        for antena_pos in ANTENNAS.values():
            for l,r in combinations(antena_pos,2):
                for a,b in [(l,r),(r,l)]:
                    # Y,X
                    v = (a[0]-b[0],a[1]-b[1])
                    s = 0
                    vp = vec2mul(v,s)
                    mp = vec2add(l,vp)
                    while c:=MAP.get(mp[0],{}).get(mp[1],None):
                        if c and c != "#":
                            cpt += 1
                            MAP[mp[0]][mp[1]]="#"
                        s += 1
                        vp = vec2mul(v,s)
                        mp = vec2add(l,vp)    

             
    print(cpt)
part_1()
part_2()
def part_1():
    with open("day_12.txt") as f:
        MAP = {}
        for y,l in enumerate(f.readlines()):
            for x,c in enumerate(l.strip()):
                MAP[(y,x)]=c    
        
        visited = set()
        zones = []
        cpt = 0
        for k,v in MAP.items():
            if k in visited:
                continue
            current = v 

            walk = [k]
            zone = set([k])
            while walk:
                (y,x) = walk.pop()
                candidate = [(y+dy,x+dx) for (dy,dx) in [(-1,0),(1,0),(0,-1),(0,1)] if MAP.get((y+dy,x+dx)) == current and (y+dy,x+dx) not in zone ]
                # print(candidate)
                walk.extend(candidate)
                zone.update(candidate)

            peri = list()
            for (cy,cx) in zone:
                peri.extend([(cy+dy,cx+dx)  for (dy,dx) in [(-1,0),(1,0),(0,-1),(0,1)] if (cy+dy,cx+dx) not in zone])
            area = len(zone)
            perim = len(peri)

            cpt += area*perim

            visited.update(zone)
        print(cpt)

def part_2():
    with open("day_12.txt") as f:
        MAP = {}
        for y,l in enumerate(f.readlines()):
            for x,c in enumerate(l.strip()):
                MAP[(y,x)]=c    
        
        visited = set()
        zones = []
        cpt = 0
        for k,v in MAP.items():
            if k in visited:
                continue
            current = v 

            walk = [k]
            zone = set([k])
            while walk:
                (y,x) = walk.pop()
                candidate = [(y+dy,x+dx) for (dy,dx) in [(-1,0),(1,0),(0,-1),(0,1)] if MAP.get((y+dy,x+dx)) == current and (y+dy,x+dx) not in zone ]
                # print(candidate)
                walk.extend(candidate)
                zone.update(candidate)
            peri = list()
            for (cy,cx) in zone:
                peri.extend([((dy,dx),( (cy+dy), (cx+dx)))  for (dy,dx) in [(-1,0),(1,0),(0,-1),(0,1)] if (cy+dy,cx+dx) not in zone])
            area = len(zone)

            pperi = {}
            for a,b in peri:
                if a not in pperi:
                    pperi[a]=list()
                pperi[a].append(b)
            cside = 0
            for ((dy,dx),p) in pperi.items():
                p = sorted(p,key=lambda pp: pp if dx==0 else (pp[1],pp[0]))
                side = [ p[0]]
                # print(  (dy,dx), "::::",p)
                for (sy,sx) in p[1:]:
                    if dx==0: # Testing up or down
                        if sy != side[-1][0] : # change line
                            side.append((sy,sx))
                        elif sx  == side[-1][1]+1 : #Continuous
                            side[-1] = (side[-1][0],sx)
                        else: # breaking
                            side.append((sy,sx))
                    elif dy==0: # Testing up or down
                        if sx != side[-1][1] : # change col
                            side.append((sy,sx))
                        elif sy  == side[-1][0]+1 : #Continuous
                            side[-1] = (sy,side[-1][1])
                        else: # breaking
                            side.append((sy,sx))
                cside += len(side)
            
            # perim = sum([len(b) for _,b in pperi.items()])
            cpt += area*cside

            visited.update(zone)
        print(cpt)


part_1()
part_2()
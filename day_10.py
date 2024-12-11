from operator import xor
def part_1():
    cpt = 0
    with open("day_10.txt") as f:
      
        MAP = {}
        for y,l in enumerate(f.readlines()):
            for x,c in enumerate(l.strip()):

                MAP[(y,x)]=int(c) if c.isdigit() else -1
        
        starts = [(c,v) for (c,v) in MAP.items() if v == 0]
        for s in starts:
            end = set()
            next = [s]
            while next:
                reach = []
                for n in next:
                    reach.extend([ ((ny,nx),nv) for ((ny,nx),nv) in MAP.items() if nv == n[1]+1 and (abs(ny-n[0][0])==1 and nx==n[0][1] or abs(nx-n[0][1])==1  and ny==n[0][0]) ])
                end.update([r for r in reach if r[1]==9])
                next = [r for r in reach if r[1]!=9]


            cpt += len(end)
    print(cpt)
        
def part_2():
    cpt = 0
    with open("day_10.txt") as f:
      
        MAP = {}
        for y,l in enumerate(f.readlines()):
            for x,c in enumerate(l.strip()):

                MAP[(y,x)]=int(c) if c.isdigit() else -1
        
        starts = [(c,v) for (c,v) in MAP.items() if v == 0]
        for s in starts:
            end = []
            next = [s]
            while next:
                reach = []
                for n in next:
                    reach.extend([ ((ny,nx),nv) for ((ny,nx),nv) in MAP.items() if nv == n[1]+1 and (abs(ny-n[0][0])==1 and nx==n[0][1] or abs(nx-n[0][1])==1  and ny==n[0][0]) ])
                end.extend([r for r in reach if r[1]==9])
                next = [r for r in reach if r[1]!=9]

            cpt += len(end)
    print(cpt)
part_1()
part_2()
TOKEN = {
    "A":3,
    "B":1
}


def solve1(a,b,na,nb,target):
    # A
    ax = target[0] // a[0]
    ay = target[1] // a[1] 
    ma = min(ax,ay)

    bx = target[0] // b[0]
    by = target[1] // b[1] 
    mb = min(bx,by)  

    sa = [ (r,(a[0]*r,a[1]*r)) for r in range(ma,0,-1)]
    sb = [ (r,(b[0]*r,b[1]*r)) for r in range(mb,0,-1)]

    for aa in sa:
        for bb in sb:
            if [aa[1][0]+bb[1][0],aa[1][1]+bb[1][1]] == target:
                if aa[1][0]+bb[1][0]< target[0] or aa[1][1]+bb[1][1]< target[1]:
                    break
                return (aa[0],bb[0])
def solve2(a,b,na,nb,target):
    # A
    ax = target[0] // a[0]
    ay = target[1] // a[1] 
    ma = min(ax,ay)

    bx = target[0] // b[0]
    by = target[1] // b[1] 
    mb = min(bx,by)  
    """
    
    """
    x = (target[0]*b[1] - b[0]*target[1])/( (a[0]*b[1]) - (b[0]*a[1])) 
    y = (target[1]*a[0] - a[1]*target[0])/( (a[0]*b[1]) - (b[0]*a[1])) 
    if x%1 == 0 and y%1==0:
        return (x,y)
    
def part_1():
    prgm = []
    with open("day_13.txt") as f:
        
        data = [l.strip() for l in f.readlines()]
        for i in range(0,len(data),4) :
            a,b,p = data[i], data[i+1], data[i+2]
            prg = {}
            for k,v in [("A",a),("B",b),("P",p)]:
                prg[k]=([ int(a.strip()[2:]) for a in v.split(":")[-1].split(",")])

            prgm.append(prg)
    cpt = 0
    for p in prgm:

        s = (solve1(p['A'],p['B'],0,0,p['P']))
        if s:
            cpt += s[0]*TOKEN["A"]+s[1]*TOKEN["B"]
    print(cpt)
def part_2():
    prgm = []
    with open("day_13.txt") as f:
        
        data = [l.strip() for l in f.readlines()]
        for i in range(0,len(data),4) :
            a,b,p = data[i], data[i+1], data[i+2]
            prg = {}
            for k,v in [("A",a),("B",b),("P",p)]:
                prg[k]=([ int(a.strip()[2:]) for a in v.split(":")[-1].split(",")])

            prgm.append(prg)
    cpt = 0
    for p in prgm:
        real_p = [p["P"][0]+10000000000000,p["P"][1]+10000000000000]
        s = (solve2(p['A'],p['B'],0,0,real_p))
        if s:
            cpt += s[0]*TOKEN["A"]+s[1]*TOKEN["B"]


    print(cpt)
part_1()    
part_2()
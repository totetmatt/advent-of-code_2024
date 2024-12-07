def solve(h,t,r):
    # print(">",h,t,r)
    bh, *bt = t
    add = h + bh
    mul = h * bh
    if len(bt)==0:
        return (add == r or mul == r)
    return solve(add,bt,r) or solve(mul,bt,r)

def solve2(h,t,r):
    # print(">",h,t,r)
    bh, *bt = t
    add = h + bh
    mul = h * bh
    concat = int(str(h)+str(bh))
    if len(bt)==0:
        return (add == r or mul == r or concat == r)
    return solve2(add,bt,r) or solve2(mul,bt,r) or solve2(concat,bt,r)   

        
def part_1():
    cpt = 0
    with open("day_07.txt") as f:
        lines = [l.strip() for l in f.readlines()]
        for r,num in [l.split(":") for l in lines] :
            
            r = int(r)
            h,*t = [int(n.strip()) for n in num.strip().split(" ")]
            # print("======",r,"h=",h,"t=",t)
            if solve(h,t,r):
                cpt += r

    print(cpt)
def part_2():
    cpt = 0
    with open("day_07.txt") as f:
        lines = [l.strip() for l in f.readlines()]
        for r,num in [l.split(":") for l in lines] :
            
            r = int(r)
            h,*t = [int(n.strip()) for n in num.strip().split(" ")]
            # print("======",r,"h=",h,"t=",t)
            if solve2(h,t,r):
                cpt += r

    print(cpt)
part_1()
part_2()
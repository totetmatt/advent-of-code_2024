def rule(stones):
    for s in stones:
        l = len(str(s))
        if s == 0:
            yield 1
        elif l % 2 == 0:
            yield int(str(s)[:l//2])
            yield int(str(s)[l//2:])
        else:
            yield s * 2024

def rule2(stones):
    for s,nb in stones.items():
        l = len(str(s))
        if s == 0:
            yield (1,nb)
        elif l % 2 == 0:
            yield (int(str(s)[:l//2]),nb)
            yield (int(str(s)[l//2:]),nb)
        else:
            yield (s * 2024,nb)
def part_1():
    with open("day_11.txt") as f:
       stones = [int(s) for s in f.read().strip().split(" ")]
       for i in range(1,26):
           stones = list(rule(stones))
    print(len(stones))
def part_2():
    with open("day_11.txt") as f:
        stones = {int(s):1 for s in f.read().strip().split(" ")}

        for i in range(1,75):
            z = {}
            for s,v in rule2(stones):
                if s not in z:
                    z[s]= 0
                z[s]+=v
            stones = z
    cpt = 0
    for s,v in rule2(stones):
        cpt +=v 
    print(cpt)
part_1()
part_2()
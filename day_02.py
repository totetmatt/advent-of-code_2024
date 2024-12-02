def part_01():
    with open("day_02.txt") as f:
        lines = [[int(i) for i in s.strip().split(" ")] for s in f.readlines()]
        c = 0
        for line in lines:
            a = [ line[r]-line[r+1] for r in range(0,len(line)-1)]
            level = [0<abs(b)<=3 for b in a]
            cst = { b < 0  for b in a}
            
            if all(level) and len(cst)==1:
                c = c +1
        print(c)
def part_02():
    with open("day_02.txt") as f:
        lines = [[int(i) for i in s.strip().split(" ")] for s in f.readlines()]
        c = 0
        for linef in lines:

            ll = [  [l for i,l in enumerate(linef) if i !=  g]  for g in range(0,len(linef))]

            for line in ll:
                a = [ line[r]-line[r+1] for r in range(0,len(line)-1)]
                level = [0<abs(b)<=3 for b in a]
                cst = { b < 0  for b in a}
                
                if all(level) and len(cst)==1:
                    c = c +1
                    break
        print(c)

part_02()
    
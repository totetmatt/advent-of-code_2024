prgm = []
with open("day_13.txt") as f:
    
    data = [l.strip() for l in f.readlines()]
    for i in range(0,len(data),4) :
        a,b,p = data[i], data[i+1], data[i+2]
        prg = {}
        for k,v in [("A",a),("B",b),("P",p)]:
            prg[k]=([ int(a.strip()[2:]) for a in v.split(":")[-1].split(",")])

        prgm.append(prg)

arr = []
l = []
for p in prgm:
    arr.extend( [p['A'][0],p['A'][1],p['B'][0],p['B'][1],p['P'][0],p['P'][1],p['P'][0]+10000000000000,p['P'][1]+10000000000000])
a=','.join((str(b) for b in arr))
l = len(arr)
print(f"int l_input={l};")
print(f"long input[{l}]={{{a}}};")
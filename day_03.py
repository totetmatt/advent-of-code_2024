import re
def part_01():
    mul_re = re.compile(r"mul\(\d+,\d+\)")

    with open("day_03.txt") as f:
        cmd = f.read()
        x = [[int(i) for i in x[4:-1].split(",")] for x in mul_re.findall(cmd)]
        x = sum([ a[0]*a[1] for a in x])
        print(x)
def part_02():
    mul_re = re.compile(r"mul\(\d+,\d+\)|don't\(\)|do\(\)")

    with open("day_03.txt") as f:
        cmd = f.read()
        active = True
        cpt = 0
        for x in [x for x in mul_re.findall(cmd)]:
            if "don't()" in x :
                active = False
            elif "do()" in x :
                active = True
            elif active :
                a,b=[ int(y) for y in x[4:-1].split(",")]
                cpt += a*b
        print(cpt)
part_01()
part_02()
            

import functools
def solve_1(str,token):
    if not token:
        return False
    h,*t = token
    tmp = str.replace(h,"-")
    if len(set(tmp))==1:
        return True 
    return solve_1(tmp,t)
@functools.cache
def solve_11(string,template,index):
    if len(string) <= index:
        return True
    next = [tmpl for tmpl in template if string.startswith(tmpl,index)]
    if not next :
        return False
    return any([solve_11(string,template,index+len(x)) for x in next])
@functools.cache
def solve_2(string,template,index,cpt=0):
    if len(string) <= index:
        return 1+cpt
    next = [tmpl for tmpl in template if string.startswith(tmpl,index)]
    if not next :
        return cpt
    return sum([solve_2(string,template,index+len(x),cpt) for x in next])
def part_1():
    with open("day_19.test.txt") as f:
        head,tail = f.read().split("\n\n")
        patterns = sorted([h.strip() for h in head.strip().split(',')],key= lambda a:len(a),reverse=True)
        designs = [t.strip() for t in tail.strip().split("\n")]
        
        r = "|".join(patterns)
        cpt = 0
        for design in designs:
            if solve_11(design,tuple(patterns),0):
                cpt += 1
        print(cpt)

def part_2():
    with open("day_19.txt") as f:
        head,tail = f.read().split("\n\n")
        patterns = sorted([h.strip() for h in head.strip().split(',')],key= lambda a:len(a),reverse=True)
        designs = [t.strip() for t in tail.strip().split("\n")]

        cpt = 0
        for design in designs:
            cpt+=solve_2(design,tuple(patterns),0)
        print(cpt)

part_1()              
part_2()
#281 too high
#262 too low
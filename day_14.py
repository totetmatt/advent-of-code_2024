"""
The robots outside the actual bathroom are in a space which is
 101 tiles wide and 103 tiles tall (when viewed from above). 
 However, in this example, 
the robots are in a space which is only 11 tiles wide and 7 tiles tall.
"""
def part_1():
    with open("day_14.txt") as f:
        robot = []
        for l in [l.strip() for l in f.readlines()]:
            p,v =l.split()
            p=p[2:]
            v=v[2:]
            p = tuple([int(i) for i in p.split(",")])
            v= tuple([int(i) for i in v.split(",")])
          
            robot.append((p,v))
        width  = 101 # 11
        height = 103 # 7

        for s in range(1,10000):
            print(f"s={s}")
            robot = [  (( (px+vx)%width  if px+vx>=0 else width + (px+vx),
                          (py+vy)%height if py+vy>=0 else height + (py+vy)  
                         )
                         ,(vx,vy)) for ((px,py),(vx,vy)) in robot]
                         
            pos = ([a for a,_ in robot])
        
            for y in range(0,height):
                for x in range(0,width):
                    if (x,y) in pos:
                        print("1",end="")
                    else:
                        print(".",end="")
                print()
        hw = width//2
        hh = height//2
        cpt = {(True,True):0,(False,True):0,(True,False):0,(False,False):0}
        for (x,y) in pos:
            if x==hw or y==hh:
                continue
            cpt[(x<hw,y<hh)] += 1
        # print(cpt)
        gcpt = 1
        for x in cpt.values():
            gcpt*=x
        print(gcpt)
def part_2():
    with open("day_14.txt") as f:
        robot = []
        for l in [l.strip() for l in f.readlines()]:
            p,v =l.split()
            p=p[2:]
            v=v[2:]
            p = tuple([int(i) for i in p.split(",")])
            v= tuple([int(i) for i in v.split(",")])
          
            robot.append((p,v))
        width  = 101 # 11
        height = 103 # 7
        hw = width//2
        hh = height//2
        print(hw,hh)
        # 7257
        for s in range(4000,8000):

            robot = [  (( (px+vx)%width  if px+vx>=0 else width + (px+vx),
                          (py+vy)%height if py+vy>=0 else height + (py+vy)  
                         )
                         ,(vx,vy)) for ((px,py),(vx,vy)) in robot]
                         
            pos = set([a for a,_ in robot])
            if True:#and (hw-1,1) in pos and (hw+1,1) in pos :
                print(f"s={s}")
                for y in range(0,height):
                    for x in range(0,width):
                        if (x,y) in pos:
                            print("█",end="")
                        else:
                            print(" ",end="")
                    print()

        
part_1()
# part_2()
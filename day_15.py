DIR = {
    "^":(-1,0),
    "v":(1,0),
    ">":(0,1),
    "<":(0,-1)
}
def part_1():
    with open("day_15.txt") as f:
        mapdata,path =f.read().split("\n\n")
        
        mapdata = mapdata.split("\n")
        path = path.replace("\n","")
  
        MAP = {}
        ROBOT = None
        width = 0
        height = 0
        for y,l in enumerate(mapdata):
            for x,c in enumerate(l):
                width = max(width,x)
                height = max(height,y)
                MAP[(y,x)]=c
                if c == '@':
                    ROBOT = (y,x)
        width +=1
        height +=1
        # print(ROBOT)
        # print(path)
        # print(MAP)

        def move(el,pos,dir):
            
            # print(el,pos,dir)
            new = (pos[0]+dir[0],pos[1]+dir[1])
            e = MAP[new]
            if e == "#":
                return None
            if e == '.':
                MAP[pos] = "."
                MAP[new]= el
                if el == "@":
                    ROBOT = new
                return new
            if e == "O":
                if move(e,new,dir):
                    MAP[pos] = "."
                    MAP[new]= el
                    if el == "@":
                        ROBOT = new
                    return new 
                else :
                    return None  
        for en,dir in enumerate(path,start=1):
            # print(en,dir)
            dir = DIR[dir]
            # print(dir)
            if r:=move("@",ROBOT,dir) :
                ROBOT = r
    """for y in range(0,height):
        for x in range(0,width):
            print(MAP[(y,x)],end="")
        print()"""
    cpt = 0
    for ((y,x),c) in MAP.items():
        if c == "O":
            cpt += y*100+x
    print(cpt)
def part_2():
    with open("day_15.test.txt") as f:
        mapdata,path =f.read().split("\n\n")
        mapdata = mapdata.replace("O","[]")
        mapdata = mapdata.replace("#","##")
        mapdata = mapdata.replace(".","..")
        mapdata = mapdata.replace("@","@.")
        
        mapdata = mapdata.split("\n")
        path = path.replace("\n","")
    
        MAP = {}
        ROBOT = None
        width = 0
        height = 0
        for y,l in enumerate(mapdata):
            for x,c in enumerate(l):
                width = max(width,x)
                height = max(height,y)
                MAP[(y,x)]=c
                if c == '@':
                    ROBOT = (y,x)
        width +=1
        height +=1
        # print(ROBOT)
        # print(path)
        # print(MAP)
        for y in range(0,height):
            for x in range(0,width):
                print(MAP[(y,x)],end="")
            print()
        
        def move(el,pos,dir,lol=False):
            
            print(el,pos,dir)
            
            new = (pos[0]+dir[0],pos[1]+dir[1])


            e = MAP[new]
  
            if e == "#" :
                    return None
            if e == '.' :
                if el =="[" and abs(dir[0])== 1 and lol:
                    m = move("]",(pos[0],pos[1]+1),dir,True) 
                    if not m:
                        return None      
            
                if el =="]" and abs(dir[0])== 1 and lol:
                    m = move("[",(pos[0],pos[1]-1),dir,True) 
                    if not m:
                        return None 
                MAP[pos] = "."
                MAP[new]= el


                if el == "@":
                    ROBOT = new
                return new
            if e in ['[',']']:
                

                if move(e,new,dir):
                    if abs(dir[0])==1:
                        if e == "[":
                            extra = (new[0],new[1]+1)
                            extra= move("]",extra,dir)
                        else:
                            extra = (new[0],new[1]-1)
                            extra= move("[",extra,dir)
                    
                    MAP[pos] = "."
                    MAP[new]= el
                    if el == "@":
                        ROBOT = new
                    return new 
                else :
                    return None  
        for dir in path[:7]:
            # print(en,dir)
            dir = DIR[dir]
            # print(dir)
            if r:=move("@",ROBOT,dir) :
                ROBOT = r
            for y in range(0,height):
                for x in range(0,width):
                    print(MAP[(y,x)],end="")
                print()
            cpt = 0
    for ((y,x),c) in MAP.items():
        if c == "O":
            cpt += y*100+x
    print(cpt)            
part_1()
part_2()
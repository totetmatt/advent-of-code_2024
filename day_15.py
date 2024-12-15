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
        
        """def move(pos,dir):
        
            current = MAP[pos]
            n_pos = (pos[0]+dir[0],pos[1]+dir[1])
            if current == ".":
                return [pos]
            if current == "#":
                return []
            if dir[0]==0 and current in ['[',']']: # X moves, nothing particular
                return move(n_pos,dir) + [pos]
            if dir[1]==0 and current in ['[',']']: # Y move, problem
                if current == "[":
                    c1 = move(n_pos,dir)  + [pos]
                    if type(c1[0]) == list:
                        c1[1] = c1[1]+ [pos]
                    else :
                        c1 += [pos]
                    c2 = move((n_pos[0],n_pos[1]+1),dir) + [(pos[0],pos[1]+1)]
                if current == "]":
                    c1 = move(n_pos,dir)
                    
                    if type(c1[0]) == list:
                        c1[1] = c1[1]+ [pos]
                    else :
                        c1 += [pos]
                    c2 = move((n_pos[0],n_pos[1]-1),dir) + [(pos[0],pos[1]-1)]
                    
                if c1 and c2:
                    return  [c2] + [c1] 
                else :
                    return []
            if current == "@" and dir[0]==0:
                moves = move(n_pos,dir) 
                print(moves)
                if moves:
                    moves = moves +[pos]
                    for m in range(0,len(moves)-1):
                        MAP[moves[m]] = MAP[moves[m+1]]
                    MAP[pos] =  "."
                    return n_pos
            if current == "@" and dir[1]==0:
                moves = move(n_pos,dir) 
       
                print(moves)
                if moves:
                    moves = moves +[pos]
                    for m in range(0,len(moves)-1):
                        MAP[moves[m]] = MAP[moves[m+1]]
                       
                    MAP[pos] =  "."
                    return n_pos
        """
           
        def move(pos,dir,l=[]):
   
            current = MAP[pos]
            n_pos = (pos[0]+dir[0],pos[1]+dir[1])
            next = MAP[n_pos]
            print(pos,current,dir)
            if next in ["[","]"] and dir[0]==0:
                return move(n_pos,dir,[ [pos,n_pos] ] + l)
            if next in ["[","]"] and dir[1]==0:
                if next == "]":
                    return  move(n_pos,dir,[ [pos,n_pos] ]+ l)  +  move( (n_pos[0],n_pos[1]-1),dir,[ ]) 
                if next == "[":
                    return  move(n_pos,dir,[ [pos,n_pos] ]+ l)  +  move( (n_pos[0],n_pos[1]+1),dir,[ ]) +l    
            if next  == ".":
                return [[pos,n_pos]] +l 


                
                
        for dir in path[:6]:
            # print(en,dir)
            dir = DIR[dir]
            # print(dir)
            m =  move(ROBOT,dir)
            print(m)
            for p,np in  m:
                MAP[np]=MAP[p]
            last_p,last_np = m[-1]
            ROBOT = last_np
            MAP[last_p] = "."
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
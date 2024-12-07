def write_ppm(outfile,width,height,MAP,GUARD,PATH,ORIG):
    with open(outfile,"w") as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")
        for y in range(0,width):
            for x in range(0,height):
                if (y,x)==ORIG:
                    f.write("255 0 0\n")
                
                elif GUARD == (y,x) or (y,x) in PATH:
                        f.write("0 255 0\n")
    
                else:
                    if MAP[(y,x)]=="#":
                        f.write("255 255 255\n")
                    else :
                        f.write("0 0 0\n")
def frame(MAP,GUARD,PATH,ORIG,EXTRA=[]):
    map_width = max([x for _,x in MAP.keys()])+1
    map_height = max([y for y,_ in MAP.keys()])+1

    for y in range(0,map_width):
        for x in range(0,map_height):
            if (y,x)==ORIG:
                print("^",end="")
            
            elif GUARD == (y,x) or (y,x) in PATH:
                    print("X",end="")
            elif EXTRA == (y,x):
                print("O",end="")
            else:
                print(MAP[(y,x)],end="")
        print()
    print()
def rotate(dir):
    if dir == (-1,0):
        return (0,1)
    if dir == (0,1):
        return (1,0)
    if dir == (1,0):
        return (0,-1)
    if dir == (0,-1):
        return (-1,0)
def step(GUARD,GUARD_DIR):
    return (GUARD[0]+GUARD_DIR[0],GUARD[1]+GUARD_DIR[1])
def part_1():
    MAP = {}
    GUARD = None
    GUARD_DIR = None
    ORIG_GUARD = None 
    ORIG_DIR = None
    PATH = set()
    with open("day_06.txt") as f:
        
        for y,l in enumerate(f.readlines()):
            for x,c in enumerate(l.strip()):
                if c == "^":
                    MAP[(y,x)]="."
                    ORIG_GUARD=GUARD = (y,x)
                    PATH.add(GUARD)
                    ORIG_DIR=GUARD_DIR = (-1,0)
                else:
                    MAP[(y,x)]=c
        frame(MAP,GUARD,PATH,ORIG_GUARD)
        frame_counter = 0
        map_width = max([x for _,x in MAP.keys()])+1
        map_height = max([y for y,_ in MAP.keys()])+1
        write_ppm(f"render/day_06_{frame_counter:04d}.ppm",map_width,map_height,MAP,GUARD,PATH,ORIG_GUARD)
       
        while True:
            next = step(GUARD,GUARD_DIR)
            frame_counter += 1
            if  not (0<= next[0] < map_width and 0<= next[1] < map_height):
                break
            if MAP[next] == "#":
                GUARD_DIR = rotate(GUARD_DIR)
            else:
                GUARD = next
                PATH.add(GUARD)
            write_ppm(f"render/day_06_{frame_counter:04d}.ppm",map_width,map_height,MAP,GUARD,PATH,ORIG_GUARD)
       
            # frame(MAP,GUARD)

        print(len(set(PATH)))

def part_2():
    MAP = {}
    GUARD = None
    GUARD_DIR = None
    ORIG_GUARD = None 
    ORIG_DIR = None
    PATH = []
    with open("day_06.txt") as f:
        for y,l in enumerate(f.readlines()):
            for x,c in enumerate(l.strip()):
                if c == "^":
                    MAP[(y,x)]="."
                    ORIG_GUARD=GUARD = (y,x)
                    PATH.append(GUARD)
                    ORIG_DIR=GUARD_DIR = (-1,0)
                else:
                    MAP[(y,x)]=c
        frame(MAP,GUARD,PATH,ORIG_GUARD)
        map_width = max([x for _,x in MAP.keys()])+1
        map_height = max([y for y,_ in MAP.keys()])+1
        while True:
            next = step(GUARD,GUARD_DIR)
            if  not (0<= next[0] < map_width and 0<= next[1] < map_height):
                break
            if MAP[next] == "#":
                GUARD_DIR = rotate(GUARD_DIR)
            else:
                GUARD = next
                PATH.append(GUARD)

        cpt = 0       
        LOOP_BLOCK = []
        for extra in list(PATH[1:]):
            GUARD = ORIG_GUARD
            GUARD_DIR = ORIG_DIR
            PATH = []
            BLOCK = []

            while True:

                next = step(GUARD,GUARD_DIR)
                if  not (0<= next[0] < map_width and 0<= next[1] < map_height):
                    break
                if (next,GUARD_DIR) in BLOCK and next != ORIG_GUARD:
                    print("LOL")
                    cpt +=1
                    LOOP_BLOCK.append(extra)
                    # frame(MAP,GUARD,PATH,ORIG_GUARD,extra)
                    break
                if MAP[next] == "#" or next == extra:
                    BLOCK.append((next,GUARD_DIR))
                    GUARD_DIR = rotate(GUARD_DIR)
                else:
                    GUARD = next
                    PATH.append(GUARD)
            

        print(cpt,len(set(LOOP_BLOCK)))
part_1()
# part_2()
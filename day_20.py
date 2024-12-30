from collections import Counter
import animoc
def solve_1(start,end,map,width,height,dist={}, graph ={},frames=[]):
    frame = dict(map)
    to_visit = [start]
    visited = set()
    
    dist[start] = 0
    while end not in dist:
        current = to_visit.pop()
        nxt = [(y,x) for (y,x) in [ (current[0]-1,current[1]),
               (current[0]+1,current[1]),
               (current[0],current[1]-1),
               (current[0],current[1]+1)] if 0<=y<height and 0<=x<width and map[(y,x)]!="#" and (y,x) not in visited ]
        for n in nxt:
            dist[n] = dist[current] +1
            to_visit.append(n)
            graph[n]=current
        visited.add(current)
        # frame[current]="X"
        # frames.append(animoc.make_frame(width,height,frame,{'.':"0 0 0","#":'128 128 128','S':'0 255 0','E':'255 0 0','X':'255 255 255'}))
def part_1():
    with open("day_20.txt") as f:
        MAP={}
        START = None
        END = None
        for y,l in enumerate(f.readlines()):
            for x,c in enumerate(l.strip()):
                MAP[(y,x)]=c
                if c == "S":
                    START = (y,x)
                elif c =="E":
                    END = (y,x)
        width = max([x for _,x in MAP.keys()])+1
        height = max([y for y,_ in MAP.keys()])+1

        dist = {}
        graph = {}
        frames = []
        solve_1(START,END,MAP,width,height,dist,graph,frames)
        """for y in range(0,height):
            for x in range(0,width):
                if (y,x) in dist and MAP[(y,x)] not in ["S","E"]:
                    print("O",end="")
                else:
                    print(MAP[(y,x)].replace("#","░"),end="")
            print()"""
        # animoc.video(animoc.make_frame(width,height,MAP,{'.':"0 0 0","#":'128 128 128','S':'0 255 0','E':'255 0 0'}))
        candidate = [ ((y-1,x) ,(y,x) ,(y+1,x) )for ((y,x),c) in MAP.items() if c=="#" 
                     and 0<y<height-1 and 0<x<width-1  
                     and (  (MAP[(y-1,x)] !="#" and MAP[(y+1,x)] !="#")
                     )] + [ ((y,x-1) ,(y,x) ,(y,x+1) )for ((y,x),c) in MAP.items() if c=="#" 
                     and 0<y<height-1 and 0<x<width-1  
                     and (  (MAP[(y,x-1)] !="#" and MAP[(y,x+1)] !="#")
                     )] 

        cpt = Counter()
        for b,c,a in candidate:
            cpt[abs(dist[a]-dist[b])-2] +=1
            # frame = dict(MAP)
            # MAP[c]="@"
            # frames.append(animoc.make_frame(width,height,frame,{'.':"0 0 0","#":'128 128 128','S':'0 255 0','E':'255 0 0','X':'255 255 255','@':'255 0 0'}))
        # animoc.video("".join(frames))
        print(sum([v for k,v in cpt.items() if k >= 100]))
def part_2():
    with open("day_20.txt") as f:
        MAP={}
        START = None
        END = None
        for y,l in enumerate(f.readlines()):
            for x,c in enumerate(l.strip()):
                MAP[(y,x)]=c
                if c == "S":
                    START = (y,x)
                elif c =="E":
                    END = (y,x)
        width = max([x for _,x in MAP.keys()])+1
        height = max([y for y,_ in MAP.keys()])+1

        dist = {}
        graph = {}
        solve_1(START,END,MAP,width,height,dist,graph)
        """for y in range(0,height):
            for x in range(0,width):
                if (y,x) in dist and MAP[(y,x)] not in ["S","E"]:
                    print("O",end="")
                else:
                    print(MAP[(y,x)].replace("#","░"),end="")
            print()"""
        """t_y,t_x = (1,7)
        mx = 2
        candidate = [ ((dist[(y,x)]-dist[(t_y,t_x)]),abs(y-t_y)+abs(x-t_x)) for ((y,x),c) in MAP.items() if c!="#"
                        and (abs(y-t_y)+abs(x-t_x) <= mx and dist[(y,x)]-dist[(t_y,t_x)] >0 and  (abs(dist[(y,x)]-dist[(t_y,t_x)])!=abs(y-t_y)+abs(x-t_x)))
                     ]
        print(candidate)"""

        mx = 20
        from collections import Counter
        cpt = Counter()
        for t_y,t_x in [ (y,x) for ((y,x),c) in MAP.items() if c != "#"]:
            candidate = [ (dist[(y,x)]-dist[(t_y,t_x)])-(abs(y-t_y)+abs(x-t_x)) 
                           for ((y,x),c) in MAP.items() if c!="#"
                            and (abs(y-t_y)+abs(x-t_x) <= mx 
                                 and dist[(y,x)]-dist[(t_y,t_x)] >0 and  (abs(dist[(y,x)]-dist[(t_y,t_x)])!=abs(y-t_y)+abs(x-t_x)))
                        ]
            cpt.update(candidate)
        """for (ps,c) in sorted([ (ps,c) for (ps,c) in cpt.items()]):
            if 50<= ps <=76:
                print(c,ps)"""


        print(sum([v for k,v in cpt.items() if k >= 100]))

part_1()
part_2()
import animoc
FRAMES =[]
def part_1():
    with open("day_18.txt") as f:
        try:
            data = [tuple([int(i) for i in l.strip().split(",")]) for l in f.readlines()]
            #XY
            width = 71
            height = 71
            s = []
            for r in range(0,len(data)):
                print("==",r,"==")
                print(data[r-1])
                if s and all([ x not in set(data[:r]) for x in s ]):
                    continue
                start = (0,0)
                end = (width-1,height-1)
                to_visit = [(0,0)]
                visited = set()
                graph ={}
                dist = {start:0}
                while end not in dist:
                    to_visit.sort(key=lambda x:dist[x])
                    current = to_visit.pop(0)
                    n = [(current[0]+1,current[1]),(current[0]-1,current[1]),(current[0],current[1]+1),(current[0],current[1]-1)]
                
                    n = [ x for x in n if x not in visited and x not in data[:r] and 0 <=x[0]<width and 0<=x[1]<height]
                    # print(current, ">>",n)
                    for x in n:
                        if dist[current]+1 < dist.get(x,10000000):
                            dist[x]=  dist[current]+1
                            graph[x] = current
                            to_visit.append(x)
                    visited.add(current)
                s = [end]
                g = end
                while g:=graph.get(g):
                    s.append(g)
                # print(s)
                mmap={}
                for y in range(0,height):
                    for x in range(0,width):
                        if (x,y) in data[:r]:
                            print("▒",end="")
                            mmap[(y,x)]="▒"
                        elif (x,y) in s:
                            print("×",end="")
                            mmap[(y,x)]="×"
                        else:
                            print("░",end="")
                            mmap[(y,x)]="░"
                    print()
                if r == 1024:
                    print(dist[end],len(s))
                FRAMES.append(animoc.make_frame(71,71,mmap,{'▒':'128 128 128','×':'255 0 0'}))
        except :
            pass
    animoc.video("".join(FRAMES))
           
        

part_1()
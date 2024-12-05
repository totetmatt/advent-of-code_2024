

def part_1():
    def dir(init,size_wh):
        x,y = init
        w,h = size_wh
        up = [(x,y-i) for i in range(0,4) if  y-i >=0]
        down = [(x,y+i) for i in range(0,4) if y+i < h]
        left = [(x-i,y) for i in range(0,4) if x-i >=0 ]
        right = [(x+i,y) for i in range(0,4) if x+i < w]
        up_left =  [(x-i,y-i) for i in range(0,4) if  y-i >=0 and x-i >=0]
        up_right =  [(x+i,y-i) for i in range(0,4) if  y-i >=0 and  x+i < w]
        down_left =  [(x-i,y+i) for i in range(0,4) if  y+i < h and x-i >=0]
        down_right =  [(x+i,y+i) for i in range(0,4) if  y+i < h and x+i < w]
        return [s for s in [up,down,left,right,up_left,up_right,down_left,down_right] if len(s) == 4]
    with open("day_04.txt") as f:
        data = [s.strip() for s in f.readlines()]
        s_width = len(data[0])
        s_height = len(data)
        board = {}
        for y,l in enumerate(data):
            for x,c in enumerate(l):
                board[(x,y)] = c
        cpt = 0
        sols = set()
        for coord,c in board.items():
            if c=="X":
                z = [(s,"".join([ board[t]  for t in s])) for s in  dir(coord,(s_width,s_height))]
                z = [(s,a) for s,a in z if a == "XMAS"]
                cpt +=len(z)
                for s,_ in z:
                    sols.update(s)
        for y in range(0,s_height):
            for x in range(0,s_width):
                if (x,y) in sols:
                    print(board[(x,y)],end="")
                else:
                    print(".",end="")
            print()
        print(cpt)
def part_2():
    def dir(init,size_wh):
        """
         -1,-1  0,-1 1,-1
         -1,0   0,0  1,0
         -1,1   0,+1 1,1   
        """
        x,y = init
        w,h = size_wh
        d_up_right = [c for c in [(x-1,y-1), (x,y) ,(x+1,y+1)] if  0<=x-1 and x+1<s_width and 0<=y-1 and y+1<s_height] 
        d_down_left = [c for c in [ (x+1,y-1), (x,y) ,(x-1,y+1)] if  0<=x-1 and x+1<s_width and 0<=y-1 and y+1<s_height] 

        return [d_up_right,d_down_left]
    with open("day_04.txt") as f:
        # 2318 too high
        data = [s.strip() for s in f.readlines()]
        s_width = len(data[0])
        s_height = len(data)
        board = {}
        for y,l in enumerate(data):
            for x,c in enumerate(l):
                board[(x,y)] = c
        cpt = 0
        sols = set()

        for coord,c in board.items():
            if c == "A":
                x_shape = dir(coord,(s_width,s_height))

                if x_shape[0] and x_shape[1] and {'M','A','S'} == {board[cr] for cr in x_shape[0]} and {board[cr] for cr in x_shape[0]} == {board[cr] for cr in x_shape[1]}:
                    cpt += 1
                    print(c,coord)
                    sols.update(x_shape[0])
                    sols.update(x_shape[1])
                    
        for y in range(0,s_height):
            for x in range(0,s_width):
                if (x,y) in sols:
                    print(board[(x,y)],end="")
                else:
                    print(".",end="")
            print()
        print(cpt)
part_1()
part_2()
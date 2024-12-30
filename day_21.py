"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
    <<vAA>A>^AAvA<^A>AAvA^A<vA>^A<A>A<vA>^A<A>A<<vA>A>^AAvA<^A>A
    <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A EX

"""
NUMPAD={
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),
    '0': (3,1),
    'A': (3,2),
    '': (3,0)
}

DIRPAD = {
    '^': (0,1),
    'A': (0,2),
    '<': (1,0),
    'v': (1,1),
    '>': (1,2),
    '' : (0,0)
}
DIRTOK = {
  (-1,0): '^',
  (1,0): 'v',
  (0,-1): '<',
  (0,1) : '>'
  
}
def solve_1(pad,sequence):
    current = pad['A']
    forbid = pad['']
    seq = []
    for s in sequence:
        dir =  (pad[s][0] - current[0],pad[s][1]-current[1])
        if (current[0] == forbid[0] and abs(current[0]-dir[0]) == 0) or \
        (current[1] == forbid[1] and abs(current[1]-dir[1]) == 0):
            dir = (dir[1],dir[0])
        if dir[1] !=0:
            seq += int(abs(dir[1])) * DIRTOK[(0,dir[1]/abs(dir[1]))]
        if dir[0] !=0:
            seq += int(abs(dir[0])) * DIRTOK[(dir[0]/abs(dir[0]),0)]
        seq += "A"
        current = pad[s]
    return seq
def part_1():
    """
    68 * 29 
    60 * 980 
    68 * 179 
    64 * 456
    64 * 379
    """
    cpt = 0
    with open("day_21.test.txt") as f:
        for code in f.readlines():
            code = code.strip()
            print('------')
            print(code)
            seq = solve_1(NUMPAD,code)
            # print("".join(seq))
            seq = solve_1(DIRPAD,seq)
            # print("".join(seq))
            seq = solve_1(DIRPAD,seq)
            # print("".join(seq))
            print(len(seq),'*',int("".join([c for c in code if c.isdigit()])))
            cpt += (len(seq)*int("".join([c for c in code if c.isdigit()])))
    print(cpt)

part_1()
# too low 195348
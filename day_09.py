def part_1():
    with open('day_09.txt') as f:
        data = f.read().strip()
        mem = []
        for idx,d in enumerate(data):
            if idx%2 ==0: # File
                mem.extend([f'{idx//2}']*int(d))
            else: #free space
                mem.extend( [f'.']*int(d))

        mem = [ m for m in list(mem) if m]
        l_ptr = 0
        r_ptr = len(mem)-1
        while l_ptr <= r_ptr:
            if mem[l_ptr] != ".":
                l_ptr += 1
                continue

            if mem[r_ptr] == ".":
                r_ptr -= 1
                continue

            mem[l_ptr],mem[r_ptr] = mem[r_ptr],mem[l_ptr]
            l_ptr += 1 
            r_ptr -= 1
        cpt = 0  
        for idx,c in enumerate(mem):
            if c == ".":
                continue 
            cpt += idx*int(c)
        print(cpt)
    
def part_2():
    with open('day_09.txt') as f:
        data = f.read().strip()
        mem = []
        for idx,d in enumerate(data):
            if idx%2 ==0: # File
                mem.append([f'{idx//2}']*int(d))
            else: #free space
                mem.append( [f'.']*int(d))

        mem = [ list(m) for m in list(mem) if m]




        # print("|".join([''.join(m) for m in mem]))
        for id in reversed([m[0] for m in mem if m[0]!="."]):
            ##print(f"==={id}===")
            ##print(mem)
            l_ptr = 0
            r_ptr = len(mem)-1     
            #print(r_ptr)
            while mem[r_ptr][0] != id:

                r_ptr -= 1
            #print(f"r_ptr:[{r_ptr}] {mem[r_ptr]}")
            len_file = len(mem[r_ptr])

            while l_ptr<r_ptr and not (mem[l_ptr][0] == "." and len_file <= len(mem[l_ptr])):

                l_ptr+=1
            if l_ptr >=len(mem):
                #print("no place")
                continue
            #print(f"l_ptr:[{l_ptr}] {mem[l_ptr]}")
            len_free = len(mem[l_ptr])
            if len_file == len_free:
                mem[l_ptr],mem[r_ptr]=(mem[r_ptr],mem[l_ptr])
            else:
                free_filled,free_remain = mem[l_ptr][:len_file], mem[l_ptr][:len_free-len_file]

                new = [mem[r_ptr], free_remain]
             
                mem = [x for x in mem[:l_ptr] + new + mem[l_ptr+1:r_ptr] + [free_filled] + mem[r_ptr+1:] if x != []]


        r = []
        # print("|".join([''.join(m) for m in mem]))
        for m in mem:
            for n in m:
                r.append(n)
        print(r)

        cpt = 0  
        for idx,c in enumerate(r):
            if c == ".":
                continue 
            cpt += idx*int(c)

        print(cpt)
part_1()
part_2()
"""

   
"""
def prune(secret):
    return secret%16777216
def mix(x,secret):
    r = x^secret
    return r
def rnd(secret):
    # Calculate the result of multiplying the secret number by 64. 
    #   Then, mix this result into the secret number. 
    #   Finally, prune the secret number.
   
    secret_1 = secret*64
    secret_2 = mix(secret_1,secret)
    secret_3 = prune(secret_2)

    #  Calculate the result of dividing the secret number by 32. 
    # Round the result down to the nearest integer.
    #  Then, mix this result into the secret number. 
    # Finally, prune the secret number.
    secret_4 = secret_3 //32
    secret_5 = mix(secret_4, secret_3)
    secret_6 = prune(secret_5)

    #  Calculate the result of multiplying the secret number by 2048.
    # Then, mix this result into the secret number. 
    # Finally, prune the secret number.
    secret_7 = secret_6 * 2048
    secret_8 = mix(secret_7, secret_6)
    secret_9 = prune(secret_8)
    return secret_9
def part_1():
    with open("day_22.txt") as f:
        cpt = 0
        for l in f.readlines():
            s =  start = int(l.strip())
            for r in range(1,2001):
                s = rnd(s)
            # print(start,s)
            cpt += s
        print(cpt)
def part_2():
    with open("day_22.txt") as f:
        cpt = 0
        sellers = []
        for l in f.readlines():
            s = int(l.strip())
            sellers.append(s)
        seqs = {} # tuple(seq) => price idx seller
        # print(seqs)
        maxx = 0
        for idx,s in enumerate(sellers):
            win = [s-((s//10)*10)]
            for r in range(0,2000):
                
                """if len(win) != 1:
                    print(s, win[-1], f'({win[-1]-win[-2]})')
                else:
                    print(s, win[-1])"""
                s = rnd(s)
                d = s-((s//10)*10)
                win.append(d)
                if len(win) >5:
                    win = win[1:]
                if len(win) == 5:
                    dif = tuple(win[r+1]-win[r] for r in range(0,4))
                    if not seqs.get(dif):
                        seqs[dif] = [0]*len(sellers)

                    seqs[dif][idx] = d
                    maxx =max(sum(seqs[dif]),maxx)
                
            # print(seqs)
        
        print(maxx)
# part_1() 
part_2()
# too high 2450
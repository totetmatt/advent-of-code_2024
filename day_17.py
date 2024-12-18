def part_1():

    REG = {
        "A":0,
        "B":0,
        "C":0
    }
    def combo(a):
        if a <=3 :
            return a
        return {
            4: REG["A"],
            5: REG["B"],
            6: REG["C"],
            
        }[a]
    OPNAME = { # For debug
        "0" : "adv",
        "1" : "bxl",
        "2" : "bst",
        "3" : "jnz",
        "4" : "bxc",
        "5" : "out",
        "6" : "bdv",
        "7" : "cdv"
    }
    OPCODE = {
        "0" : lambda a: (REG.update({"A":REG["A"]//(2**combo(a))}),None),
        "1" : lambda a: (REG.update({"B":REG["B"]^a}),None),
        "2" : lambda a: (REG.update({"B":combo(a)%8}),None),
        "3" : lambda a: (None ,None if REG["A"]==0 else a),
        "4" : lambda _: (REG.update({"B": REG["B"]^REG['C']}),None),
        "5" : lambda a: (f"{combo(a)%8}",None),
        "6" : lambda a: (REG.update({"B":REG["A"]//(2**combo(a))}),None),
        "7" : lambda a: (REG.update({"C":REG["A"]//(2**combo(a))}),None)
    }
    with open("day_17.txt") as f:
        registers,program  =f.read().split("\n\n")
        regs = registers.split("\n")
        IP = 0
        for reg in regs:
            _,rname,rval = reg.split()
            rname = rname.replace(":","")
            rval = int(rval)
            REG[rname] = rval
        ins = program.split()[-1].split(",")
        stdout = []
        print(ins)
        print(REG)
        while IP+1 < len(ins):

            opc,opr = ins[IP:IP+2]

            # print(">>",f'{OPNAME[opc]}({opc})', opr)
            ret,ipj = OPCODE[opc](int(opr))
            # print(REG)
            # print("<<",ret,ipj )
            if ret:
                stdout.append(ret)
            if ipj  is not None:
                IP = ipj
            else:    
                IP += 2
        print("STDOUT",",".join(stdout))
def part_2():

    REG = {
        "A":0,
        "B":0,
        "C":0
    }
    def combo(a):
        if a <=3 :
            return a
        return {
            4: REG["A"],
            5: REG["B"],
            6: REG["C"],
            
        }[a]
    OPNAME = { # For debug
        "0" : "adv",
        "1" : "bxl",
        "2" : "bst",
        "3" : "jnz",
        "4" : "bxc",
        "5" : "out",
        "6" : "bdv",
        "7" : "cdv"
    }
    OPCODE = {
        "0" : lambda a: (REG.update({"A":REG["A"]//(2**combo(a))}),None),
        "1" : lambda a: (REG.update({"B":REG["B"]^a}),None),
        "2" : lambda a: (REG.update({"B":combo(a)%8}),None),
        "3" : lambda a: (None ,None if REG["A"]==0 else a),
        "4" : lambda _: (REG.update({"B": REG["B"]^REG['C']}),None),
        "5" : lambda a: (f"{combo(a)%8}",None),
        "6" : lambda a: (REG.update({"B":REG["A"]//(2**combo(a))}),None),
        "7" : lambda a: (REG.update({"C":REG["A"]//(2**combo(a))}),None)
    }
    with open("day_17.txt") as f:
        registers,program  =f.read().split("\n\n")
        regs = registers.split("\n")
        
        for reg in regs:
            _,rname,rval = reg.split()
            rname = rname.replace(":","")
            rval = int(rval)
            REG[rname] = rval
        ins = program.split()[-1].split(",")
        stdout = []
        # print(ins)
        # print(REG)
        ORIGREG = REG


        found = None
        REG["A"] =117440
        att =REG["A"] 
        while found is None:
            IP = 0
            stdout = []
            REG = ORIGREG
            REG["A"] = att
            print(f'{att:03b}',att)
            while IP+1 < len(ins):

                opc,opr = ins[IP:IP+2]

                # print(">>",f'{OPNAME[opc]}({opc})', opr)
                ret,ipj = OPCODE[opc](int(opr))
                # print(REG)
                # print("<<",ret,ipj )
                if ret:
                    stdout.append(ret)
                    if stdout != ins[:len(stdout)]:
                        # print(stdout)
                        # print(ins[:len(stdout)])
                        # print("NOK")
                        break
                if ipj  is not None:
                    IP = ipj
                else:    
                    IP += 2
            if stdout == ins:
                print("FOUND")
                found = att
            else:
                att += 1
                print("NOT FOUND")

            print("".join([f'{int(i):03b}'  for i in ins]))
            print("".join([f'{int(i):03b}' for i in stdout]))

        # print(att)
# part_1()
part_2()

def part_1():
    rule_set = {}
    cpt = 0
    with open("day_05.txt") as f:
        data = f.read()
        rules,updates=  data.split("\n\n")
        for source,target in [r.split("|") for r in rules.split("\n")]:
            if source not in rule_set:
                rule_set[source]=set()
            rule_set[source].add(target)
        for update in[u.split(",") for u in updates.split("\n")]:
            if update[0] == '':
                continue
            correct = True
            for i in range(0,len(update)):
                rule = rule_set.get(update[i],"")
                tail = set(update[i+1:])
                correct = all([ t in rule for t in tail])
                if not correct:
                    break
                # print(update[i],all([ t in rule for t in tail]))
            if correct:
                cpt += int(update[len(update)//2])
    print(cpt)
def part_2():
    rule_set = {}
    cpt = 0
    with open("day_05.txt") as f:
        data = f.read()
        rules,updates=  data.split("\n\n")
        for source,target in [r.split("|") for r in rules.split("\n")]:
            if source not in rule_set:
                rule_set[source]=set()
            rule_set[source].add(target)
        for update in[u.split(",") for u in updates.split("\n")][:]:
            if update[0] == '':
                continue
            was_incorrect = False
            for i in range(0,len(update)):
                rule = rule_set.get(update[i],"")
                tail = set(update[i+1:])
                correct = all([ t in rule for t in tail])
                if correct:
                    continue
                was_incorrect = True
                while not correct:
                    not_correct = ([ t for t in tail if t not in rule])
                    if not_correct:
                        switch_idx = (max([update.index(n) for n in not_correct]))
                        update[i],update[switch_idx]=(update[switch_idx],update[i])

                    rule = rule_set.get(update[i],"")
                    tail = set(update[i+1:])
                    correct = all([ t in rule for t in tail])

  
            if  was_incorrect:
                cpt += int(update[len(update)//2])
    print(cpt)
part_1()
part_2()
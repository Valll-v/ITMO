import random


MATRIX = [
    [0, 1, 1, 5,  3],
    [1, 0, 3, 1,  5],
    [1, 3, 0, 11, 1],
    [5, 1, 11, 0, 1],
    [3, 5, 1, 1,  0],
]


def select(pop1, pop2):
    choice = random.choice([1, 2, 3, 4, 5])
    res1 = pop1[:choice]
    res2 = pop2[:choice]
    for i in range(choice, 5):
        if pop1[i] not in res2:
            res2.append(pop1[i])
        if pop2[i] not in res1:
            res1.append(pop2[i])
    for i in range(5):
        if pop1[i] not in res1:
            res1.append(pop1[i])
        if pop2[i] not in res2:
            res2.append(pop2[i])
    return [res1, res2]


def target_func(pop):
    res = 0
    for i in range(5):
        res += MATRIX[pop[i - 1]][pop[i]]
    return res


def mutate(pops, e=0.01):
    for pop in pops:
        if random.random() <= e:
            print('Mutate!')
            a, i = random.randint(0, 4), random.randint(1, 4)
            pop[a], pop[a - i] = pop[a - i], pop[a]
    return pops


def gen_init_pops(n):
    init_pop = [0, 1, 2, 3, 4]
    pops = [init_pop]
    for _ in range(n - 1):
        i = random.randint(1, 4)
        new_pop = pops[-1][:]
        new_pop[i], new_pop[i - 1] = new_pop[i - 1], new_pop[i]
        pops.append(new_pop)
    return pops


def main():
    n = 4
    pops = gen_init_pops(n)
    print('Init pops:')
    print(pops)
    for i in range(100):
        pops = mutate(pops)
        print('Pops after mutate')
        print(pops)
        a1, b1, a2, b2 = random.choice([(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)])
        print(f'Parents: {a1} & {b1} | {a2} & {b2}')
        pops += select(pops[a1], pops[b1])
        pops += select(pops[a2], pops[b2])
        print(f'Extended pops:')
        print(pops)
        pops = sorted(pops, key=target_func)[:4]
        print(f'New best pops:')
        print(pops)
    print('Best pop:')
    print([i + 1 for i in pops[0]])
    print('Best distance: ', target_func(pops[0]))



main()

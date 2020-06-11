import random


def generate_random():
    child = []
    while len(child) < 8:
        num = random.randint(1, 8)
        child.append(num)
    return child


def generate_grid(array):
    grid = [[0 for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            if i+1 == array[j]:
                grid[i][j] = 1
    return grid


def cal_fitness(chromosome, grid):
    gcount = 0
    for i in range(8):
        num = chromosome[i]
        count = 0
        for j in range(8):
            if j != i & chromosome[j] == num:
                count += 1

        # top right
        col = i
        row = num - 1
        for j in range(8):
            if row > 0 and col < 7:
                if row+1 != num:
                    if grid[row][col] == 1:
                        count += 1
            row -= 1
            col += 1

        # top left
        row = num - 1
        col = i
        for j in range(8):
            if row > 0 and col > 0:
                if row+1 != num:
                    if grid[row][col] == 1:
                        count += 1
            row -= 1
            col -= 1

        # bottom left
        row = num - 1
        col = i
        for j in range(8):
            if row < 7 and col < 7:
                if row + 1 != num:
                    if grid[row][col] == 1:
                        count += 1
            row += 1
            col -= 1

        # bottom right
        row = num - 1
        col = i
        for j in range(8):
            if row < 7 and col < 7:
                if row + 1 != num:
                    if grid[row][col] == 1:
                        count += 1
            row += 1
            col += 1

        if count > 0:
            gcount += 1

    return 8 - gcount


def roulette_wheel():
    parents.clear()
    probabilities.clear()

    sum = 0
    fitt = 0

    for i in range(len(population)):

        fit, c = population[i]
        sum += fit

    for i in range(len(population)):
        fit, chr = population[i]
        fitness = round((fit/sum), 2)

        fitt += fitness
        probabilities.append(fitt)

    p1 = random.choice(probabilities)
    for i in range(len(probabilities)):
        if p1 == probabilities[i]:
            fit, chr = population[i]
            parents.append(list(chr))
            break

    p2 = random.choice(probabilities)
    while p2 == p1:
        p2 = random.choice(probabilities)
    for i in range(len(probabilities)):
        if p2 == probabilities[i]:
            fit, chr = population[i]
            parents.append(list(chr))
            break


def one_point_crossover():
    offspring1 = []
    offspring2 = []
    parent1 = parents[0]
    parent2 = parents[1]
    for i in range(len(parent1)):
        if i < 4:
            offspring1.append(parent1[i])
            offspring2.append(parent2[i])
        else:
            offspring1.append(parent2[i])
            offspring2.append(parent1[i])
    return offspring1, offspring2


def mutation(array):
    child = []
    for i in range(0, 2):
        r = random.randint(0, 7)

        ranint = bin(array[r])

        if len(ranint) == 3:
            templist = list(ranint)
            templist.append('1')
            ranint = ''.join(templist)
            ranint = int(ranint, 2)
        elif len(ranint) == 4:
            templist = list(ranint)

            r = random.randint(2, 3)

            if r != 2 or r == 3:
                if templist[r] == '0':
                    templist[r] = '1'
                else:
                    templist[r] = '0'
            else:
                templist.append('1')
            ranint = ''.join(templist)

            ranint = int(ranint, 2)

        elif len(ranint) == 5:
            templist = list(ranint)

            if templist[3] == '0':
                templist[3] = '1'
            else:
                templist[3] = '0'
            if templist[4] == '0':
                templist[4] = '1'
            else:
                templist[4] = '0'

            ranint = ''.join(templist)
            ranint = int(ranint, 2)

        elif len(ranint) == 6:
            templist = list(ranint)
            if templist[2] == '1':
                templist[2] = '0'
                a = random.randint(3, 5)
                if templist[a] == '0':
                    templist[a] = '1'
                b = random.randint(3, 5)
                if templist[b] == '0':
                    templist[b] = '1'
            ranint = ''.join(templist)
            ranint = int(ranint, 2)
        array[r] = ranint

    child = array
    return child


def populationgen():
    child = generate_random()
    grid = generate_grid(child)
    fitness = cal_fitness(child, grid)
    population.append((fitness, child))
    print(child, fitness)


def algo():
    populationgen()
    chromosome = []
    fit = 0
    i = 0
    a = 0
    while fit <= 7:
        if len(population) > 100:
            population.pop(0)

        roulette_wheel()
        offspring1, offspring2 = one_point_crossover()

        newpop1 = mutation(offspring1)
        newpop2 = mutation(offspring2)
        grid = generate_grid(newpop1)
        fitness = cal_fitness(newpop1, grid)
        offspring = (fitness, newpop1)
        grid = generate_grid(offspring2)
        fitness2 = cal_fitness(newpop2, grid)
        if fitness > fitness2:
            population.append(offspring)
            fit = fitness
        else:
            offspring = (fitness2, newpop2)
            population.append(offspring)
            fit = fitness2

        a, chromosome = offspring
        print('iteration =', i, 'chromosome: ', chromosome, 'fitness =', fit)
        # print(fit)
        population.sort()

        i += 1
        a += 1
        if a > 2500:
            populationgen()
            a = 0

        if i > 25000:  # to limit no of iterations
            if fit >= 6:
                break

    print(chromosome)


# driver code

population = []
parents = []
probabilities = []
algo()

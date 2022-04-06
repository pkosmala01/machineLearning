import random
from math import sin


def StartingPop(dim, length, size):
    pop = []
    for i in range(size):
        element = ""
        for j in range(dim):
            s = ""
            for k in range(length):
                s += random.choice(['0', '1'])
            element += s
        pop.append(element)
    return pop


def CalcFunction(variable, code):
    x1 = code[variable[:5]]
    x2 = code[variable[5:10]]
    x3 = code[variable[10:15]]
    x4 = code[variable[15:]]
    result = (x1+2*x2-7)**2 + (2*x1+x2-5)**2 + (sin(1.5*x3))**3 + (x3-1)**2 * (1+(sin(1.5*x4))**2) + (x4-1)**2 * (1+(sin(x4))**2)
    return result


def Evaluate(elemList, code):
    evalList = []
    for element in elemList:
        evalList.append(CalcFunction(element, code))
    return evalList


def Reproduce(evals, pop, size):
    tempEvals = []
    for x in evals:
        tempEvals.append(-x + max(evals) + 1)
    tempSum = sum(tempEvals)
    probabilities = []
    probSum = 0
    for x in tempEvals:
        probabilities.append(x/tempSum + probSum)
        probSum += x/tempSum
    newPop = []
    for x in range(size):
        rand = random.random()
        for prob in probabilities:
            if rand < prob:
                newPop.append(pop[probabilities.index(prob)])
                break
    return newPop


def Crossover(pop, prob):
    for x in range(len(pop)//2):
        rand = random.random()
        if rand < prob:
            parentsIndex = (random.randint(0, len(pop)-1), random.randint(0, len(pop)-1))
            cutPoint = random.randint(0, 20)
            child1 = pop[parentsIndex[0]][:cutPoint] + pop[parentsIndex[1]][cutPoint:]
            child2 = pop[parentsIndex[1]][:cutPoint] + pop[parentsIndex[0]][cutPoint:]
            pop[parentsIndex[0]] = child1
            pop[parentsIndex[1]] = child2
    return pop


def Mutation(pop, prob):
    for element in pop:
        for bit in range(len(element)):
            rand = random.random()
            if rand < prob:
                if element[bit] == '0':
                    element = element[:bit] + '1' + element[bit:]
                else:
                    element = element[:bit] + '0' + element[bit:]
    return pop


def HollandAlg(codeDict, limit, popSize, dimensions, crossProb, mutProb):
    iter = 0
    pop = StartingPop(dimensions, 5, popSize)
    evalList = Evaluate(pop, codeDict)
    evalResult = min(evalList)
    elementResult = pop[evalList.index(evalResult)]
    while iter < limit:
        pop = Reproduce(evalList, pop, popSize)
        pop = Crossover(pop, crossProb)
        pop = Mutation(pop, mutProb)
        evalList = Evaluate(pop, codeDict)
        if min(evalList) < evalResult:
            evalResult = min(evalList)
            elementResult = pop[evalList.index(evalResult)]
        iter += 1
    return evalResult, elementResult


if __name__ == "__main__":
    graysCode = {"00000": -16, "00001": -15, "00011": -14, "00010": -13,
                 "00110": -12, "00100": -11, "01100": -10, "01000": -9,
                 "11000": -8, "10000": -7, "10001": -6, "10101": -5,
                 "10100": -4, "10110": -3, "10010": -2, "11010": -1,
                 "01010": 0, "01011": 1, "01001": 2, "01101": 3,
                 "00101": 4, "00111": 5, "01111": 6, "01110": 7,
                 "11110": 8, "11100": 9, "11101": 10, "11001": 11,
                 "11011": 12, "10011": 13, "10111": 14, "11111": 15}
    limit = 500
    popSize = 100
    minimum = HollandAlg(graysCode, limit, popSize, 4, 0.8, 0.05)
    print(minimum)

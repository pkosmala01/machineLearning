import time
import statistics
from geneticHolland import HollandAlg


graysCode = {"00000": -16, "00001": -15, "00011": -14, "00010": -13,
             "00110": -12, "00100": -11, "01100": -10, "01000": -9,
             "11000": -8, "10000": -7, "10001": -6, "10101": -5,
             "10100": -4, "10110": -3, "10010": -2, "11010": -1,
             "01010": 0, "01011": 1, "01001": 2, "01101": 3,
             "00101": 4, "00111": 5, "01111": 6, "01110": 7,
             "11110": 8, "11100": 9, "11101": 10, "11001": 11,
             "11011": 12, "10011": 13, "10111": 14, "11111": 15}


def PrintResults(resultList, times):
    print(statistics.mean(resultList), statistics.stdev(resultList), statistics.mean(times))


def SmallPopSize():
    resultList = []
    times = []
    limit = 500
    popSize = 100
    mutProb = 0.05
    crossProb = 0.5
    dim = 4
    for x in range(25):
        start = time.time()
        resultList.append(HollandAlg(graysCode, limit, popSize, dim, crossProb, mutProb)[0])
        times.append(time.time() - start)
    PrintResults(resultList, times)


def LargePopSize():
    resultList = []
    times = []
    limit = 500
    popSize = 1000
    mutProb = 0.05
    crossProb = 0.5
    dim = 4
    for x in range(25):
        start = time.time()
        resultList.append(HollandAlg(graysCode, limit, popSize, dim, crossProb, mutProb)[0])
        times.append(time.time() - start)
    PrintResults(resultList, times)


def SmallerCrossoverProbability():
    resultList = []
    times = []
    limit = 500
    popSize = 1000
    mutProb = 0.05
    crossProb = 0.1
    dim = 4
    for x in range(25):
        start = time.time()
        resultList.append(HollandAlg(graysCode, limit, popSize, dim, crossProb, mutProb)[0])
        times.append(time.time() - start)
    PrintResults(resultList, times)


def BiggerMutationProbability():
    resultList = []
    times = []
    limit = 500
    popSize = 1000
    mutProb = 0.5
    crossProb = 0.5
    dim = 4
    for x in range(25):
        start = time.time()
        resultList.append(HollandAlg(graysCode, limit, popSize, dim, crossProb, mutProb)[0])
        times.append(time.time() - start)
    PrintResults(resultList, times)


if __name__ == "__main__":
    SmallPopSize()
    LargePopSize()
    SmallerCrossoverProbability()
    BiggerMutationProbability()

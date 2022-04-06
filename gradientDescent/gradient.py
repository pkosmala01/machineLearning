import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, tan, pi, sqrt


def menu():
    dimensions = int(input("Podaj liczbę wymiarów funkcji f (1 lub 2): "))
    if dimensions > 2 or dimensions < 1:
        print("Niewłaściwa liczba wymiarów funkcji!")
        return
    function = input("Podaj wzór funkcji (zmienne oznaczane przez x, y): ")
    gradients = []
    startingPoint = [1.0, 1.0]
    for dimension in range(dimensions):
        gradients.append(input("Podaj wzór elementu wektora gradientu (zmienne oznaczane przez x, y): "))
        startingPoint[dimension] = float(input("Podaj współrzędną punktu początkowego: "))
    alpha = float(input("Podaj współczynnik skoku: "))
    epsilon = float(input("Podaj dokładność: "))
    gradientDescent(function, gradients, alpha, epsilon, startingPoint)


def gradientDescent(function, gradients, step, error, startingPoint):
    letters = ['x', 'y']
    arguments = {'x': startingPoint[0], 'y': startingPoint[1], 'pi': pi, 'sin': sin, 'cos': cos, 'tan': tan}
    history = [[startingPoint[0]], [startingPoint[1]]]
    iter = 0
    while True:
        closeEnough = True
        iter += 1
        for dimension in range(len(gradients)):
            arguments[letters[dimension]] -= step * eval(gradients[dimension], arguments)
            history[dimension].append(arguments[letters[dimension]])
            if abs(eval(gradients[dimension], arguments)) > error:
                closeEnough = False
        if len(gradients) == 1:
            history[1].append(iter/100)
        if closeEnough:
            printResults(arguments, iter, len(gradients), letters, history, function)
            return
    return


def calculateFunction(function, arguments):
    return eval(function, arguments)


def printResults(arguments, iter, dimensions, letters, history, function):
    for dimension in range(dimensions):
        print(f'{letters[dimension]} = {arguments[letters[dimension]]}')
    print(f'Liczba iteracji: {iter}')
    if dimensions == 1:
        xPoints = np.linspace(-10, 10, 1000)
        yPoints = []
        for x in xPoints:
            args = {'x': x, 'pi': pi, 'sin': sin, 'cos': cos, 'tan': tan}
            yPoints.append(calculateFunction(function, args))
        plot = plt.subplot(211)
        plot = plt.plot(xPoints, yPoints)
        plot = plt.plot(history[0], history[1], '-ok')
        xPoints = [abs(x-arguments['x']) for x in history[0]]
        fig = plt.subplot(212)
        fig = plt.plot(xPoints)
        plt.title("Odległość od minimum w kolejnych iteracjach")
    if dimensions == 2:
        plot = plt.gca()
        xPoints = np.linspace(-10, 10, 1000)
        yPoints = np.linspace(-10, 10, 1000)
        zPoints = []
        for x in xPoints:
            row = []
            for y in yPoints:
                args = {'x': x, 'y': y, 'pi': pi, 'sin': sin, 'cos': cos, 'tan': tan}
                row.append(calculateFunction(function, args))
            zPoints.append(row)
        plot = plt.subplot(211)
        plotColoured = plt.pcolormesh(xPoints, yPoints, zPoints)
        plot = plt.plot(history[0], history[1], '-ok')
        xPoints = [sqrt(pow(x-arguments['x'], 2) + pow(y-arguments['y'], 2)) for x, y in zip(history[0], history[1])]
        fig = plt.subplot(212)
        fig = plt.plot(xPoints)
        plt.title("Odległość od minimum w kolejnych iteracjach")
    plt.show()


if __name__ == "__main__":
    menu()

from alphabeta import AlphaBeta
from two_player_games.games.dots_and_boxes import DotsAndBoxes
import math
import random


def TestRandomStart(size, depth):
    game = DotsAndBoxes(size)
    for i in range(6):
        game.state = game.state.make_move(random.choice(game.state.get_moves()))
    while(not game.state.is_finished()):
        bestMoveVal = -math.inf
        for move in game.state.get_moves():
            val = AlphaBeta(game, depth, -math.inf, math.inf)
            if val >= bestMoveVal:
                bestMove = move
                bestMoveVal = val
        game.state = game.state.make_move(bestMove)
        # random move by opponent
        game.state = game.state.make_move(random.choice(game.state.get_moves()))
    return game.state.get_scores()[game.first_player] - game.state.get_scores()[game.second_player]


def TestVs(size, depth):
    game = DotsAndBoxes(size)
    while(not game.state.is_finished()):
        bestMoveVal = -math.inf
        for move in game.state.get_moves():
            val = AlphaBeta(game, depth, -math.inf, math.inf)
            if val >= bestMoveVal:
                bestMove = move
                bestMoveVal = val
        game.state = game.state.make_move(bestMove)
        # random move by opponent
        game.state = game.state.make_move(random.choice(game.state.get_moves()))
    return game.state.get_scores()[game.first_player] - game.state.get_scores()[game.second_player]


if __name__ == "__main__":
    print("Głębokość od 2 do 4:")
    for i in range(2, 5):
        vsresults = []
        for j in range(10):
            vsresults.append(TestVs(3, i))
        print(vsresults)
    print("Rozmiar od 2 do 4:")
    for i in range(2, 5):
        vsresults = []
        for j in range(10):
            vsresults.append(TestVs(i, 3))
        print(vsresults)
    print("Rozmiar od 2 do 4 (losowy start):")
    for i in range(2, 5):
        vsresults = []
        for j in range(10):
            vsresults.append(TestVs(i, 3))
        print(vsresults)

from two_player_games.games.dots_and_boxes import DotsAndBoxes
import math
from copy import deepcopy


def Heur(game):
    return game.state.get_scores()[game.first_player] - game.state.get_scores()[game.second_player]


def AlphaBeta(game, depth, alpha, beta):
    if game.state.is_finished() or depth == 0:
        return Heur(game)
    if game.state.get_current_player() == game.first_player:
        for move in game.state.get_moves():
            newgame = deepcopy(game)
            newgame.state = newgame.state.make_move(move)
            alpha = max(alpha, AlphaBeta(newgame, depth-1, alpha, beta))
            if alpha >= beta:
                return beta
        return alpha
    else:
        for move in game.state.get_moves():
            newgame = deepcopy(game)
            newgame.state = newgame.state.make_move(move)
            beta = min(beta, AlphaBeta(newgame, depth-1, alpha, beta))
            if alpha >= beta:
                return alpha
        return beta


if __name__ == "__main__":
    game = DotsAndBoxes(3)
    result = AlphaBeta(game, 8, -math.inf, math.inf)
    print(result)

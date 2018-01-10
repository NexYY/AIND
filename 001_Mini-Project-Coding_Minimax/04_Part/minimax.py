from minimax_helpers import *


def minimax_decision(gameState):
    def _minimax_decision(gameState):
	    """ Return the move along a branch of the game tree that
	    has the best possible value.  A move is a pair of coordinates
	    in (column, row) order corresponding to a legal move for
	    the searching player.
	    
	    You can ignore the special case of calling this function
	    from a terminal state.
	    """
	    best_score = float("-inf")
	    best_move = None
	    for m in gameState.get_legal_moves():
	        v = min_value(gameState.forecast_move(m))
	        if v > best_score:
	            best_score = v
	            best_move = m
	    return best_move

	""" Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """

    #we start with player 1 = parity 0
	    # The built in `max()` function can be used as argmax!
    return max(gameState.get_legal_moves(),
               key=lambda m: min_value(gameState.forecast_move(m)))

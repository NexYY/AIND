"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass

def score(func):
    def wrap_sf(game, player):
        if game.is_loser(player):
            return float("-inf")

        if game.is_winner(player):
            return float("inf")
        return func(game, player)
    return wrap_sf

@score
def custom_score(game, player):
    return float(len(game.get_legal_moves(player)))

@score
def custom_score_2(game, player):
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves)

@score
def custom_score_3(game, player):
    w, h = game.width / 2., game.height / 2.
    y, x = game.get_player_location(player)
    return float((h - y)**2 + (w - x)**2)


class IsolationPlayer:
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    def _should_timeout(self):
        t = self.time_left()
        return t < self.TIMER_THRESHOLD

    def checkTimeout(func):
        def wrap_f(self, *args, **kwargs):
            if self._should_timeout():
                raise SearchTimeout()
            return func(self, *args, **kwargs)
        return wrap_f

    def checkDepth(func):
        def wrap_f(self, game, depth, *args, **kwargs):
            if depth == 0:
                return self.score(game, self), (-1, -1)           
            return func(self, game, depth, *args, **kwargs)
        return wrap_f
    
    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    @checkTimeout
    def minimax(self, game, depth):
        # check how is the active player
        if game.active_player == self:
            return self.max_value(game, depth)[1]
        else:
            return self.min_value(game, depth)[1]

    @checkTimeout
    @checkDepth
    def min_value(self, game, depth):
        min_value_tmp = float("inf")
        best_next_move = (-1, -1)

        for m in game.get_legal_moves(game.get_opponent(self)):
            next_score = self.max_value(game.forecast_move(m), depth - 1)[0]
            if min_value_tmp > next_score:
                min_value_tmp = next_score
                best_next_move = m
        return min_value_tmp, best_next_move

    @checkTimeout
    @checkDepth
    def max_value(self, game, depth):
        max_value_tmp = float("-inf")
        best_next_move = (-1, -1)

        for m in game.get_legal_moves(game.get_opponent(self)):
            next_score = self.min_value(game.forecast_move(m), depth - 1)[0]
            # looking for the biggest value in MAX
            if max_value_tmp < next_score:
                max_value_tmp = next_score
                best_next_move = m
        return max_value_tmp, best_next_move

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!
        raise NotImplementedError

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        raise NotImplementedError

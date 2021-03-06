"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
import math

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

def _custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return float(len(game.get_legal_moves(player)))

@score
def custom_score(game, player):
    """ Difference between the players legal moves and the opponents legal move, highlighting how many legal moves the next legal moves really has.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float('-inf')

    if game.is_winner(player):
        return float('inf')

    own_legal_moves = game.get_legal_moves(player)
    own_moves = len(own_legal_moves)
    for move in own_legal_moves:
        own_moves += len(_board_move(game, move))

    opp_legal_moves = game.get_legal_moves(game.get_opponent(player))
    opp_moves = len(opp_legal_moves)
    for move in opp_legal_moves:
        opp_moves += len(_board_move(game, move))

    return float(own_moves - opp_moves)


def _board_move(boardGame, loc):
    """Generate the list of possible moves for an L-shaped motion (like a
    knight in chess).
    """
    if loc == None:
        return boardGame.get_blank_spaces()

    r, c = loc
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]
    valid_moves = [(r + dr, c + dc) for dr, dc in directions
                   if boardGame.move_is_legal((r + dr, c + dc))]
    random.shuffle(valid_moves)
    return valid_moves

def _custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves)

@score
def custom_score_2(game, player):
    """"Heuristic which computes the difference in legal moves of the two players
    while penalizes player for moving to a corner
    Difference in legal moves of the two players, taking into account, that corner positions are bad and have to be penlized.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float('-inf')

    if game.is_winner(player):
        return float('inf')

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    corner_weight = 2
    if game.get_player_location(player) in [(0, 0), (0, game.height - 1), (game.width - 1, 0), (game.width - 1, game.height - 1)]:
        own_moves -= corner_weight

    return float(own_moves - opp_moves)

def _custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    w, h = game.width / 2., game.height / 2.
    y, x = game.get_player_location(player)
    return float((h - y)**2 + (w - x)**2)

@score
def custom_score_3(game, player):
    """The third heuristic evaluates again the difference in legal moves between the player and the opponent, however it also additionally ranks moves higher which are farther away from the opponent’s current position. This is based on the principle, that in isolation you need to have movement space to win, staying away from the opponent to not get isolated.
    
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    if game.is_loser(player):
        return float('-inf')

    if game.is_winner(player):
        return float('inf')

    opp_player = game.get_opponent(player)
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(opp_player))

    player_location = game.get_player_location(player)
    opp_location = game.get_player_location(opp_player)
    x_distance = math.pow(player_location[0] - opp_location[0], 2)
    y_distance = math.pow(player_location[1] - opp_location[1], 2)
    distance_bet_player_opp = math.sqrt(x_distance + y_distance)

    return float((own_moves + distance_bet_player_opp) - opp_moves)


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

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
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

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

        # check how is the active player
        #if game.active_player == self:
        #    return self.max_value(game, depth)[1]
        #else:
        #    return self.min_value(game, depth)[1]
        return self.max_value(game, depth)[1]
        #move = (-1, -1)
        #legal_moves = game.get_legal_moves()
        #if len(legal_moves)==0:
        #    return move
        #score_i, move = max ((self.min_value(game, depth-1), p) for p in legal_moves )
        #return move 
        
    @checkTimeout
    @checkDepth
    def min_value(self, game, depth):
        min_value_tmp = float("inf")
        best_next_move = (-1, -1)

        #for m in game.get_legal_moves(game.get_opponent()):
        for m in game.get_legal_moves(game.active_player):
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

        #for m in game.get_legal_moves(game.get_opponent()):
        for m in game.get_legal_moves(game.active_player):
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

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)
        if len(game.get_legal_moves()) >= 1:
            legal_moves = game.get_legal_moves()
            best_move = legal_moves[0]
        else:
            return best_move

        try:
            for depth in range(1, len(game.get_blank_spaces())):
                new_move = self.alphabeta(game, depth)
                # Reached end game
                if new_move == ():
                    return best_move
                else:
                    best_move = new_move
            #return self.minimax(game, self.search_depth)

        except SearchTimeout:
            return best_move  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

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

        best_score = float("-inf")
        #best_move = ()
        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()
        if not legal_moves or depth == 0:
            return self.score(game, self)
        # Iterate over all possible candidate moves
        
        for cand_move in legal_moves:
            # Obtain copy of game.
            cand_game = game.forecast_move(cand_move)
            #cand_score = self.min_value(cand_game, depth-1, alpha, beta)
            cand_score = self.alphabeta_min_max(cand_game, depth=depth-1, alpha=alpha, beta=beta, maximizing_player=True, minMax = "min")
            # Update best_move and max_value if cand_score has max value
            if cand_score > best_score:
                best_move, best_score = cand_move, cand_score
            # Best move found.
            alpha = max(alpha, cand_score)
            # Update lower bound for pruning
        return best_move

        #return self._alphabeta_max(game, depth, alpha=float("-inf"), beta=float("inf"))
        #return self.alphabeta_min_max(game, depth, alpha=float("-inf"), beta=float("inf"))


    def _alphabeta_max(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        best_score = float("-inf")
        #best_move = ()
        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()
        if not legal_moves or depth == 0:
            return self.score(game, self), (-1, -1)
        # Iterate over all possible candidate moves
        
        for cand_move in legal_moves:
            # Obtain copy of game.
            cand_game = game.forecast_move(cand_move)
            #cand_score = self.min_value(cand_game, depth-1, alpha, beta)
            cand_score = self.alphabeta_min_max(cand_game, depth=depth-1, alpha=alpha, beta=beta, maximizing_player=True, minMax = "min")
            # Update best_move and max_value if cand_score has max value
            if cand_score > best_score:
                best_move, best_score = cand_move, cand_score
            # Best move found.
            if best_score < beta:
                alpha = max(alpha, best_score)
            else:
                break
            # Update lower bound for pruning
        return best_move

    def alphabeta_min_max(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True, minMax = "min"):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        legal_moves = game.get_legal_moves()
        if not legal_moves or depth == 0 or game.is_winner(self):
            return self.score(game, self)

        if minMax == "max":
            score = float("-inf")
            for move in legal_moves:
                #score = max(score, self.min_value(game.forecast_move(move), depth-1, alpha, beta))                    
                forecast_game = game.forecast_move(move)
                score = max(score, self.alphabeta_min_max(forecast_game, depth=depth-1, alpha=alpha, beta=beta, maximizing_player=True, minMax = "min"))
                if score >= beta:
                    return score # Found candidate upper value
                # lower bound
                alpha = max(alpha, score)
        elif minMax == "min":
            score = float("inf")
            for move in legal_moves:
                forecast_game = game.forecast_move(move)
                #score = min(score, self.max_value(game.forecast_move(move), depth-1, alpha, beta))
                score = min(score, self.alphabeta_min_max(forecast_game, depth=depth-1, alpha=alpha, beta=beta, maximizing_player=True, minMax = "max"))
                if score <= alpha:
                    return score # Found candidate lower score
                # Update upper bound
                beta = min(beta, score)
        else:
            raise Exception()
        return score

































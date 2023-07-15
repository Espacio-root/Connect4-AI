# Import necessary libraries
import math  # Import the math module for mathematical operations
import random  # Import the random module for generating random numbers

# Define a class for the Connect4 AI
class Connect4Ai:
    # Initialize the class with rows, cols, player_piece, and ai_piece as parameters
    def __init__(self, rows, cols, player_piece, ai_piece):
        self.rows = rows
        self.cols = cols
        self.player_piece = player_piece
        self.ai_piece = ai_piece

    # Evaluate a window of pieces for a given player_piece
    def evaluate_window(self, window, piece):
        # Determine the opponent's piece based on the player's piece
        opponent_piece = self.player_piece
        if piece == self.player_piece:
            opponent_piece = self.ai_piece

        score = 0  # Initialize the score for the window

        # Evaluate the window based on the number of pieces and empty spaces
        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2

        # Deduct score if the window contains the opponent's pieces and one empty space
        if window.count(opponent_piece) == 3 and window.count(0) == 1:
            score -= 4

        return score

    # Check if a given move results in a winning position
    def winning_move(self, board, piece):
        # Check for horizontal winning positions
        for c in range(self.cols - 3):
            for r in range(self.rows):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                    return True

        # Check for vertical winning positions
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                    return True

        # Check for diagonal (ascending) winning positions
        for c in range(self.cols - 3):
            for r in range(3, self.rows):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                    return True

        # Check for diagonal (descending) winning positions
        for c in range(3, self.cols):
            for r in range(3, self.rows):
                if board[r][c] == piece and board[r - 1][c - 1] == piece and board[r - 2][c - 2] == piece and board[r - 3][c - 3] == piece:
                    return True

    # Calculate the score of a given position for a player_piece
    def score_position(self, board, piece):
        score = 0  # Initialize the score for the position

        center_array = [int(i) for i in list(board[:, self.cols // 2])]
        center_count = center_array.count(piece)
        score += center_count * 6  # Add score for the player_piece's pieces in the center column

        # Evaluate rows for potential winning positions
        for r in range(self.rows):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(self.cols - 3):
                window = row_array[c:c + 4]
                score += self.evaluate_window(window, piece)

        # Evaluate columns for potential winning positions
        for c in range(self.cols):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(self.rows - 3):
                window = col_array[r:r + 4]
                score += self.evaluate_window(window, piece)

        # Evaluate diagonals (ascending) for potential winning positions
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                window = [board[r - i][c + i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        # Evaluate diagonals (descending) for potential winning positions
        for r in range(3, self.rows):
            for c in range(3, self.cols):
                window = [board[r - i][c - i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        return score

    # Check if a column is a valid location to make a move
    def is_valid_location(self, board, col):
        return board[0][col] == 0

    # Get a list of valid columns where a move can be made
    def get_valid_locations(self, board):
        valid_locations = []

        for column in range(self.cols):
            if self.is_valid_location(board, column):
                valid_locations.append(column)

        return valid_locations

    # Find the next open row in a given column
    def get_next_open_row(self, board, col):
        for r in range(self.rows - 1, -1, -1):
            if board[r][col] == 0:
                return r

    # Drop a game piece into a given row and column
    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece
        return board

    # Check if the current board state is a terminal node (winning position or board is full)
    def is_terminal_node(self, board):
        return self.winning_move(board, self.player_piece) or self.winning_move(board, self.ai_piece) or len(
            self.get_valid_locations(board)) == 0

    # Implement the minimax algorithm to find the best move
    def minimax(self, board, depth, alpha, beta, maximizing_player):
        valid_locations = self.get_valid_locations(board)  # Get a list of valid moves
        is_terminal = self.is_terminal_node(board)  # Check if the current state is a terminal node

        # Base cases for recursion
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.winning_move(board, self.ai_piece):  # AI wins
                    return (None, 10000000)
                elif self.winning_move(board, self.player_piece):  # Player wins
                    return (None, -10000000)
                else:  # It's a tie
                    return (None, 0)
            else:  # If the depth is 0 and it's not a terminal node, evaluate the position
                return (None, self.score_position(board, self.ai_piece))

        if maximizing_player:
            value = -math.inf  # Initialize the value for the maximizing player
            column = random.choice(valid_locations)  # Randomly choose a move

            for col in valid_locations:
                row = self.get_next_open_row(board, col)
                b_copy = board.copy()  # Make a copy of the board
                self.drop_piece(b_copy, row, col, self.ai_piece)  # Simulate the move
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]  # Recurse for the opponent's turn
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(value, alpha)  # Update alpha
                if alpha >= beta:  # Pruning condition
                    break

            return column, value  # Return the best move and its score

        else:  # Minimizing player's turn
            value = math.inf  # Initialize the value for the minimizing player
            column = random.choice(valid_locations)  # Randomly choose a move

            for col in valid_locations:
                row = self.get_next_open_row(board, col)
                b_copy = board.copy()  # Make a copy of the board
                self.drop_piece(b_copy, row, col, self.player_piece)  # Simulate the move
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]  # Recurse for the AI's turn
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(value, beta)  # Update beta
                if alpha >= beta:  # Pruning condition
                    break

            return column, value  # Return the best move and its score

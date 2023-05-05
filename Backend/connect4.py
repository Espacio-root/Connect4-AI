import math
import random
import numpy as np

class Connect4Ai:
    def __init__(self, rows, cols, player_piece, ai_piece):
        self.rows = rows
        self.cols = cols
        self.player_piece = player_piece
        self.ai_piece = ai_piece

    def evaluate_window(self, window, piece):
        opponent_piece = self.player_piece

        if piece == self.player_piece:
            opponent_piece = self.ai_piece
        score = 0
        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2

        if window.count(opponent_piece) == 3 and window.count(0) == 1:
            score -= 4 

        return score  

    def winning_move(self, board, piece):

        for c in range(self.cols-3):
            for r in range(self.rows):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

        for c in range(self.cols):
            for r in range(self.rows-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        for c in range(self.cols-3):
            for r in range(3, self.rows):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

        for c in range(3,self.cols):
            for r in range(3, self.rows):
                if board[r][c] == piece and board[r-1][c-1] == piece and board[r-2][c-2] == piece and board[r-3][c-3] == piece:
                    return True
                
    def score_position(self, board, piece):

        score = 0

        center_array = [int(i) for i in list(board[:,self.cols//2])]
        center_count = center_array.count(piece)
        score += center_count * 6

        for r in range(self.rows):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(self.cols - 3):
                window = row_array[c:c + 4]
                score += self.evaluate_window(window, piece)

        for c in range(self.cols):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(self.rows-3):
                window = col_array[r:r+4]
                score += self.evaluate_window(window, piece)

        for r in range(3,self.rows):
            for c in range(self.cols - 3):
                window = [board[r-i][c+i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        for r in range(3,self.rows):
            for c in range(3,self.cols):
                window = [board[r-i][c-i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        return score
    
    def is_valid_location(self, board, col):
        return board[0][col] == 0
    
    def get_valid_locations(self, board):
        valid_locations = []
        
        for column in range(self.cols):
            if self.is_valid_location(board, column):
                valid_locations.append(column)

        return valid_locations
    
    def get_next_open_row(self, board, col):
        for r in range(self.rows-1, -1, -1):
            if board[r][col] == 0:
                return r

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def is_terminal_node(self, board):
        return self.winning_move(board, self.player_piece) or self.winning_move(board, self.ai_piece) or len(self.get_valid_locations(board)) == 0


    def minimax(self, board, depth, alpha, beta, maximizing_player):

        valid_locations = self.get_valid_locations(board)

        is_terminal = self.is_terminal_node(board)

        if depth == 0 or is_terminal:
            if is_terminal: 
                if self.winning_move(board, self.ai_piece):
                    return (None, 10000000)
                elif self.winning_move(board, self.player_piece):
                    return (None, -10000000)
                else:
                    return (None, 0)
            else: 
                return (None, self.score_position(board, self.ai_piece))

        if maximizing_player:
            value = -math.inf
            column = random.choice(valid_locations)

            for col in valid_locations:
                row = self.get_next_open_row(board, col)
                b_copy = board.copy()
                self.drop_piece(b_copy, row, col, self.ai_piece)
                new_score = self.minimax(b_copy, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(value, alpha) 
                if alpha >= beta:
                    break

            return column, value

        else:
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_open_row(board, col)
                b_copy = board.copy()
                self.drop_piece(b_copy, row, col, self.player_piece)
                new_score = self.minimax(b_copy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(value, beta) 
                if alpha >= beta:
                    break
            return column, value
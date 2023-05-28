
class Board:
    
    WHITE_SPOT = -1
    EMPTY_SPOT = 0
    P1 = 1
    P2 = 2
    P1_K = 3
    P2_K = 4
    HEIGHT = 8
    WIDTH = 8
    
    
    def __init__(self):
       self.player_turn = self.P1
       self.board = [
            [-1, 1, -1, 1, -1, 1, -1, 1],
            [1, -1, 1, -1, 1, -1, 1, -1],
            [-1, 1, -1, 1, -1, 1, -1, 1],
            [0, -1, 0, -1, 0, -1, 0, -1],
            [-1, 0, -1, 0, -1, 0, -1, 0],
            [2, -1, 2, -1, 2, -1, 2, -1],
            [-1, 2, -1, 2, -1, 2, -1, 2],
            [2, -1, 2, -1, 2, -1, 2, -1]
       ]

    def real_spot(self, row, col):
        if row >= 0 and row < 8:
            if col >= 0 and col < 8:
                if not self.board[row, col] == self.EMPTY_SPOT:
                    return True
        return False
    
    def piece_moves(self, row, col):
        moves = []
        piece = self.board[row][col]
        if piece == self.P1:
            if (col+1 < 8 and self.board[row+1][col+1] == 0):
                moves.append([row+1, col+1])
            if (col-1 >= 0 and self.board[row+1][col-1] == 0):
                moves.append([row+1, col-1])
        elif piece == self.P2:
            if (col+1 < 8 and self.board[row-1][col+1] == 0):
                moves.append([row-1, col+1])
            if (col-1 >= 0 and self.board[row-1][col-1] == 0):
                moves.append([row-1, col-1])
        elif piece == self.P1_K or piece == self.P2_K:
            if row-1 >= 0:
                if (col+1 < 8 and self.board[row-1][col+1] == 0):
                    moves.append([row-1, col+1])
                if (col-1 >= 0 and self.board[row-1][col-1] == 0):
                    moves.append([row-1, col-1])
            if row+1 < 8:
                if (col+1 < 8 and self.board[row+1][col+1] == 0):
                    moves.append([row+1, col+1])
                if (col-1 >= 0 and self.board[row+1][col-1] == 0):
                    moves.append([row+1, col-1])
        return moves
    
    def piece_jumps(self, row, col):
        jumps = []
        piece = self.board[row][col]
        if piece == self.P1:
            if (col+1 < 8 and self.board[row+1][col+1] == 0):
                jumps.append([row+1, col+1])
            if (col-1 >= 0 and self.board[row+1][col-1] == 0):
                jumps.append([row+1, col-1])
        elif piece == self.P2:
            if (col+1 < 8 and self.board[row-1][col+1] == 0):
                jumps.append([row-1, col+1])
            if (col-1 >= 0 and self.board[row-1][col-1] == 0):
                jumps.append([row-1, col-1])
        elif piece == self.P1_K or piece == self.P2_K:
            if row-1 >= 0:
                if (col+1 < 8 and self.board[row-1][col+1] == 0):
                    jumps.append([row-1, col+1])
                if (col-1 >= 0 and self.board[row-1][col-1] == 0):
                    jumps.append([row-1, col-1])
            if row+1 < 8:
                if (col+1 < 8 and self.board[row+1][col+1] == 0):
                    jumps.append([row+1, col+1])
                if (col-1 >= 0 and self.board[row+1][col-1] == 0):
                    jumps.append([row+1, col-1])
        return jumps
    
    def possible_moves(self):
        for row in range(8):
            for col in range(8):
                if not (self.board[row][col] == -1 or self.board[row][col] == 0):
                    piece = self.board[row][col]
                    self.piece_moves(piece, row, col)
                    
        
    def update_position(self, start, end):
        return True

    def print_board(self):
        for row in self.board:
            for square in row:
                if square == -1:
                    print("  ", end="")
                elif square == 0:
                    print("\u25A0 ", end="")
                elif square == 1:
                    print("\u25CF ", end="")
                elif square == 2:
                    print("\u25CB ", end="")    
                elif square == 3:
                    print("\u265A ", end="")
                elif square == 4:
                    print("\u2654 ", end="")
            print()
        




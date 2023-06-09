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
       self.player_turn = self.P2
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


    def move(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece == self.player_turn or piece - 2 == self.player_turn:
            if self.is_real_spot(start[0], start[1]):
                if self.is_valid_move(start, end):
                    self.update_position(start, end)
                    if (piece == self.P1 and end[0] == 7) or (piece == self.P2 and end[0] == 0):
                        self.board[end[0]][end[1]] += 2
                    if piece == self.P1_K or piece == self.P1:
                        self.player_turn = self.P2
                    else:
                        self.player_turn = self.P1

    def update_position(self, start, end):
        piece = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = 0
        self.board[end[0]][end[1]] = piece
        if abs(start[0] - end[0]) >= 2:
            self.board[(start[0] + end[0]) // 2][(start[1] + end[1]) // 2] = 0

    def is_valid_move(self, start, end):
        moves = self.piece_moves(start[0], start[1])
        jumps = self.piece_jumps(start[0], start[1])
        if any(move == end for move in moves) and not self.is_jump_possible():
            return True
        elif any(jump == end for jump in jumps):
            return True
        return False
    
    def is_real_spot(self, row, col):
        if row >= 0 and row < 8:
            if col >= 0 and col < 8:
                if not self.board[row][col] == self.EMPTY_SPOT:
                    return True
        return False

    def is_jump_possible(self):
        jumps = []
        for row in range(8):
            for col in range(8):
                if not (row + col) % 2 == 0:
                    if self.board[row][col] == self.player_turn or self.board[row][col] == self.player_turn+2:
                        if not self.piece_jumps(row, col) == []:
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
            if row+2 < 8:
                if (col+2 < 8 and row+2 < 8
                    and (self.board[row+1][col+1] == self.P2 or self.board[row+1][col+1] == self.P2_K) 
                    and self.board[row+2][col+2] == self.EMPTY_SPOT):
                    jumps.append([row+2, col+2])

                if (col-2 >= 0 and row+2 < 8
                    and (self.board[row+1][col-1] == self.P2 or self.board[row+1][col-1] == self.P2_K)
                    and self.board[row+2][col-2] == self.EMPTY_SPOT):
                    jumps.append([row+2, col-2])

        elif piece == self.P2:
            if row-2 >= 0:
                if (col+2 < 8
                    and (self.board[row-1][col+1] == self.P1 or self.board[row-1][col+1] == self.P1_K)
                    and self.board[row-2][col+2] == self.EMPTY_SPOT):
                    jumps.append([row-2, col+2])
                if (col-2 >= 0
                    and (self.board[row-1][col-1] == self.P1 or self.board[row-1][col-1] == self.P1_K)
                    and self.board[row-2][col-2] == self.EMPTY_SPOT):
                    jumps.append([row-2, col-2])

        elif piece == self.P1_K:
            if row-2 >= 0:
                if (col+2 < 8 
                    and (self.board[row-1][col+1] == self.P2 or self.board[row-1][col+1] == self.P2_K)
                    and self.board[row-2][col+2] == self.EMPTY_SPOT):
                    jumps.append([row-2, col+2])
                if (col-2 >= 0 
                    and (self.board[row-1][col-1] == self.P2 or self.board[row-1][col-1] == self.P2_K)
                    and self.board[row-2][col-2] == self.EMPTY_SPOT):
                    jumps.append([row-2, col-2])

            if row+2 < 8:
                if (col+2 < 8 
                    and (self.board[row+1][col+1] == self.P2 or self.board[row+1][col+1] == self.P2_K)
                    and self.board[row+2][col+2] == self.EMPTY_SPOT):
                    jumps.append([row+2, col+2])
                if (col-2 >= 0 
                    and (self.board[row+1][col-1] == self.P2 or self.board[row+1][col-1] == self.P2_K)
                    and self.board[row+2][col-2] == self.EMPTY_SPOT):
                    jumps.append([row+2, col-2])

        elif piece == self.P2_K:
            if row-2 >= 0:
                if (col+2 < 8 
                    and (self.board[row-1][col+1] == self.P1 or self.board[row-1][col+1] == self.P1_K)
                    and self.board[row-2][col+2] == self.EMPTY_SPOT):
                    jumps.append([row-2, col+2])
                if (col-2 >= 0 
                    and (self.board[row-1][col-1] == self.P1 or self.board[row-1][col-1] == self.P1_K)
                    and self.board[row-2][col-2] == self.EMPTY_SPOT):
                    jumps.append([row-2, col-2])
            if row+2 < 8:
                if (col+2 < 8 
                    and (self.board[row+1][col+1] == self.P1 or self.board[row+1][col+1] == self.P1_K)
                    and self.board[row+2][col+2] == self.EMPTY_SPOT):
                    jumps.append([row+2, col+2])
                if (col-2 >= 0 
                    and (self.board[row+1][col-1] == self.P1 or self.board[row+1][col-1] == self.P1_K)
                    and self.board[row+2][col-2] == self.EMPTY_SPOT):
                    jumps.append([row+2, col-2])
        return jumps
    

    def possible_moves(self):
        for row in range(8):
            for col in range(8):
                if not (self.board[row][col] == -1 or self.board[row][col] == 0):
                    piece = self.board[row][col]
                    self.piece_moves(piece, row, col)
                    
        
    
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

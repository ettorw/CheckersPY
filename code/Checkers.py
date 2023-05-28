from Board import Board

run = True
board = Board()
move = [[None, None], [None, None]]
print("==========| CheckerPY |==========")

while run:
    print(board.print_board())
    print(board.piece_moves(2, 1))
    input() 

import sys
from PyQt5.QtGui import QColor, QBrush, QPen, QPainter
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint

from Board import Board

board = Board()

class CheckersBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.piece_size = 120
        self.setGeometry(500, 200, 8 * self.piece_size, 8 * self.piece_size)
        self.setWindowTitle("Checkers Board")
        
        self.selected_piece = None
        self.selected_piece_pos = None
        
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        for row in range(8):
            for col in range(8):
                x = col * self.piece_size
                y = row * self.piece_size

                if (row + col) % 2 == 0:
                    painter.setBrush(QColor("#999999"))
                else:
                    painter.setBrush(QColor("#111111"))

                painter.drawRect(x, y, self.piece_size, self.piece_size)

                piece = board.board[row][col]
                if piece != 0 and piece != -1:
                    if piece == 1:
                        color = QColor("#63E7FE")
                    elif piece == 2:
                        color = QColor("#d90511")
                    elif piece == 3:
                        color = QColor("#63E7FE")
                    elif piece == 4:
                        color = QColor("#d90511")

                    painter.setBrush(QBrush(color))
                    painter.setPen(QPen(Qt.black, 2))
                    painter.drawEllipse(x + 5, y + 5, self.piece_size - 10, self.piece_size - 10)

        painter.end()

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()

        row = y // self.piece_size
        col = x // self.piece_size

        piece = board.board[row][col]
        if piece != 0 and piece != -1:
            self.selected_piece = piece
            self.selected_piece_pos = (row, col)

    def mouseMoveEvent(self, event):
        if self.selected_piece is not None:
            x = event.x()
            y = event.y()

            row = y // self.piece_size
            col = x // self.piece_size

            if board.is_valid_move(self.selected_piece_pos, [row, col]):
                self.selected_piece_pos = (row, col)
                self.update()

    def mouseReleaseEvent(self, event):
        if self.selected_piece is not None:
            x = event.x()
            y = event.y()

            row = y // self.piece_size
            col = x // self.piece_size

            if board.is_valid_move(self.selected_piece_pos, [row, col]):
                board.update_position(self.selected_piece_pos, [row, col])
                self.selected_piece = None
                self.selected_piece_pos = None
                self.update()
            else:
                self.selected_piece = None
                self.selected_piece_pos = None
                self.update()


app = QApplication(sys.argv)
ex = CheckersBoard()
sys.exit(app.exec_())

"""
run = True
board = Board()
move = [[None, None], [None, None]]
print("==========| CheckerPY |==========")

while run:
    print(board.print_board())
    print(board.piece_moves(2, 1))
    input() 
"""
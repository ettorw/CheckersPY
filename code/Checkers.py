import sys
from PyQt5.QtGui import QColor, QBrush, QPen, QPainter
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

from Board import Board

board = Board()

class CheckersBoard(QWidget):
    def __init__(self, board):
        super().__init__()
        self.piece_size = 120
        self.setGeometry(500, 200, 8 * self.piece_size, 8 * self.piece_size)
        self.setWindowTitle("Checkers Board")
        self.show()
        
        # Initialize click variables
        self.first_click_row = None
        self.first_click_col = None

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
                        color = QColor("#0197b2")
                    elif piece == 4:
                        color = QColor("#7c0309")

                    painter.setBrush(QBrush(color))
                    painter.setPen(QPen(Qt.black, 2))
                    painter.drawEllipse(x + 5, y + 5, self.piece_size - 10, self.piece_size - 10)

        painter.end()

    def mousePressEvent(self, event):
        self.start = [event.pos().y() // self.piece_size, event.pos().x() // self.piece_size]

        if self.start[0] < 0 or self.start[0] > 7 or self.start[1] < 0 or self.start[1] > 7:
            return

    def mouseReleaseEvent(self, event):
        self.end = [event.pos().y() // self.piece_size, event.pos().x() // self.piece_size]

        if self.end[0] < 0 or self.end[0] > 7 or self.end[1] < 0 or self.end[1] > 7:
            return

        board.move(self.start, self.end)
        self.update()

app = QApplication(sys.argv)
ex = CheckersBoard(board)
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
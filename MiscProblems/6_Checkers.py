import numpy as np


class Checkers:
    def __init__(self, n, m):
        self.board = np.zeros(n , m)
        self.color_map = {"red":1, "blue":2}

    def verify_position(self, pos):
        color = pos[0]
        x = pos[1]
        y = pos[2]
        n, m = self.board.zize

        if color not in self.c:
            return False

        if x <0 or x >= n:
            return False

        if y <0 or y >= m:
            return False

        if self.board[x, y] != 0:
            return False

        return True

    def place(self, pos):
        color = pos[0]
        x = pos[1]
        y = pos[2]

        if verify_position(pos):
            self.board[x, y] = self.c[color]

        return
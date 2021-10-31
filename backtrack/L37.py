from typing import List

class Solution:

    def buil_grid_map(self):
        self.grid_map = {}
        for i in range(3):
            for j in range(3):
                plist = []
                for row in range(i*3, (i+1)*3):
                    for col in range(j*3, (j+1)*3):
                        plist.append((row, col))
                for p in plist:
                    self.grid_map[p] = plist


    def get_position(self, index):
        row = index//self.N
        col = index%self.N
        return row, col

    def check(self, board, row, col, digit):
        digit = str(digit)
        for i in range(self.N):
            if board[row][i] == digit:
                return False
            if board[i][col] == digit:
                return False

        plist = self.grid_map[(row,col)]
        for r,c in plist:
            if board[r][c] == digit:
                return False
        return True

    def backtrack(self, board, index):
        if index >= self.number:
            return True
        for i in range(index, self.number):
            row, col = self.get_position(i)
            if board[row][col] != ".":
                continue
            for digit in range(1,10):
                if self.check(board, row, col, digit):
                    board[row][col] = str(digit)
                    flag = self.backtrack(board, i + 1)
                    if flag:
                        return True
                    board[row][col] = "."
            return False

        return True


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.N = len(board)
        self.number = len(board) * len(board)
        self.buil_grid_map()

        self.backtrack(board, 0)
        return board


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    solution = Solution()
    solution.solveSudoku(board)
    for i in range(len(board)):
        print(board[i])
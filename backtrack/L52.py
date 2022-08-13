class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        self.total = 0

    def check_valid(self, Q_index):
        for j, p in enumerate(self.path):
            p_Q_index = p.index('Q')
            if p_Q_index == Q_index:
                return False
            if abs(j-len(self.path)) == abs(p_Q_index-Q_index):
                return False
        return True

    def backtrack(self,n, row_index):
        if row_index == n:
            self.total += 1
            return
        for i in range(n):
            row = ["." for _ in range(n)]
            row[i] = "Q"
            if not self.check_valid(i):
                continue
            self.path.append(row)
            self.backtrack(n, row_index + 1)
            self.path.pop()

    def totalNQueens(self, n: int) -> int:
        if n <= 1:
            return n
        self.backtrack(n, 0)
        return self.total

if __name__ == '__main__':
    solution = Solution()
    print(solution.totalNQueens(4))
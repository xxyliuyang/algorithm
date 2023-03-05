from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def dfs(self, left, right, n):
        if left == n and right == n:
            self.result.append("".join(self.path))
            return
        if left < n:
            self.path.append("(")
            self.dfs(left + 1, right, n)
            self.path.pop()
        if right < n and left > right:
            self.path.append(")")
            self.dfs(left, right + 1, n)
            self.path.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.dfs(0, 0, n)
        return self.result


if __name__ == '__main__':
    n = 3
    solution = Solution()
    print(solution.generateParenthesis(n))

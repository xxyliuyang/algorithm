from typing import List
import copy

class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def backtrack(self, n, k, position):
        if len(self.path) == k:
            self.result.append(copy.deepcopy(self.path))
            return
        for i in range(position, n+1):
            self.path.append(i)
            self.backtrack(n, k , i+1)
            self.path.pop(i)

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n, k, 1)
        return self.result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
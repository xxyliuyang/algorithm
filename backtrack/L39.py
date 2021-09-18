from typing import List
import copy

class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        self.total = 0

    def trackback(self, candidates, target, start_index):
        if self.total > target:
            return
        if self.total == target:
            self.result.append(copy.deepcopy(self.path))

        for i in range(start_index, len(candidates)):
            if self.total > target:
                break
            self.total += candidates[i]
            self.path.append(candidates[i])
            self.trackback(candidates, target, i)
            self.total -= candidates[i]
            self.path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return self.result

        candidates.sort()
        self.trackback(candidates, target, 0)
        return self.result

if __name__ == '__main__':
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7

    res = solution.combinationSum(candidates, target)
    print(res)
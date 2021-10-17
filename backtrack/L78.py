from typing import List
from copy import deepcopy

class Solution:

    def __init__(self):
        self.path = []
        self.result = []

    def backtrack(self, nums, start):
        if start >= len(nums):
            return
        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.result.append(deepcopy(self.path))
            self.backtrack(nums, i+1)
            self.path.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result.append([])
        self.backtrack(nums, 0)
        return self.result

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets(nums))
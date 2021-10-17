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
            if i != start and  i > 0 and nums[i] == nums[i-1]:
                continue
            self.path.append(nums[i])
            self.result.append(deepcopy(self.path))
            self.backtrack(nums, i+1)
            self.path.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result.append([])
        self.backtrack(nums, 0)
        return self.result


if __name__ == '__main__':
    nums = [1, 2, 2]
    solution = Solution()
    print(solution.subsetsWithDup(nums))
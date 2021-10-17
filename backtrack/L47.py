from typing import List
from copy import deepcopy

class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def backtrack(self, nums, used):
        if len(self.path) == len(nums):
            self.result.append(deepcopy(self.path))
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                continue
            used[i] = True
            self.path.append(nums[i])
            self.backtrack(nums, used)
            used[i] = False
            self.path.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return self.result
        nums.sort()
        used = [False] * len(nums)
        self.backtrack(nums, used)
        return self.result

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,3]

    print(solution.permuteUnique(nums))
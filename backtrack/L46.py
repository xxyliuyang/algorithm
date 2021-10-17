from typing import List
from copy import deepcopy

class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def backtrack(self, nums):
        if len(nums) == 0:
            self.result.append(deepcopy(self.path))
            return

        for i in range(len(nums)):
            self.path.append(nums[i])
            self.backtrack(nums[:i] + nums[i+1:])
            self.path.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return self.result
        self.backtrack(nums)
        return self.result

if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    print(solution.permute(nums))
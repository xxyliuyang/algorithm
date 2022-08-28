from typing import List
import copy

class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def backtrack(self, nums, start):
        if len(self.path)>=2:
            self.result.append(copy.deepcopy(self.path))

        for i in range(start, len(nums)):
            if self.path and nums[i] < self.path[-1]:
                continue
            if i>start and nums[i] in nums[start:i]:
                continue
            self.path.append(nums[i])
            self.backtrack(nums, i+1)
            self.path.pop()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return []

        self.backtrack(nums, 0)
        return self.result

if __name__ == '__main__':
    solution = Solution()
    nums = [4, 7, 6, 7]

    print(solution.findSubsequences(nums))
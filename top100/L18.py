from copy import deepcopy
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def backtrack(self, nums, target, index, sum_value):
        if target == sum_value and len(self.path) == 4:
            self.result.append(deepcopy(self.path))
            return

        for i in range(index, len(nums)):
            if (i > index and nums[i] == nums[i - 1]):
                continue
            if len(self.path) + len(nums) - i < 4:
                return
            self.path.append(nums[i])
            self.backtrack(nums, target, i + 1, sum_value + nums[i])
            self.path.pop()

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.backtrack(nums, target, 0, 0)
        return self.result


if __name__ == '__main__':
    nums = [1,-2,-5,-4,-3,3,3,5]
    target = -11

    solution = Solution()
    print(solution.fourSum(nums, target))

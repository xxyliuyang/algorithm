from typing import List
from collections import defaultdict

class Solution:
    def count(self, nums, lower):
        left = 0
        right = len(nums) -1
        res = 0
        while left < right:
            if nums[left] + nums[right] >= lower:
                res += right - left
                right -= 1
            else:
                left += 1
        return res

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count1 = self.count(nums, lower)
        count2 = self.count(nums, upper+1)
        return count1 - count2


if __name__ == '__main__':
    nums = [0, 1, 7, 4, 4, 5]
    lower = 3
    upper = 6

    solution = Solution()
    print(solution.countFairPairs(nums, lower, upper))
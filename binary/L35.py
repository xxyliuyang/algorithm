from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 0

    solution = Solution()
    print(solution.searchInsert(nums, target))

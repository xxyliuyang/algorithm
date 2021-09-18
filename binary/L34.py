from typing import List


class Solution:
    def find_left(self, nums, target):
        """答案在【left，right】中"""
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target \
                    and (mid == 0 or nums[mid - 1] < target):
                return mid

            if nums[mid] >= target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        return -1

    def find_right(self, nums, target):
        """答案在【left，right】中"""
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target \
                    and (mid == len(nums) - 1 or nums[mid + 1] > target):
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] <= target:
                left = mid + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_left(nums, target)
        right = self.find_right(nums, target)
        return [left, right]


if __name__ == '__main__':
    solution = Solution()
    nums = []
    target = 8
    print(solution.searchRange(nums, target))

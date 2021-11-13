from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1

        return False

if __name__ == '__main__':
    solution = Solution()
    nums = [1,0,1,1,1]
    target = 0

    print(solution.search(nums, target))
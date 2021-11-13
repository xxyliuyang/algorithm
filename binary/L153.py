from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right  = 0, len(nums)-1
        while left<=right:
            mid = left + (right-left) // 2

            if nums[mid]<nums[right]:
                right = mid-1
            else:
                left = mid + 1
        return nums[left]


if __name__ == '__main__':
    solution = Solution()
    nums = [3,4,5,1,2]
    print(solution.findMin(nums))
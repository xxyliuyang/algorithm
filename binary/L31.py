# 旋转数组：https://www.cnblogs.com/ariel-dreamland/p/9138064.html
# 如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的，只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内。

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 4

    print(solution.search(nums, target))
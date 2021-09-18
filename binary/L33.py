from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """答案在【left，right】中"""
        if len(nums) == 0:
            return -1

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[low]:
                if target >= nums[low] and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target <= nums[high] and target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        else:
            return -1



if __name__ == '__main__':
    solution = Solution()
    nums = [4,5,6,7,8,1,2,3]
    target = 8
    print(solution.search(nums, target))
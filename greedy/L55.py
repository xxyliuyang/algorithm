from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        for i in range(len(nums)):
            if farest < i:
                return False
            farest = max(farest, i + nums[i])
        return True

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    solution = Solution()

    print(solution.canJump(nums))
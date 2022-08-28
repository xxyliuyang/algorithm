from typing import List


class Solution:
    def select_first(self, nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-2]

    def not_select_first(self, nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = 0
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.select_first(nums), self.not_select_first(nums))

if __name__ == '__main__':
    nums = [2,1,2,6,1,8,10,10]
    solution = Solution()
    print(solution.rob(nums))
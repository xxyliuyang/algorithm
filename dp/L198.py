from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums)+2)]
        for i in range(2,len(nums)+2):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-2])

        return dp[-1]

if __name__ == '__main__':
    nums = [2,7,9,3,1]
    solution = Solution()
    print(solution.rob(nums))

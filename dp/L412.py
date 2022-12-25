# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# File   : L412.py
# Time   : 2022/9/24 12:17 PM
"""
from typing import List
from dp.util import show_dp

class Solution:
    """
    分割等和子集：
    1，背包大小为和的一半，求最大的价值==target
    2，背包；求最大值的问题
    """
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total//2

        dp = [[0 for _ in range(target+1)] for _ in range(len(nums))]
        for i in range(target+1):
            if i >= nums[0]:
                dp[0][i] = nums[0]
        for i in range(len(nums)):
            for j in range(target+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]] + nums[i])
        return dp[-1][-1] == target

    def canPartition_with_onedp(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total//2

        dp = [0 for _ in range(target+1)]
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
        return dp[-1] == target




if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    solution = Solution()
    print(solution.canPartition_with_onedp(nums))
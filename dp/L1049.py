# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# File   : L1049.py
# Time   : 2022/10/2 10:10 AM
"""
from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        bag = sum(stones)//2
        dp = [[0 for _ in range(bag+1)] for _ in range(len(stones))]
        for i in range(bag+1):
            if i >= stones[0]:
                dp[0][i] = stones[0]

        for i in range(1, len(stones)):
            for j in range(bag+1):
                if stones[i]>j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], stones[i]+dp[i-1][j-stones[i]])

        return sum(stones) - dp[-1][-1]*2

    def lastStoneWeightII_with_onddp(self, stones: List[int]) -> int:
        bag = sum(stones)//2
        dp = [0 for _ in range(bag+1)]
        for i in range(1, len(stones)):
            for j in range(bag, stones[i]-1, -1):
                dp[j] = max(dp[j], stones[i]+dp[j-stones[i]])
        return sum(stones) - dp[-1]*2

if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    solution = Solution()
    print(solution.lastStoneWeightII_with_onddp(stones))
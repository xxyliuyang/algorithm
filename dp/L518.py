# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# File   : L518.py
# Time   : 2022/10/4 9:38 AM
"""
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(amount+1):
                if j<coins[i]:
                    continue
                dp[j] += dp[j-coins[i]]
        return dp[-1]

if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]

    solution = Solution()
    print(solution.change(amount, coins))
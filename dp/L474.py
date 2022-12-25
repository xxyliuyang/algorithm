# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# File   : L474.py
# Time   : 2022/10/3 7:16 PM
"""
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if len(strs) == 0:
            return 0
        weigths = []
        for s in strs:
            s_ = s.replace("1", "")
            weigths.append((len(s_), len(s) - len(s_)))

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(len(strs)):
            n_zero = weigths[i][0]
            n_one = weigths[i][1]
            for j in range(m, n_zero-1, -1):
                for k in range(n, n_one-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-n_zero][k-n_one]+1)
        return dp[-1][-1]

if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3

    solution = Solution()
    print(solution.findMaxForm(strs, m, n))

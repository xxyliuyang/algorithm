# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# File   : L2673.py
# Time   : 2023/7/1 17:26
# Author : liuyang09
"""
from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        for i in range(n - 1, 0, -2):
            l_index = i - 1
            r_index = i
            res += abs(cost[l_index] - cost[r_index])
            cost[(i - 1) // 2] += max(cost[l_index], cost[r_index])
        return res


if __name__ == '__main__':
    n = 15
    cost = [764, 1460, 2664, 764, 2725, 4556, 5305, 8829, 5064, 5929, 7660, 6321, 4830, 7055, 3761]
    solution = Solution()
    print(solution.minIncrements(n, cost))

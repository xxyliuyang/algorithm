# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# File   : L5.py
# Time   : 2022/10/15 8:05 PM
"""

class Solution:
    """
    https://writings.sh/post/algorithm-longest-palindromic-substring#%E4%BA%8C%E7%BB%B4%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E6%96%B9%E6%B3%95
    """
    def longestPalindrome(self, s: str) -> str:
        """动态规划"""
        if len(s) <= 1:
            return s

        res = ""
        max_len = 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i]==s[j]:
                    if i+1<=j-1:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j]=True
                if dp[i][j] and (j-i+1)>max_len:
                    res=s[i:j+1]
                    max_len = j-i+1
        return res

    def longestPalindrome2(self, s: str) -> str:
        def _find_by_position(left, right, s):
            while (left>=0 and right < len(s)) and s[left]==s[right]:
                left -= 1
                right += 1
            if left>=0 and right < len(s) and s[left]==s[right]:
                return left, right
            return left+1, right-1
        """中心点"""
        if len(s) <= 1:
            return s
        res = ""
        for i in range(len(s)):
            left1, right1 = _find_by_position(i, i, s)
            if (right1-left1+1)>len(res):
                res = s[left1: right1+1]
            if i+1 < len(s) and s[i] == s[i+1]:
                left2, right2 = _find_by_position(i, i+1, s)
                if (right2-left2+1)>len(res):
                    res = s[left2: right2 + 1]
        return res
if __name__ == '__main__':
    s = "babad"
    solution = Solution()
    print(solution.longestPalindrome2(s))
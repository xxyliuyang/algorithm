from typing import List
from copy import deepcopy


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def is_palindrome(self, s: str):
        return s == s[::-1]

    def backtrack(self, s, start):
        if start == len(s):
            self.result.append(deepcopy(self.path))
            return

        for i in range(start, len(s)):
            if not self.is_palindrome(s[start: i+1]):
                continue
            self.path.append(s[start: i+1])
            self.backtrack(s, i+1)
            self.path.pop()

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return self.result

        self.backtrack(s, 0)
        return self.result


if __name__ == '__main__':
    s = "aab"
    solution = Solution()
    print(solution.partition(s))

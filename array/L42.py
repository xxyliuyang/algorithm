"""
金典的装雨水的问题
"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        for i in range(1, len(height)-1):
            lm = max(height[:i])
            rm = max(height[i:])
            result += max(0, min(lm, rm) - height[i])
        return result

    def trap2(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        max_left[0] = height[0]
        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i - 1])
        max_right[-1] = height[-1]
        for i in range(len(height) - 2, 0, -1):
            max_right[i] = max(height[i], max_right[i + 1])

        result = 0
        for i in range(1, len(height) - 1):
            min_value = min(max_left[i], max_right[i])
            result += max(0, min_value - height[i])
        return result


if __name__ == '__main__':
    solution = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(solution.trap2(height))
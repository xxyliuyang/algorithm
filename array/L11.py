from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<2:
            return 0

        left = 0
        right = len(height)-1
        max_area = 0
        while left<right:
            mheight = min(height[left], height[right])
            new_area = mheight * (right-left)
            max_area = max(max_area, new_area)

            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
        return max_area

if __name__ == '__main__':
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    print(solution.maxArea(nums))
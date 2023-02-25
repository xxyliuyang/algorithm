from typing import List


class Solution:
    def get_samll_number(self, nums, value, right_position):
        r = 0
        for i in range(right_position):
            if nums[i] < value:
                r += 1
        return r

    def get_large_number(self, nums, value, left_position):
        r = 0
        for i in range(left_position + 1, len(nums)):
            if nums[i] > value:
                r += 1
        return r

    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for k in range(n - 1, -1, -1):
            for j in range(0, k):
                if nums[k] < nums[j]:
                    res += self.get_samll_number(nums, nums[k], j) * self.get_large_number(nums, nums[j], k)
        return res


if __name__ == '__main__':
    nums = [1, 3, 2, 4, 5]
    solution = Solution()
    print(solution.countQuadruplets(nums))

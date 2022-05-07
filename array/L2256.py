from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        left_sum = [0 for _ in range(len(nums))]
        right_sum = [0 for _ in range(len(nums))]

        left_sum[0] = nums[0]
        for i in range(1, len(nums)):
            left_sum[i] = left_sum[i-1] + nums[i]
        for i in range(len(nums)-2, -1, -1):
            right_sum[i] = right_sum[i+1] +nums[i+1]

        min_index = 0
        min_avg = float("inf")
        for i in range(len(nums)):
            left_length = i+1
            right_length = len(nums)-i-1
            left_avg = left_sum[i]//left_length
            right_avg = 0
            if right_length > 0:
                right_avg = right_sum[i] // right_length

            diff = abs(left_avg - right_avg)
            if diff < min_avg:
                min_avg = diff
                min_index = i
        return min_index



if __name__ == '__main__':
    nums = []
    solution = Solution()
    print(solution.minimumAverageDifference(nums))

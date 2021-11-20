# 讲解：https://mp.weixin.qq.com/s/u2vh9dYOV-fOYoYT-ihF2w

from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums = [nums[0]] + nums

        cur_iff = 0
        pre_diff = 0
        count = 1
        for i in range(1, len(nums)):
            cur_iff = nums[i] - nums[i-1]
            if (cur_iff >0 and pre_diff <= 0) or (cur_iff<0 and pre_diff>=0):
                count += 1
                pre_diff = cur_iff
        return count

if __name__ == '__main__':
    nums = [1, 7, 4, 9, 2, 5]
    solution = Solution()

    print(solution.wiggleMaxLength(nums))
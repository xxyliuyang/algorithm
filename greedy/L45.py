# 讲解： https://mp.weixin.qq.com/s/a9p5gbPAGlwzQDsRKootyw
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_far = 0
        count = 0
        next_far = 0

        for i in range(len(nums)-1):
            next_far = max(next_far, nums[i]+i)
            if i == cur_far:
                count += 1
                cur_far = next_far
        return count

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    solution = Solution()

    print(solution.jump(nums))